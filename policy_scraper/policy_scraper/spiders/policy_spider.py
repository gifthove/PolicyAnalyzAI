import scrapy
import os  # Ensure os is imported
from urllib.parse import urljoin
from scrapy.utils.response import get_base_url


class PolicySpider(scrapy.Spider):
    name = "policy_spider"
    allowed_domains = ["otago.ac.nz"]
    start_urls = ["https://www.otago.ac.nz/staff/policies"]

    def parse(self, response):
        """
        Parse the main policy page and extract links to individual policies.
        """
        self.logger.info("Parsing main policy page")
        policy_links = response.css("a::attr(href)").getall()

        for link in policy_links:
            absolute_url = urljoin(get_base_url(response), link)

            # Skip mailto links and unsupported content types
            if absolute_url.startswith("mailto:") or any(
                ctype in absolute_url for ctype in self.settings.get("IGNORED_CONTENT_TYPES", [])
            ):
                self.logger.info(f"Ignoring unsupported link: {absolute_url}")
                continue

            # Send request to parse individual policy pages
            yield scrapy.Request(url=absolute_url, callback=self.parse_policy)

    def parse_policy(self, response):
        """
        Parse the policy page to save the content or download files.
        """
        # Check for non-HTML responses and skip them
        content_type = response.headers.get("Content-Type", b"text/html").decode("utf-8").split(";")[0]

        if content_type != "text/html":
            self.logger.info(f"Skipping non-HTML content: {response.url}")
            return

        # Extract and clean the policy title
        policy_title = response.css("title::text").get()
        if not policy_title:
            policy_title = "default_policy"
        policy_title = policy_title.strip().replace("/", "-").replace("\\", "-")

        # Yield policy HTML content for saving via pipeline
        yield {
            "type": "policy",
            "url": response.url,
            "title": policy_title,
            "content": response.body.decode("utf-8"),
        }

        # Extract downloadable links for files
        file_links = response.css("a::attr(href)").getall()
        for file_link in file_links:
            absolute_file_url = urljoin(get_base_url(response), file_link)
            if any(absolute_file_url.endswith(ext) for ext in [".pdf", ".doc", ".docx"]):
                yield scrapy.Request(
                    url=absolute_file_url,
                    callback=self.save_file,
                    meta={"file_name": os.path.basename(file_link)},
                )

    def save_file(self, response):
        """
        Save downloadable files like PDFs or Word documents.
        """
        file_name = response.meta.get("file_name", "downloaded_file")
        content_type = response.headers.get("Content-Type", b"").decode("utf-8")

        # Determine the type of file and yield it for saving via pipeline
        if "application/pdf" in content_type:
            file_type = "pdf"
        elif "application/msword" in content_type or "application/vnd.openxmlformats-officedocument" in content_type:
            file_type = "file"
        else:
            self.logger.info(f"Skipping unsupported file type: {response.url}")
            return

        yield {
            "type": file_type,
            "url": response.url,
            "file_name": file_name,
            "content_type": content_type,
            "content": response.body,
        }
