# Spirit

0627

잡코리아 사이트 크롤링 => items를 거친 딕셔너리 크롤링데이터 생성까지완료

scrapy 에서 DB에 접속은 되는데 insert가 안됨.. 해결예정


0708

잡코리아, 사람인, 커리어 3개 사이트 크롤링 및 DB INSERT 완료

원티드 사이트 하나남았는데... 반응형 웹사이트라 방법 구현이 필요합니다

























# **Scrapy 실행방법**

<br/>

## **1. Scrapy 설치**

<br/>

pip install scrapy

<br/>


## **2. Scrapy 실행**

<br/>

scrapy crawl [스파이더 이름]

<br/>

```
scrapy crawl MainSpider
```

<br/>

## **3. CSV 파일로 저장**

-o [csv 파일명].csv을 추가


<br/>

```
scrapy crawl MainSpider -o [csv 파일명].csv 

#csv 파일 저장 + --nolog

scrapy crawl MainSpider -o [csv 파일명].csv --nolog

```

<br/>

## **참고한 사이트**

<br/>

[개발환경셋팅](https://truelifer.medium.com/scrapy-%EA%B8%B0%EB%B0%98-daum-news-crawler-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0-e8b93f8e519d)

[Xpath 사용방법](https://nittaku.tistory.com/136)

[Xpath 문법](https://www.fun-coding.org/crawl_advance5.html)

[DB insert] (https://velog.io/@new_wisdom/Python-Mysql-%EC%97%B0%EB%8F%99%ED%95%98%EA%B8%B0-insert)
