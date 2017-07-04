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

下面是一个实例：采用多进程收集一个贴吧的所有帖子

