import scrapy
from scrapy.http import Request
from Fighting.items import FightingItem


KEYWORD = input('찾고 싶은 키워드를 입력해주세요 (키워드는 띄어쓰기로 구분 됩니다) : ')
INPUTKEYWORD = ''.join(KEYWORD)

JOBKOREA_URL = 'https://www.jobkorea.co.kr/Search/?stext=' + INPUTKEYWORD +'&recruit&Page_No=%s'
SARAMIN_URL = 'https://www.saramin.co.kr/zf_user/search?searchType=search&searchword=' + INPUTKEYWORD + '&recruitPage=%s'
start_page = 0


class MainSpider(scrapy.Spider):
    name = 'MainSpider'

    def start_requests(self):
        for i in range(1, 10, 1): # 0, 1
            yield Request(url=JOBKOREA_URL % (i + start_page), callback=self.jobkorea_parse) # 콜백 함수를 이용해 페이지별로 크롤링
        for i in range(1, 10, 1):
            yield Request(url=SARAMIN_URL % (i + start_page), callback=self.saramin_parse)


    def jobkorea_parse(self, response):
            item = FightingItem()

            for y in range(1, 21, 1):

                HOMEPAGE = 'jobkorea'

                item['COMPANY'] = response.xpath(f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{y}]/div/div[1]/a/text()')[0].extract()

                item['TITLE'] = response.xpath(f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{y}]/div/div[2]/a/text()')[0].extract().lstrip()

                item['CARRER'] = response.xpath(f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{y}]/div/div[2]/p[1]/span[1]/text()')[0].extract()

                item['ACADEMIC_ABILILTY'] = response.xpath(f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{y}]/div/div[2]/p[1]/span[2]/text()')[0].extract()
    
                item['EMPLOYMENT_TYPE'] = response.xpath(f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{y}]/div/div[2]/p[1]/span[3]/text()')[0].extract()

                item['AREA'] = response.xpath(f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{y}]/div/div[2]/p[1]/span[5]/text()')[0].extract()

                # item['RECUITMENT_TYPE'] = response.xpath(f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{y}]/div/div[2]/p[1]/span[6]/text()')[0].extract()
        
                item['RECUITMENT_PERIOD'] = response.xpath(f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{y}]/div/div[2]/p[1]/span[6]/text()')[0].extract()

                item['OTHER_CONTENTS'] = response.xpath(f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{y}]/div/div[2]/p[2]/text()')[0].extract()

                xpath_url = response.xpath(f'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li[{y}]/div/div[2]/a/@href')[0].extract()
                item['URL'] = 'https://www.jobkorea.co.kr' + xpath_url 

                if xpath_url == None:
                    HOMEPAGE = None

                item['HOMEPAGE'] = HOMEPAGE    

                yield item

    def saramin_parse(self, response):
            item = FightingItem()

            for y in range(1, 40, 1):

                HOMEPAGE = 'saramin'
             
                item['COMPANY'] = response.xpath(f'//*[@id="recruit_info_list"]/div[1]/div[{y}]/div[2]/strong/a/text()')[0].extract().lstrip()
                item['TITLE'] = response.xpath(f'//*[@id="recruit_info_list"]/div[1]/div[{y}]/div[1]/h2/a/span/text()')[0].extract()

                CARRER = response.xpath(f'//*[@id="recruit_info_list"]/div[1]/div[{y}]/div[1]/div[3]/span[2]/text()')[0].extract()
                if '무관' in CARRER:
                    CARRER = '신입'
                item['CARRER'] = CARRER

                item['ACADEMIC_ABILILTY'] = response.xpath(f'//*[@id="recruit_info_list"]/div[1]/div[{y}]/div[1]/div[3]/span[3]/text()')[0].extract() 
                item['EMPLOYMENT_TYPE'] = response.xpath(f'//*[@id="recruit_info_list"]/div[1]/div[{y}]/div[1]/div[3]/span[4]/text()')[0].extract()

                Extract_AREA = response.xpath(f'//*[@id="recruit_info_list"]/div[1]/div[{y}]/div[1]/div[3]/span[1]/a[1]/text()').extract()
                Extract_AREA2 = response.xpath(f'//*[@id="recruit_info_list"]/div[1]/div[{y}]/div[1]/div[3]/span[1]/a[2]/text()').extract()
                AREA = Extract_AREA + Extract_AREA2
                item['AREA'] = AREA[0]
                item['RECUITMENT_PERIOD'] = response.xpath(f'//*[@id="recruit_info_list"]/div[1]/div[{y}]/div[1]/div[2]/span/text()')[0].extract()

                
                Extract_etc = []
                for x in range (1, 4):
                    Extract_etc_a_list = response.xpath(f'//*[@id="recruit_info_list"]/div[1]/div[{y}]/div[1]/div[4]/a[{x}]/text()').extract()
                    Extract_etc.extend(Extract_etc_a_list)
                    for z in range (1, 4):
                        Extract_etc_b_list = response.xpath(f'//*[@id="recruit_info_list"]/div[1]/div[{y}]/div[1]/div[4]/b[{x}]/a[{z}]/text()').extract()
                    Extract_etc.extend(Extract_etc_b_list)    
                ETC = ",".join(Extract_etc)

                item['OTHER_CONTENTS'] = ETC

                Xpath_URL = response.xpath(f'//*[@id="recruit_info_list"]/div[1]/div[{y}]/div[1]/h2/a/@href')[0].extract()
                URL = 'https://www.saramin.co.kr' + Xpath_URL 
                item['URL'] = URL
                # BOARD_TIME = response.xpath(f'//*[@id="recruit_info_list"]/div[1]/div[{y}]/div[1]/div[4]/span/text()')[0].extract()
                # print(BOARD_TIME)
                
                if Xpath_URL == None:
                    HOMEPAGE = None
                
                item['HOMEPAGE'] = HOMEPAGE  

                yield item


# 잡코리아 크롤링 끝
