# first-scrapy
## 가상환경 세팅
### 1. 터미널 전환
VS Code 터미널을 PowerShell에서 Command Prompt로 전환
### 2. 가상환경 venv 생성
`python -m venv .venv`
### 3. 가상환경 실행
`.venv\Scripts\activate.bat`
### 4. Git Ignore 세팅
`echo .venv/ >> .gitignore`

## Scrapy
### 1. Scrapy 프로젝트 생성
`scrapy startproject scrap`

scrap이라는 새로운 프로젝트 생성
### 2. 디렉토리 전환
`cd scrap/`
### 3. spider 생성
`scrapy genspider <스파이더명> <도메인명>`

`(.venv) C:\Users\Administrator\Desktop\ho\first-scrapy\scrap>scrapy genspider ho https://velog.io/@dev-honing/%ED%85%8C%EC%8A%A4%ED%8A%B8`
### 4. spider 편집
디렉토리 이동
스파이더명.py 파일 수정
```
# scrap/scrap/spiders/ho.py
import scrapy

class HoSpider(scrapy.Spider):
    name = "ho"
    allowed_domains = ["velog.io"]
    start_urls = ["https://velog.io/@dev-honing/%ED%85%8C%EC%8A%A4%ED%8A%B8"]

    def parse(self, response):
        # h1 태그의 텍스트를 추출
        h1_text = response.css('h1::text').get()
        
        # h2 태그의 텍스트를 추출
        h2_text = response.css('h2::text').get()

        # h3 태그의 텍스트를 추출
        h3_text = response.css('h3::text').get()
        
        # 추출된 데이터를 출력
        yield {
            'h1': h1_text,
            'h2': h2_text,
            'h3': h3_text
        }
```
### 5. 크롤봇 실행
`scrapy crawl ho`

### 6. 크롤링 내용 저장
`scrapy crawl ho -o output.json`