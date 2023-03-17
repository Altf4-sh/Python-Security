import scrapy
from scrapy import signals

from pony.orm import *
db = Database("sqlite", "../europython.sqlite", create_db=True)

class EuropythonSession(db.xxx):
	"""Pony ORM model of the europython session table"""
	id = PrimaryKey(int, auto=True)
	author = xxx(str)
	title = Required(str)
	description = xxx(str)
	date = xxx(str)
	tags = xxx(str)
	
class EuropythonSQLitePipeline(object):
    
    @classmethod
    def from_crawler(cls, xxx):
        pipeline = cls()
        crawler.signals.xxx(xxx, xxx)
        crawler.signals.xxx(xxx, xxx)
        return pipeline
	
    def spider_opened(self, xxx):
        db.xxx(check_tables=True, create_tables=True)

    def spider_closed(self, xxx):
        db.xxx()

    # Insert data in database
    @db_session
    def process_item(self, xxx, xxx):
        # use db_session as a context manager
        with xxx:
            try:
                strAuthor = str(xxx['author'])
                strAuthor = xxx[2:len(strAuthor)-2]
                
                strTitle = str(xxx['title'])
                strTitle = xxx[2:len(strTitle)-2]
        
                strDescription = str(xxx['description'])
                strDescription = xxx[2:len(strDescription)-2]
                strDate = str(xxx['date'])
                strDate = xxx.replace("[u'", "").replace("']", "").replace("u'", "").replace("',", ",")
                strTags = str(xxx['tags'])
                strTags = xxx.replace("[u'", "").replace("']", "").replace("u'", "").replace("',", ",")
                europython_session = EuropythonSession(author=xxx,title=xxx,description=xxx,date=strDate,tags=xxx)
            except Exception as e:
                print("Error processing the items in the DB %d: %s" % (e.args[0], e.args[1]))
            return xxx
