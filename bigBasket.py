import requests
import json
import pandas as pd
from requests.exceptions import ConnectionError


ProductCategoryList = []
ProductNameList = []
BrandNameList = []
MrpList = []
SpList = []
ProductImageList = []
ProductDescList = []
WeightList = []

response = requests.get("https://www.bigbasket.com/product/get-products/?page=1&tab_type=[%22all%22]&sorted_on=popularity&listtype=pc")
json_data = response.json()
products = ((((json_data["tab_info"])[0])["product_info"])["products"])
for i in products:
    ProductCategoryList.append(i["llc_n"])
    ProductImageList.append(i["p_img_url"])
    ProductNameList.append(i["p_brand"]+" "+i["p_desc"]+", "+i["w"]+" "+i["pack_desc"])
    WeightList.append(i["w"])
    BrandNameList.append(i["p_brand"])
    MrpList.append(i["mrp"])
    SpList.append(i["sp"])
    ProductDescList.append(i["p_desc"])

try:
    for i in range(2,1532):
        print(i)
        response = requests.get("https://www.bigbasket.com/product/get-products/?page="+str(i)+"&tab_type=[%22all%22]&sorted_on=popularity&listtype=pc")
        json_data = response.json()
        products = ((((json_data["tab_info"])["product_map"])["all"])["prods"])
        for i in products:
            ProductCategoryList.append(i["llc_n"])
            ProductImageList.append(i["p_img_url"])
            ProductNameList.append(i["p_brand"]+" "+i["p_desc"]+", "+i["w"]+" "+i["pack_desc"])
            WeightList.append(i["w"])
            BrandNameList.append(i["p_brand"])
            MrpList.append(i["mrp"])
            SpList.append(i["sp"])
            ProductDescList.append(i["p_desc"])
except ConnectionError as e:
   print(i)
   table_dict = {'Product_Name': ProductNameList, 'Brand_Name': BrandNameList, 'Product_Category': ProductCategoryList, 'Product_Weight': WeightList, 'Product_MRP': MrpList, 'Product_SP': SpList, 'Product_Description': ProductDescList, 'Product_ImgURL': ProductImageList}
   df = pd.DataFrame(table_dict)

   df.to_csv('bigbasketProducts.csv',index=False)
   df.to_json('bigbasketProducts.json',orient='records')
   print (e)
   r = "No response"


table_dict = {'Product_Name': ProductNameList, 'Brand_Name': BrandNameList, 'Product_Category': ProductCategoryList, 'Product_Weight': WeightList, 'Product_MRP': MrpList, 'Product_SP': SpList, 'Product_Description': ProductDescList, 'Product_ImgURL': ProductImageList}
df = pd.DataFrame(table_dict)

df.to_csv('bigbasketProducts.csv',index=False)
df.to_json('bigbasketProducts.json',orient='records')
