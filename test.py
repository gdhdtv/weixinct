# 启动 Playwright
from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import openpyxl
from openpyxl import Workbook

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
page = browser.new_page()

# 导航到一个页面
page.goto("https://mp.weixin.qq.com/")
print("当前页面标题:", page.title())


# 获取输入框并输入邮箱地址
# email_input = page.query_selector('.weui-desktop-form__input[placeholder="邮箱/微信号"]')
# if email_input:
#     email_input.fill('')

# 获取密码框并输入密码
# password_input = page.query_selector('.weui-desktop-form__input[placeholder="密码"]')
# if password_input:
#     password_input.fill('')

# 获取登录按钮并点击
# login_button = page.query_selector('.btn_login')
# if login_button:
#     login_button.click()

#等待1分钟import time
time.sleep(120)


 # 获得发表记录并点击
 #weui-desktop-menu__name
""" publish_menu_link = page.query_selector('.weui-desktop-menu__link a[title="内容管理"]')
if publish_menu_link :
    publish_menu_link .click()

publish_record_link = page.query_selector('.weui-desktop-sub-menu__item a[title="发表记录"]')
if publish_record_link:
    publish_record_link.click() """


#添加功能，把数据写入到Excel中

wb = Workbook()
ws = wb.active
ws.append(['标题', '阅读人数', '点赞人数', '转发人数', '推荐人数', '留言人数', '发布时间','文章链接',])




#获取当前网址，翻页
page.wait_for_load_state("networkidle") 
#man_url=page.url
man_url=page.evaluate("window.location.href")
for i in range(0, 430, 10):
    new_url = man_url.replace('begin=0', f'begin={i}')
    print(new_url)
    page.goto(new_url)
    time.sleep(10)

    # 获取HTML内容，选择器中的内容。
    content = page.inner_html('div.publish_content.publish_record_history')
    # 使用BeautifulSoup 获取新闻列表，并获取每条消息的数据。包括标题、发布时间、阅读人数、点赞人数、转发人数、推荐人数、文章链接。


    soup = BeautifulSoup(content, 'html.parser')
    news_list_container = soup.select('.publish_hover_content')

    for item in news_list_container:
        title=item.select('a')[0].text # 获取标题
        t1=item.select('.weui-desktop-mass-media__data__inner')[0].text # 阅读人数
        t2=item.select('.weui-desktop-mass-media__data__inner')[1].text # 点赞人数
        t3=item.select('.weui-desktop-mass-media__data__inner')[2].text # 转发人数
        t4=item.select('.weui-desktop-mass-media__data__inner')[3].text # 推荐人数
        t5=item.select('.weui-desktop-mass-media__data__inner')[4].text # 留言人数
        t6=item.select('a')[0].get('href') # 获得文章链接
        
        d1=item.select('.weui-desktop-mass__time') #发布时间
        if d1:
            #print(d1[0].text)
            d1s=d1[0].text
            d1=d1[0].text
        else:
            d1=d1s

        print(title,t1,t2,t3,t4,t5,t6,d1)
        #将数据写入表格
        ws.append([title,t1, t2, t3, t4, t5, t6, d1])


# 保存工作簿到文件
wb.save('data.xlsx')
# 关闭浏览器
browser.close()
playwright.stop()

