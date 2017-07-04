import requests
from lxml import html
import multiprocessing
import time

# Try to crawl all the courses in 163course.

start_url = 'http://www.icourse163.org/'

course_url_list = []

headers = {
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'
}
#Headers is important

def get_all_course_urls(url)：
  time.sleep(2)
  r = requests.get(start_url,headers = headers)

  tree = lxml.html.fromstring(r.content)

  urllist = tree.xpath('//a/@href')


  for item in urllist:
    if 'http://www.icourse163.org/course/' in item and item not in course_url_list:
      course_url_list.append(item)
    else:
      #If the url doesn't meet the form of course url, we should crawl inside to the url
      #It will be easier to do this by Scrapy, but we will make it by ourselves
      get_all_course_urls(item)
 

