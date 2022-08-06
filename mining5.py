from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from write import wrtite


# 设置selenium使用chrome的无头模式
chrome_options = Options()
# 在启动浏览器时加入配置
browser = webdriver.Chrome(options=chrome_options)
def miningBook(host,url):
    host = host
    driver = browser.get(host + url)
    browser.implicitly_wait(10)
    html = browser.page_source.encode("gbk", "ignore")
    return html
def wash(htmlText):
    chapterSoup= BeautifulSoup(htmlText, 'html.parser')
    contents = chapterSoup.find('div', id='content')
    nextHref=chapterSoup.select('.bottem1 > a')[3]["href"]
    title=chapterSoup.select(".bookname > h1")[0].text
    if chapterSoup.select('.bottem1 > a')[3].text !="没有了":
        stopFlag = True
    else:
        stopFlag = False
    strContent=""
    for content in contents:
        # strContent=strContent+content.text+"\n"
        strContent=strContent+content.text
    returnList = []
    returnList.append(title)
    returnList.append(strContent)
    returnList.append(nextHref)
    returnList.append(stopFlag)
    return returnList
bookName="我爹是袁术？可我想当曹贼 "
bookStr=""
bookStr = bookStr + bookName + str("作者：    我辈皆曹贼")+"\r\n"
returnList=wash(miningBook("http://www.cits0871.com","/booktxt/50902/28955213.html"))
bookStr = bookStr +"###"+returnList[0]
bookStr=bookStr+returnList[1]

while returnList[3]:
    returnList = wash(miningBook("http://www.cits0871.com", returnList[2]))
    bookStr = bookStr +"###"+returnList[0]
    bookStr = bookStr + returnList[1]
wrtite.write(bookName, bookStr)
browser.quit()
print("已经爬完了~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")