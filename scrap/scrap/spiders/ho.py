# scrap/scrap/spiders/ho.py
import scrapy

class HoSpider(scrapy.Spider):
    name = "ho"
    allowed_domains = ["velog.io"]
    start_urls = ["https://velog.io/@dev-honing/%ED%85%8C%EC%8A%A4%ED%8A%B8"]

    def parse(self, response):
        # h1 태그의 텍스트를 추출합니다.
        h1_text = response.css('h1::text').get()
        
        # h2 태그의 텍스트를 추출합니다.
        h2_text = response.css('h2::text').get()

        # h3 태그의 텍스트를 추출합니다.
        h3_text = response.css('h3::text').get()
        
        # 추출된 데이터를 출력합니다.
        yield {
            'h1': h1_text,
            'h2': h2_text,
            'h3': h3_text
        }
