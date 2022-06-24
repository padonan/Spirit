import scrapy

Associate_Degree = '4' # 2~3년제
Bachelor_Degree = '5' # 4년제
Master_Degree = '6' # 석사
Doctor_Degree = '7' # 박사
HighSchool_Degree = '3' # 고졸
NO_CARE_Degree = '0' # 학력무관

KEYWORD = input('찾고 싶은 키워드를 입력해주세요 (키워드는 띄어쓰기로 구분 됩니다) : ')
INPUTKEYWORD = ''.join(KEYWORD)
CARRER = '&careerType=2' + '&careerMin=' + input('요구경력최소:') + '&careerMax=' + input('요구경력최대:')
INPUTCARRER = ''.join(CARRER)
EDU = '&edu=' + input('학력입력 (3)고졸 (4)전문대 (5)4년제 (6)석사 (7)박사 (0)학력무관 : ')
INPUTEDU = ''.join(EDU)
PAY = '&payType=1' + '&payMin=' + input('원하는 최소연봉:') + '&payMax=' + input('원하는 최대연봉:')
INPUTPAY = ''.join(PAY)

URL = 'https://www.jobkorea.co.kr/Search/?stext=' + INPUTKEYWORD + INPUTCARRER + INPUTEDU + INPUTPAY + '&recruit&Page_No=%s'
start_page = 1

class MainSpider(scrapy.Spider):
    name = 'MainSpider'

    start_urls = [URL % start_page]


    def parse(self, response):
            for y in range(1, 21):
                COMPANY = response.xpath(f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{y}]/div/div[1]/a/text()')[0].extract()
                print(COMPANY) # COMPANY 

                TITLE = response.xpath(f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{y}]/div/div[2]/a/text()')[0].extract()
                print(TITLE) # TITLE 

                CARRER = response.xpath(f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{y}]/div/div[2]/p[1]/span[1]/text()')[0].extract() 
                print(CARRER) # 경력

                ACADEMIC_ABILITY = response.xpath(f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{y}]/div/div[2]/p[1]/span[2]/text()')[0].extract()
                print(ACADEMIC_ABILITY) # 학력

                EMPLOYMENT_TYPE = response.xpath(f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{y}]/div/div[2]/p[1]/span[3]/text()')[0].extract()
                print(EMPLOYMENT_TYPE) # 고용형태

                AREA = response.xpath(f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{y}]/div/div[2]/p[1]/span[5]/text()')[0].extract()
                print(AREA) # 지역

                RECUITMENT_TYPE = response.xpath(f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{y}]/div/div[2]/p[1]/span[6]/text()')[0].extract()
                print(RECUITMENT_TYPE) # 채용형태

                RECUITMENT_PERIOD = response.xpath(f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{y}]/div/div[2]/p[1]/span[6]/text()')[0].extract()
                print(RECUITMENT_PERIOD) # 모집기간

                POST_REGISTRATION_TIME = None

                OTHER_CONTENTS = response.xpath(f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{y}]/div/div[2]/p[2]/text()')[0].extract()
                print(OTHER_CONTENTS) # 기타내용

                xpath_url = response.xpath(f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{y}]/div/div[2]/a/@href')[0].extract()
                URL = 'https://www.jobkorea.co.kr' + xpath_url 
                print(URL,end='\n\n')  # URL 
