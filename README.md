# Spirit

0627

잡코리아 사이트 크롤링 => items를 거친 딕셔너리 크롤링데이터 생성까지완료

scrapy 에서 DB에 접속은 되는데 insert가 안됨.. 해결예정


0708

잡코리아, 사람인, 커리어 3개 사이트 크롤링 및 DB INSERT 완료

원티드 사이트 하나남았는데... 반응형 웹사이트라 방법 구현이 필요합니다

























# **Scrapy 사용법**

<br/>

## **1. Scrapy 설치하기**

<br/>

터미널을 열어 Scrapy 설치를 진행한다. 설치를 진행하기 전 Linux에서 pip를 최신버전으로 업데이트를 진행해주자


```
# pip 업그레이드

pip install --upgrade pip

# Scrapy 설치

pip install scrapy

# Scrapy 버전확인

scrapy version
```

## **2. Scrapy 실행하기**

<br/>

spider 파일실행 =  터미널에서 **scrapy crawl [스파이더 이름]** 명령어로 실행시킬 수 있다

<br/>

```
scrapy crawl MainSpider
```

<br/>

## **3. LOG파일 생성하기**

<br/>

scrapy를 실행시킨다면 실행창에 log가 주르륵 나올거다. 이 로그들을 실행시킬 때 터미널에서 보이지 않고 하나의 파일안에 쌓이도록 하기 위해 log 파일을 생성하자. settings 파일안으로 들어가 **LOG_FILE = '[로그 파일 명].log'**를 추가하자 그럼 scrapy를 실행 시킬 때 로그들이 해당 파일에 저장이 된다. 만약 log파일 없이 log를 없애고 싶다면 scrapy 실행을 시킬 때  **--nolog** 를 붙여 실행하면 log 파일 생성 없이 log가 나오지 않는다

<br/>

```
#로그파일 생성

LOG_FILE = 'MainSpider.log'

#로그파일 생성없이 로그 없애기

scrapy crawl MainSpider --nolog
```

<br/>

## **4. 크롤링 데이터 CSV 파일에 저장하기**

<br/>

크롤링한 데이터를 CSV파일에 저장시키려면 scrapy를 실행할 때 **-o [csv 파일 명].csv**을 추가 해서 실행시키자 그럼 실행 값들이 csv파일로 저장이 된다.

<br/>

```
scrapy crawl MainSpider -o [csv 파일 명].csv 

#csv 파일 저장 + --nolog

scrapy crawl MainSpider -o [csv 파일 명].csv --nolog

```

<br/>

## **참고**

<br/>

[Xpath 사용방법](https://nittaku.tistory.com/136)
