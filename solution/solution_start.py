
import pandas as pd 
import glob
import os
import json


cwd = os.getcwd()

cwd_need = cwd.split("solution")[0]



transaction_path = cwd_need + 'input_data/starter/transactions'
customer_path = cwd_need + 'input_data/starter/customers.csv'
product_path = cwd_need + 'input_data/starter/products.csv'



class customer_product_data:
    def __init__(self, transaction_path,customer_path,product_path):
        self.transaction_path = transaction_path         
        self.customer_path = customer_path
        self.product_path = product_path



    def loyalty_score_by_customer_id(self, customer_id):
        customer_df = pd.read_csv(self.customer_path)
        index_val = (customer_df[customer_df['customer_id'] == str(customer_id)].index.values)[0]
        loyalty_score = customer_df['loyalty_score'].iloc[index_val]

        return loyalty_score


    # print(loyalty_score_by_customer_id('C34',customer_path))



    def product_category_by_product_id(self, product_id):
        product_df = pd.read_csv(self.product_path)
        index_val = (product_df[product_df['product_id'] == str(product_id)].index.values)[0]
        product_category = product_df['product_category'].iloc[index_val]

        return product_category


    def create_json(self):


        all_files = os.listdir(self.transaction_path)
        garnd_data=[]

        for file in all_files:
            json_file_dir = f"{transaction_path}/{file}/transactions.json"

            with open(json_file_dir,'r') as file:
                data = file.readlines()
                # print(data)
                for each_data in data:
                    each_data = each_data[:-2] + "}"
                    # print(each_data)

                    each_data = eval(each_data)

                    customer_id = each_data['customer_id']
                    loyalty_score = self.loyalty_score_by_customer_id(customer_id)
                    date_of_purchase = each_data['date_of_purchase']
                    basket = each_data['basket']
                    for each_product in basket:
                        product_id = each_product['product_id']
                        product_category = self.product_category_by_product_id(product_id)


                        result = {"customer_id":customer_id,"loyalty_score":str(loyalty_score),"product_id":product_id,"product_category":product_category}
                        garnd_data.append(result)




        return garnd_data
   



x = customer_product_data(transaction_path,customer_path,product_path)
garnd_data = x.create_json()
 

out_df = pd.DataFrame(garnd_data)
out_df.to_csv(cwd_need + "customer_product_data.csv")



        