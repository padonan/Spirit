# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
import pymysql
import sys

class FightingPipeline(object):

    def __init__(self):
        try:
            self.conn = pymysql.connect(
                user = "root",
                password = '',
                host = 'cldb.c838wggzqfla.ap-northeast-2.rds.amazonaws.com',
                port = 3306,
                db = "CLDB",
                charset = "utf8"
            )
            print("DB connected")
        except pymysql.Error as e:
            print(f"Error connecting to pymysql Platform: {e}")
            sys.exit(1)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = "INSERT INTO DB (homepage, COMPANY, TITLE, career, ACADEMIC, EMPLOYMENT, AREA, PERIOD, URL, etc) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        self.cursor.execute(sql, ( (item['HOMEPAGE'].encode('utf-8')),(item['COMPANY'].encode('utf-8')), (item['TITLE'].encode('utf-8')), (item['CARRER'].encode('utf-8')), (item['ACADEMIC_ABILILTY'].encode('utf-8')), (item['EMPLOYMENT_TYPE'].encode('utf-8')), (item['AREA'].encode('utf-8')), (item['RECUITMENT_PERIOD'].encode('utf-8')),(item['URL'].encode('utf-8')), (item['OTHER_CONTENTS'].encode('utf-8')) ))
        self.conn.commit()
        print("DB inserted")
        return item



# pymysql을 이용한 aws서버내의 DB커넥트 및 인서트, items의 변수들을 받아온다



































# class Fighting_DBPipeline(object):
# 	def __init__(self):
# 		try:
# 			self.conn = MySQLdb.connect(user='root', passwd='1234', db='test1', host='localhost', charset="utf8", use_unicode=True)
# 			#print("1")
# 			self.cursor = self.conn.cursor()
# 			#print("2")
# 		except MySQLdb.Error:
# 			sys.exit(1)					
# 		#log data to json file


# 	def process_item(self, item, spider): 		
# 		# create record if doesn't exist. 
# 		self.cursor.execute("select * from test1.new_table where new_table name = %s and link = %s and company = %s and receiptdate = %s and result_date = %s", 
#         (item['aptname'][0].encode('utf-8'), "http://www.apt2you.com/houseSaleDetailInfo.do?manageNo="+item['link'][0].encode('utf-8'), item['company'][0].encode('utf-8'), 
#         item['receiptdate'][0].encode('utf-8'), item['result_date'][0].encode('utf-8')))
# 		result = self.cursor.fetchone()
    
# 		# print "select * from apt2u.apt where aptname = '%s' and link = 'http://www.apt2you.com/houseSaleDetailInfo.do?manageNo=%s' and 
#         # company = '%s' and receiptdate = '%s' and result_date = '%s'" % (item['aptname'][0].encode('utf-8'), item['link'][0].encode('utf-8'), 
#         # item['company'][0].encode('utf-8'), item['receiptdate'][0].encode('utf-8'), item['result_date'][0].encode('utf-8'))

# 		if result:
# 			print("data already exist")		
# 		else:
# 			try:
# 				self.cursor.execute("insert into apt2u.apt(aptname, link, company, receiptdate, result_date) values (%s, %s, %s, %s, %s)", 
#                 (item['aptname'][0].encode('utf-8'), "http://www.apt2you.com/houseSaleDetailInfo.do?manageNo="+item['link'][0].encode('utf-8'), 
#                 item['company'][0].encode('utf-8'), item['receiptdate'][0].encode('utf-8'), item['result_date'][0].encode('utf-8')))
# 				self.conn.commit()
# 			except MySQLdb.Error:
# 				return item

