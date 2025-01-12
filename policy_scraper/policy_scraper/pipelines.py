import os
import base64
import json
from slugify import slugify
from policy_scraper.cleaning import clean_html
from policy_scraper.tokenizing import tokenize_text
from whoosh import index
from whoosh.fields import Schema, TEXT, ID
from whoosh.writing import AsyncWriter
from policy_scraper.consolidator import consolidate_data  # Import the consolidator


class PolicyScraperPipeline:
    def open_spider(self, spider):
        """
        Called when the spider is opened. Ensures the necessary directories exist
        and initializes the Whoosh index.
        """
        self.base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

        # Correct paths according to the PolicyAnalyzAI folder structure
        self.policy_dir = os.path.join(self.base_dir, "data", "raw", "policies")
        self.clean_files_dir = os.path.join(self.base_dir, "data", "processed", "clean_json_files")
        self.tokenized_files_dir = os.path.join(self.base_dir, "data", "processed", "tokenized_json_files")
        self.index_dir = os.path.join(self.base_dir, "output", "index")
        self.pdf_dir = os.path.join(self.base_dir, "data", "raw", "pdfs")
        self.file_dir = os.path.join(self.base_dir, "data", "raw", "files")

        os.makedirs(self.policy_dir, exist_ok=True)
        os.makedirs(self.clean_files_dir, exist_ok=True)
        os.makedirs(self.tokenized_files_dir, exist_ok=True)
        os.makedirs(self.pdf_dir, exist_ok=True)
        os.makedirs(self.file_dir, exist_ok=True)
        os.makedirs(self.index_dir, exist_ok=True)

        # Initialize Whoosh index
        self.schema = Schema(
            id=ID(stored=True, unique=True),
            title=TEXT(stored=True),
            content=TEXT(stored=True),
            url=ID(stored=True),
        )
        if not index.exists_in(self.index_dir):
            self.index = index.create_in(self.index_dir, self.schema)
        else:
            self.index = index.open_dir(self.index_dir)

    def process_item(self, item, spider):
        """
        Processes each item based on its type (policy, file, etc.).
        """
        if item.get("type") == "policy":
            self.save_policy(item, spider)
            self.save_cleaned_policy(item, spider)
            self.save_tokenized_policy(item, spider)
            self.index_policy(item, spider)
        elif item.get("type") == "file":
            self.save_file(item, spider)
        return item

    def save_policy(self, item, spider):
        """
        Saves the original HTML content of a policy.
        """
        file_name = slugify(item.get("title", "default_policy")) + ".html"
        file_path = os.path.join(self.policy_dir, file_name)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(item.get("content", ""))
        spider.logger.info(f"✅ Saved policy HTML: {file_path}")

    def save_cleaned_policy(self, item, spider):
        """
        Saves the cleaned text content of a policy.
        """
        cleaned_text = clean_html(item.get("content", ""))
        file_name = slugify(item.get("title", "default_policy")) + ".json"
        file_path = os.path.join(self.clean_files_dir, file_name)

        cleaned_data = {
            "title": item.get("title"),
            "url": item.get("url"),
            "cleaned_content": cleaned_text,
        }

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(cleaned_data, f, ensure_ascii=False, indent=4)
        spider.logger.info(f"✅ Saved cleaned policy JSON: {file_path}")

    def save_tokenized_policy(self, item, spider):
        """
        Saves the tokenized word and sentence data of a policy.
        """
        try:
            cleaned_text = clean_html(item.get("content", ""))
            tokens = tokenize_text(cleaned_text)
            spider.logger.info(f"🔎 Tokenized {len(tokens['word_tokens'])} words and {len(tokens['sentence_tokens'])} sentences.")

            file_name = slugify(item.get("title", "default_policy")) + ".json"
            file_path = os.path.join(self.tokenized_files_dir, file_name)

            tokenized_data = {
                "title": item.get("title"),
                "url": item.get("url"),
                "word_tokens": tokens["word_tokens"],
                "sentence_tokens": tokens["sentence_tokens"],
            }

            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(tokenized_data, f, ensure_ascii=False, indent=4)
            spider.logger.info(f"✅ Saved tokenized policy JSON: {file_path}")
        except Exception as e:
            spider.logger.error(f"❌ Error in save_tokenized_policy: {e}")

    def index_policy(self, item, spider):
        """
        Index the policy content for search.
        """
        try:
            cleaned_text = clean_html(item.get("content", ""))
            writer = AsyncWriter(self.index)

            writer.add_document(
                id=slugify(item.get("title", "default_policy")),
                title=item.get("title", "Untitled"),
                content=cleaned_text,
                url=item.get("url", "Unknown URL")
            )
            writer.commit()
            spider.logger.info(f"📦 Indexed policy: {item.get('title')}")
        except Exception as e:
            spider.logger.error(f"❌ Error indexing policy: {e}")

    def close_spider(self, spider):
        """
        Called when the spider is closed. Triggers data consolidation.
        """
        try:
            spider.logger.info("🔄 Starting data consolidation...")

            consolidate_data(
                clean_dir=self.clean_files_dir,
                tokenized_dir=self.tokenized_files_dir,
                output_file=os.path.join(self.base_dir, "data", "processed", "consolidated_data.json")
            )

            spider.logger.info("✅ Data consolidation completed successfully.")
        except Exception as e:
            spider.logger.error(f"❌ Error consolidating data: {e}")


class BytesToBase64Pipeline:
    """
    Converts byte fields in items to base64-encoded strings.
    """
    def process_item(self, item, spider):
        for key, value in item.items():
            if isinstance(value, bytes):
                item[key] = base64.b64encode(value).decode("utf-8")
        return item
