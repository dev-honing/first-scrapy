import scrapy


class HoSpider(scrapy.Spider):
    name = "ho"
    allowed_domains = ["velog.io"]
    start_urls = ["https://velog.io/@dev-honing/%ED%85%8C%EC%8A%A4%ED%8A%B8"]

    def parse(self, response):
        pass
