from bs4 import BeautifulSoup


html_doc = """
<html>
<head><title>示例页面</title></head>
<body>
<p class="title"><b>示例标题</b></p>
<p class="story">这是一个示例段落...</p>
</body>
</html>
"""
import requests
response = requests.get('http://www.github.com')
# 创建BeautifulSoup对象(即DOM树)
soup = BeautifulSoup(response.text, 'html.parser')

# 访问元素
print(soup.title)  # <title>示例页面</title>
print(soup.title.string)  # 示例页面

# 查找所有p标签
# for p in soup.find_all('div'):
#     print(p.get_text())

#查找特定元素
link = soup.select('.flash-container >a')

print(link)
