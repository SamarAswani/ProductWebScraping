import requests
import json
import pandas as pd
from requests.exceptions import ConnectionError

ProductCategoryList = []
ProductNameList = []
BrandNameList = []
ProductPriceList = []
MrpList = []
ProductImageList = []
LargeProductImageList = []
ProductDescList = []
WeightList = []
WeightUnitType = []
ProductType = []
DiscountList = []

# categories = ["16","1487","163","18","1878","13","12","14","1616","15","1379","1788","5","7","1047","1710","1879"]
categories = ["916", "1010", "1161", "1160", "917", "1158", "929", "933", "776", "1871", "695", "979", "691", "690", "722", "1115", "1117", "723", "692", "693", "1784", "983", "1084", "986", "1833", "926", "1075", "1048", "1085", "1082", "1053", "1050", "1052", "1051", "727", "1880", "944", "935", "942", "940", "1319", "1930", "1102", "955", "957", "960", "1599", "1184", "922", "953", "951", "954", "1004", "1137", "1125", "974", "962", "965", "968", "1126", "970", "1127", "1380", "1382", "1385", "1384", "1433", "1383", "1445", "1793", "1794", "1800", "1796", "1797", "1795", "1590", "1000", "1001", "1002", "305", "1014", "1276", "1187", "1387", "1049", "1841", "1896", "1893", "1886"]
headers = {'auth_key':"14a9ce3454854337dc7128d725648d97b731052516ff52a4da7af921d1183037", 'user-agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}

try:
    for cat in categories:
        response = requests.get('https://grofers.com/v4/search/merchants/27316/products/?l1_cat='+cat+'&start=0&next=48', headers=headers)
        json_data = response.json()
        products = (json_data["result"])["products"]
        for i in products:
            if (i["brand"] == "G Fresh") or ((i["brand"])[:7] == "Grofers"):
                continue
            else:
                ProductCategoryList.append(((i["categories"])[0])["name"])
                ProductImageList.append(i["image_url"])
                ProductNameList.append(i["name"])
                WeightList.append(i["unit"])
                WeightUnitType.append(i["unit_type"])
                BrandNameList.append(i["brand"])
                ProductPriceList.append(i["price"])
                MrpList.append(i["mrp"])
                ProductDescList.append(i["description"])
                LargeProductImageList.append(i["large_image_url"])
                ProductType.append(i["type"])
                DiscountList.append(i["discount"])

except ConnectionError as e:
   print(cat)
   print(i)
   table_dict = {'name': ProductNameList, 'brand': BrandNameList, 'category': ProductCategoryList, 'sp': ProductPriceList, 'mrp': MrpList, 'discount': DiscountList, 'type': ProductType, 'weight': WeightList, 'weightUnitType': WeightUnitType, 'description': ProductDescList, 'productImageUrl': ProductImageList, 'largeImageUrl': LargeProductImageList}
   df = pd.DataFrame(table_dict)

   df.to_csv('grocersProducts.csv',index=False)
   df.to_json('grocersProducts.json',orient='records')
   print (e)
   r = "No response"


table_dict = {'name': ProductNameList, 'brand': BrandNameList, 'category': ProductCategoryList, 'sp': ProductPriceList, 'mrp': MrpList, 'discount': DiscountList, 'type': ProductType, 'weight': WeightList, 'weightUnitType': WeightUnitType, 'description': ProductDescList, 'productImageUrl': ProductImageList, 'largeImageUrl': LargeProductImageList}
df = pd.DataFrame(table_dict)


df.to_csv('GrofersNew.csv',index=False)
df.to_json('GrofersNew.json',orient='records')
