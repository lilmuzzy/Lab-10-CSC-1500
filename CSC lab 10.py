import csv
import json
sales_data=[]
list1=[[],[],[],[],[],[],[],[]]

with open('SalesJan2009.csv', "r") as csvfile:
    reader = csv.reader(csvfile)
    Transaction_date=dict()
    Product=dict()
    Price=dict()
    Payment_Type=dict()
    Name=dict()
    City=dict()
    State=dict()
    Country=dict()
    for line in reader:
        list1[0].append(line[0])
        list1[1].append(line[1])
        list1[2].append(line[2])
        list1[3].append(line[3])
        list1[4].append(line[4])
        list1[5].append(line[5])
        list1[6].append(line[6])
        list1[7].append(line[7])  
Transaction_date["Time"]=list1[0] 
Product["Product"]= list1[1] 
Price["Price"]= list1[2]
Payment_Type["Payment_Type"]= list1[3]  
Name["Name"]= list1[4]
City["City"]= list1[5]
State["State"]= list1[6]
Country["Country"]= list1[7]
sales_data.append(Transaction_date)
sales_data.append(Product)
sales_data.append(Price)
sales_data.append(Payment_Type)
sales_data.append(Name)
sales_data.append(City)
sales_data.append(State)
sales_data.append(Country)

with open('transaction_data.json', 'w') as jsonfile:
    json.dump(sales_data, jsonfile)
    