import requests
from lxml import html
import multiprocessing
import time

# Try to crawl all the courses in 163course.

start_url_one = 'http://www.icourse163.org/'
start_url_two = 'http://www.icourse163.org/category/all'

course_url_list = []

headers = {
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'
}
#Headers is important

def get_all_course_urls(url，i)：
  if i >= 4:
    return None
  time.sleep(2)
  r = requests.get(url,headers = headers)

  tree = lxml.html.fromstring(r.content)

  urllist = tree.xpath('//a/@href')

  for item in urllist:
    if 'http://www.icourse163.org/course/' in item and item not in course_url_list:
      course_url_list.append(item)
    else:
      #If the url doesn't meet the form of course url, we should crawl inside to the url
      #It will be easier to do this by Scrapy, but we will make it by ourselves
      get_all_course_urls(item,i+1)

      
      
      
if __name__ == '__main__':
  p1 = multiprocessing.Process(target = get_all_course_urls,args=(start_url_one,1))
  p2 = multiprocessing.Process(target = get_all_course_urls,args=(start_url_two,1))
  p1.start()
  p2.start()

