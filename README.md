# maoyanpiaofang
抓取猫眼票房的实时数据





代码写得很简单。之前很傻很天真的尝试用urllib2来获取网页的源码，可是没什么发现解析到的源码有乱码，根本就不能用beautifulsoup抓取，后来在知乎上问，有一知友告诉我这个网页用到了JavaScript，所以需要模拟post。我不懂他说什么。但后来一次机缘巧合，看了油管上一个利用get抓取网页信息的视频，很受鼓舞，赶紧用requests库重新试试，结果真的可以抓取到数据了。



所需第三方模块：
 requests，安装方式（用pip):  
  pip install requests

 beautifulsoup, 安装方式（用pip）：
  pip install BeautifulSoup4

运行方式：在有运行功能上的代码编辑器上运行。如我使用的PyCharm，当然，也可以使用python原生的ide运行。


仍待完善的地方：
1、如何让抓取到的各种数据，如片名、实时票房、总票房、排片占比等数据在展示时可以对齐？不会像现在这么乱。
2、希望可以用弹窗的方式来显示这些数据。
