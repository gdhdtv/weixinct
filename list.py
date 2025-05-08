from bs4 import BeautifulSoup

# 读取本地HTML文件内容
with open('response.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(html_content, 'html.parser')

# 假设新闻列表在一个具有特定类名的div中，且每条新闻都在一个li元素中
news_list_container = soup.select('.publish_hover_content')
if news_list_container:
    news_items = news_list_container.find_all('li', class_='news-item')
    
    for item in news_items:
        # 提取标题、发布时间、阅读人数、点赞人数、转发人数、推荐人数和文章链接
        title = item.find('h2').text if item.find('h2') else 'N/A'
        publish_time = item.find('span', class_='publish-time').text if item.find('span', class_='publish-time') else 'N/A'
        read_count = item.find('span', class_='read-count').text if item.find('span', class_='read-count') else '0'
        like_count = item.find('span', class_='like-count').text if item.find('span', class_='like-count') else '0'
        share_count = item.find('span', class_='share-count').text if item.find('span', class_='share-count') else '0'
        recommend_count = item.find('span', class_='recommend-count').text if item.find('span', class_='recommend-count') else '0'
        article_link = item.find('a')['href'] if item.find('a') else 'N/A'
        
        # 打印提取的信息
        print(f"标题: {title}")
        print(f"发布时间: {publish_time}")
        print(f"阅读人数: {read_count}")
        print(f"点赞人数: {like_count}")
        print(f"转发人数: {share_count}")
        print(f"推荐人数: {recommend_count}")
        print(f"文章链接: {article_link}")
        print('---')
else:
    print("未找到新闻列表容器。")