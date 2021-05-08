import requests
import json
import pandas as pd
from requests.exceptions import ConnectionError

ProductCategoryList = []
ProductNameList = []
BrandNameList = []
ProductPriceList = []
MrpList = []
DiscountList = []
ManufacturerList = []
ProductImageList = []

headers = {'Connection':"keep-alive", 'accept':"application/json", 'DNT':'1', 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36', 'content-type':'application/x-www-form-urlencoded', 'Origin':'https://www.jiomart.com','Sec-Fetch-Site':'cross-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://www.jiomart.com/','Accept-Language':'en-US,en;q=0.9'}
params={'x-algolia-agent': 'Algolia for JavaScript (3.33.0); Browser; instantsearch.js (4.14.0); JS Helper (3.3.4)', 'x-algolia-application-id':'3YP0HP3WSH','x-algolia-api-key':'aace3f18430a49e185d2c1111602e4b1'}
data = {"requests":[{"indexName":"prod_mart_groceries_products_popularity","params":"maxValuesPerFacet=50&query=&filters=(available_stores%3A6210)%20AND%20(inventory_stores%3AALL%20OR%20inventory_stores%3A6210%20OR%20inventory_stores%3ATMW7%20)&clickAnalytics=true&highlightPreTag=_ais-highlight&highlightPostTag=%2Fais-highlight_&page=0&hitsPerPage=11370&facets=%5B%22in_stock%22%2C%22category_level.level4%22%2C%22brand%22%2C%22avg_selling_price%22%2C%22avg_discount_pct%22%5D&tagFilters="}]}


for i in range(1,1200):
    print(i)
    data = {"requests":[{"indexName":"prod_mart_groceries_products_popularity","params":"maxValuesPerFacet=50&query=&filters=manufacturer_id%3A'"+str(i)+"'%20AND%20(available_stores%3A6210)%20AND%20(inventory_stores%3AALL%20OR%20inventory_stores%3A6210%20OR%20inventory_stores%3ATMW7%20)&clickAnalytics=true&highlightPreTag=_ais-highlight&highlightPostTag=%2Fais-highlight_&page=0&hitsPerPage=1000&facets=%5B%22in_stock%22%2C%22category_level.level4%22%2C%22brand%22%2C%22avg_selling_price%22%2C%22avg_discount_pct%22%5D&tagFilters="}]}
    response = requests.post('https://3yp0hp3wsh-dsn.algolia.net/1/indexes/*/queries', params=params, headers=headers, json=data)
    json_data = response.json()
    products = (json_data["results"])[0]["hits"] 
    for i in products:
        try:
            ProductCategoryList.append((i["categories"])[3])
        except KeyError:
            ProductCategoryList.append("")
        except IndexError:
            ProductCategoryList.append((i["categories"])[2])
        try:
            ProductNameList.append(i["display_name"])
        except KeyError:
            ProductNameList.append("")
        try:
            BrandNameList.append(i["brand"])
        except KeyError:
            BrandNameList.append("")
        try:
            ProductPriceList.append(i["avg_selling_price"])
        except KeyError:
            ProductPriceList.append("")
        try:
            MrpList.append(i["avg_mrp"]) 
        except KeyError:
            MrpList.append("")   
        try:
            DiscountList.append(i["avg_discount_pct"])
        except KeyError:
            DiscountList.append("") 
        try:
            ManufacturerList.append(i["manufacturer_name"])
        except KeyError:
            ManufacturerList.append("")      
        try:
            ProductImageList.append("https://www.jiomart.com/" + (i["image_url"]))
        except KeyError:
            ProductImageList.append("")         




            
            
           
#    table_dict = {'name': ProductNameList, 'brand': BrandNameList, 'manufacturer': ManufacturerList, 'category': ProductCategoryList, 'sp': ProductPriceList, 'mrp': MrpList, 'discount': DiscountList, 'productImageUrl': ProductImageList}
#    df = pd.DataFrame(table_dict)

#    df.to_csv('jioProducts.csv',index=False)
#    df.to_json('jioProducts.json',orient='records')



table_dict = {'name': ProductNameList, 'brand': BrandNameList, 'manufacturer': ManufacturerList, 'category': ProductCategoryList, 'sp': ProductPriceList, 'mrp': MrpList, 'discount': DiscountList, 'productImageUrl': ProductImageList}
df = pd.DataFrame(table_dict)


df.to_csv('jioProducts1.csv',index=False)
df.to_json('jioProducts1.json',orient='records')
