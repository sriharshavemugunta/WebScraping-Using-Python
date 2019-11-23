import requests#library for handling the interaction with the web page
import pandas as pd
from bs4 import BeautifulSoup #library for handling the text extraction from the web page’s source code (HTML and CSS)
url = "https://www.snapdeal.com/products/mobiles-mobile-phones/filters/Form_s~Smartphones?sort=plrty"
response = requests.get(url)
print(response)
data = BeautifulSoup(response.text,"html.parser")
mobiles_data = data.find_all("div", class_="product-tuple-listing")
d = []
for info  in  mobiles_data:
  title = info.find('p', class_="product-title").text
  actual_price = info.find('span',class_="product-desc-price").text
  discount_price = info.find('span',class_="product-price").text

  if( info.find('div',class_="product-discount")):
    discount_percentage = info.find('div', class_="product-discount").text
  else:
    discount_percentage = ""

  if (info.find('p', class_="product-rating-count")):
    rating_count = info.find('p', class_="product-rating-count").text
  else:
    rating_count = ""

  url_class = info.find("div", class_="product-tuple-image")
  url = url_class.find("a").attrs['href']
  d.append({'Mobile':title,'Actual Price':actual_price,'Discount Price':discount_price,"Discount Percentage":discount_percentage,"Rating Count":rating_count,'url':url,})
  final_data = pd.DataFrame(d)
  print (final_data)