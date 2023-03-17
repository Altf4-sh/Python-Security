import scrapy
from scrapy import signals

from pony.orm import *
db = Database("sqlite", "../europython.sqlite", create_db=True)

class EuropythonSession(db.Entity):
	"""Pony ORM model of the europython session table"""
	id = PrimaryKey(int, auto=True)
	author = Required(str)
	title = Required(str)
	description = Required(str)
	date = Required(str)
	tags = Required(str)
	
class EuropythonSQLitePipeline(object):
    
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline
	
    def spider_opened(self, spider):
        db.generate_mapping(check_tables=True, create_tables=True)

    def spider_closed(self, spider):
        db.commit()

    # Insert data in database
    @db_session
    def process_item(self, item, spider):
        # use db_session as a context manager
        with db_session:
            try:
                strAuthor = str(item['author'])
                strAuthor = strAuthor[2:len(strAuthor)-2]
                
                strTitle = str(item['title'])
                strTitle = strTitle[2:len(strTitle)-2]
        
                strDescription = str(item['description'])
                strDescription = strDescription[2:len(strDescription)-2]
                strDate = str(item['date'])
                strDate = strDate.replace("[u'", "").replace("']", "").replace("u'", "").replace("',", ",")
                strTags = str(item['tags'])
                strTags = strTags.replace("[u'", "").replace("']", "").replace("u'", "").replace("',", ",")
                europython_session = EuropythonSession(author=strAuthor,title=strTitle,description=strDescription,date=strDate,tags=strTags)
            except Exception as e:
                print("Error processing the items in the DB %d: %s" % (e.args[0], e.args[1]))
            return item
