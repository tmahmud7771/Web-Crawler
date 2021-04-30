import re,requests 
url = "https://books.toscrape.com/index.html"
response = requests.get(url)

# to check response is ok or not type print(response.ok) if True its ok else not 
# print(response.ok)

text = response.text

#to check the lenght
# print(len(text))

# result = re.findall(r'<div class="side_categories">(.*?)</div>',text,re.M | re.DOTALL)
#to check the what is the result 
# print(result)


category_path = re.compile(r'<li>\s*<a href=".*?)">(.*?)<', re.M | re.DOTALL)

result = category_path.findall(text)
arr = []
for item in result:
    print(item[0])