# scrap/scrap/spiders/ho.py
import scrapy
from datetime import datetime

class HoSpider(scrapy.Spider):
    name = "ho"
    allowed_domains = ["velog.io"]
    start_urls = ["https://velog.io/@dev-honing/%ED%85%8C%EC%8A%A4%ED%8A%B8"]

    def parse(self, response):
        # 현재 일시 가져오기(형식: YYYY-MM-DD hh:mm)
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        # 추출할 태그들을 리스트로 지정
        tags = ['h1', 'h2', 'h3']
        
        # 각 태그를 반복해 텍스트 추출
        extracted_data = {}
        for tag in tags:
            # 해당 태그의 텍스트를 추출
            text = response.css(f'{tag}::text').getall()
            # 추출된 텍스트를 딕셔너리에 저장
            extracted_data[tag] = text

        # 추출된 데이터와 일시를 출력
        item = {
            '일시': now,
            **extracted_data
        }
        
        # 각 아이템을 리스트에 저장해 출력
        yield item
