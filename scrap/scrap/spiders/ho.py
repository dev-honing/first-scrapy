# scrap/scrap/spiders/ho.py
import scrapy
import json
from datetime import datetime

class HoSpider(scrapy.Spider):
    name = "ho"
    allowed_domains = ["velog.io"]
    start_urls = ["https://velog.io/@dev-honing/%ED%85%8C%EC%8A%A4%ED%8A%B8"]

    def parse(self, response):
        h1_elements = response.css('h1::text').getall()
        h2_elements = response.css('h2::text').getall()
        h3_elements = response.css('h3::text').getall()

        # 저장할 데이터 양식
        data = {
            "일시": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "h1": h1_elements,
            "h2": h2_elements,
            "h3": h3_elements
        }

        # 기존 데이터 로드 및 초기화
        try:
            # 기존 데이터 로딩
            with open('output.json', 'r', encoding='utf-8') as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            # 파일이 없으면 빈 리스트 생성
            existing_data = []
        
        # 새로운 데이터 추가
        existing_data.append(data)

        # 업데이트된 데이터 저장
        with open('output.json', 'w', encoding='utf-8') as file:
            json.dump(existing_data, file, ensure_ascii=False, indent=2)

        self.log('output.json 파일에 데이터 저장 완료')
