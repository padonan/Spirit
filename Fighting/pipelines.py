# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from twisted.enterprise import adbapi
import datetime
import logging
import MySQLdb.cursors
from scrapy.exceptions import DropItem
from Fighting.items import FightingItem
import sys

class FightingPipeline:
    def process_item(self, item, spider):
        return item







































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

