#we need to import the libraries that we need
import requests
import sys
from bs4 import BeautifulSoup
import mysql.connector





#we need to make the python to know the persian language that we can use persian website
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')





#we need to connect to the mysql to add the data to mysql
print("Connecting to the database.......")
connection=mysql.connector.connect(
    user="root",host="127.0.0.1",password="13831349mM@#",database="commodity"
)
print("Connected to the database")




#now we need to create a cursur to insert something into the database or read it
mycursur=connection.cursor()





#we need to request to the webpage to find the car prices
result=requests.get('https://emalls.ir/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA_%DA%A9%D9%86%D8%B3%D9%88%D9%84-%D8%A8%D8%A7%D8%B2%DB%8C~Category~655')





#items we need from html file
'''
main title
subtitle
prd-price
'''





#we need to use beautiful soup to clear the html code
soup=BeautifulSoup(result.text,'html.parser')





#we need to find the (price) and then we need arttibutes like maintitle subtitle and prd-price
name_of_device=soup.find_all(r'a',attrs={'class':'maintitle'})
# subtitle_of_device=soup.find_all(r'a',attrs={'class':'subtitle'})
price_of_device=soup.find_all(r'div',attrs={'class':'prd-price'})







#then we need to create a list of the names and the prices
names=[]
prices=[]




#then we need to create a fro loop to read the data
for rows in name_of_device:
    names.append(rows.text)
for rows2 in price_of_device:
    prices.append(rows2.text)






#then we need a for to print the datas correctly and use the cursur to add the data to database
count=0
for rows3 in names:
    print(f"Name:{rows3}                                                               Price:{prices[count]}")
    mycursur.execute('INSERT INTO commodity_info VALUES(\'%s\',\'%s\')'%(rows3,prices[count]))
    connection.commit()
    count+=1
    if(count>len(prices)):
        break



#we need to close the connection now
connection.close()



#MAHDI NAJAFI:) FOLLOW MY GITHUB IF YOU WANT------>MAHDIrobo
