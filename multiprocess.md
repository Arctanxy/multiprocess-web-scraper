# 多进程爬虫
---
通过多进程的方式实现爬虫提速

使用python中的multiprocessing模块

```
import multiprocessing

def run():
  print('Look, I'm running')
  
if __name__ == '__main__':
  p = multiprocessing.Process(target = run,args=(i,))
  p.start()
```

注意使用多进程爬虫时需要有一个调度函数，保证几个进程之间爬取数据不重复。（多线程同理）

下面是一个实例：采用多进程收集网易中国大学MOOC的所有课程
遵循深度优先的原则，深度设为4：
对首页中每个链接深入爬取四次，收集所有遇到的带有http://www.icourse163.org/course/ 字段的链接；
然后抓取课程信息。

广度优先：
从首页http://www.icourse163.org/ 出发

1. 打开首页中所有包含http://www.icourse163.org/course/ 字段的链接；
2. 打开首页中所有其他链接，搜集其中包含课程字段的链接，并打开其他链接，寻找包含课程字段的链接；
3. 如果一个页面连续深入打开两次都没有发现其他链接，则将该页加入黑名单；
4. 每发现一个课程网页都核对一下是不是打开过。
