import pymongo
import os
from solution_start import *

client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mydb=client['customer_product_data']
datainfo=mydb.customer_data

cwd = os.getcwd()
cwd_need = cwd.split("solution")[0]


transaction_path = cwd_need + 'input_data/starter/transactions'
customer_path = cwd_need + 'input_data/starter/customers.csv'
product_path = cwd_need + 'input_data/starter/products.csv'
# output_path = cwd_need + 'output_data/outputs/'

x = customer_product_data(transaction_path,customer_path,product_path)
garnd_data = x.create_json()



for j in garnd_data:
	if j != None:
		datainfo.insert_one(j)



print("....................insert successfully complete.........................")