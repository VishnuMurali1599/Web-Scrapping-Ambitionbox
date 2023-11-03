import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import numpy as np
import mysql.connector as connection

Company_Name=[]
Total_Review_Count=[]
Ratings=[]
Avg_Salaries=[]
Avg_interview=[]
Avg_Jobs=[]
Benifits=[]
Company_type=[]
Total_Employee=[]
Sector=[]
Total_Years=[]
Head_Quaters=[]


for page in range(1,11):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
    url=f"https://www.ambitionbox.com/list-of-companies?page={page}"
    webpage=requests.get(url,headers=headers).text
    soup=bs(webpage,'html.parser')
    for i in range(20):
        try:
            Company_Name.append(soup.find_all("h2")[i].text.replace('\n','').replace('\t',''))
        except:
            Company_Name.append('N/A')
            
            
        try:
            Ratings.append(soup.find('span',class_="companyCardWrapper__companyRatingValue").text.strip())
        except:
            Ratings.append("N/A")
            
            
        try:
            Details=soup.find_all('div',{'class':'companyCardWrapper__tertiaryInformation'})[i].text
            Total_Review_Count.append(Details.replace(',','').replace('Reviews','Reviews, ').replace('Salaries','Salaries, ').replace('Interviews','Interviews, ').replace('Jobs',' Jobs, ').replace('Benefits',' Benefits, ').replace('k','k').replace(' Photos', ' photos').split(",")[0])
        except:
            Total_Review_Count.append("N/A")
            
        try:
            Details=soup.find_all('div',{'class':'companyCardWrapper__tertiaryInformation'})[i].text
            Avg_Salaries.append(Details.replace(',','').replace('Reviews','Reviews, ').replace('Salaries','Salaries, ').replace('Interviews','Interviews, ').replace('Jobs',' Jobs, ').replace('Benefits',' Benefits, ').replace('k','k').replace(' Photos', ' photos').split(",")[1])
            #print(Avg_Salaries)
        except:
            #pass
            Avg_Salaries.append("N/A")
            
        try:
            Details=soup.find_all('div',{'class':'companyCardWrapper__tertiaryInformation'})[i].text
            Avg_interview.append(Details.replace(',','').replace('Reviews','Reviews, ').replace('Salaries','Salaries, ').replace('Interviews','Interviews, ').replace('Jobs',' Jobs, ').replace('Benefits',' Benefits, ').replace('k','k').replace(' Photos', ' photos').split(",")[2])
        except:
            #pass
            Avg_interview.append("N/A") 
            
        try:
            Details=soup.find_all('div',{'class':'companyCardWrapper__tertiaryInformation'})[i].text
            Avg_Jobs.append(Details.replace(',','').replace('Reviews','Reviews, ').replace('Salaries','Salaries, ').replace('Interviews','Interviews, ').replace('Jobs',' Jobs, ').replace('Benefits',' Benefits, ').replace('k','k').replace(' Photos', ' photos').split(",")[3])
        except:
            #pass
            Avg_Jobs.append("N/A") 
            
        try:
            Details=soup.find_all('div',{'class':'companyCardWrapper__tertiaryInformation'})[i].text
            Benifits.append(Details.replace(',','').replace('Reviews','Reviews, ').replace('Salaries','Salaries, ').replace('Interviews','Interviews, ').replace('Jobs',' Jobs, ').replace('Benefits',' Benefits, ').replace('k','k').replace(' Photos', ' photos').split(",")[4])
        except:
            #pass
            Benifits.append("N/A") 
            
        try:
            add_details=soup.find_all('span',{'class':'companyCardWrapper__interLinking'})[i]
            Company_type.append(add_details.text.strip().split('|')[0])
        except:
            Company_type.append("N/A")
            
        try:
            add_details=soup.find_all('span',{'class':'companyCardWrapper__interLinking'})[i]
            Total_Employee.append(add_details.text.strip().split('|')[1])
        except:
            Total_Employee.append("N/A")
            
        try:
            add_details=soup.find_all('span',{'class':'companyCardWrapper__interLinking'})[i]
            Sector.append(add_details.text.strip().split('|')[2])
        except:
            Sector.append("N/A")
            
        try:
            add_details=soup.find_all('span',{'class':'companyCardWrapper__interLinking'})[i]
            Total_Years.append(add_details.text.strip().split('|')[3])
        except:
            #pass
            Total_Years.append("N/A")
            
        try:
            add_details=soup.find_all('span',{'class':'companyCardWrapper__interLinking'})[i]
            Head_Quaters.append(add_details.text.strip().split('|')[4])
        except:
            #pass
            Head_Quaters.append("N/A")
                
d={"Company_Name":Company_Name,"Ratings":Ratings,"Company_Type":Company_type,"Total_Employees":Total_Employee,"Sector":Sector,"Total_Years":Total_Years,"Head_Quaters":Head_Quaters,"Total_Review_Count":Total_Review_Count,"Avg_salaries":Avg_Salaries,"Avg_Interview":Avg_interview,"Avg_Jobs":Avg_Jobs,"Benifits":Benifits}
df=pd.DataFrame(d)
df.to_csv("details.csv")
print(df)


##-------------------------- Connecting To My SQL -----------------------------------

#mydb=connection.connect(host="localhost", user="root", passwd="Vishnu@1234567890")
#print(mydb)
#cursor=mydb.cursor()
#print(cursor)

#cursor.execute("show databases")

#cursor.execute("create database Company_Details")

#cursor.execute("create table if not exists company_details.review (company_name varchar(50),Ratings float,company_type varchar(50),Total_Employees varchar(30),Sector varchar(30),Total_Years varchar(30),Head_Quaters varchar(30),Total_Review_Count varchar(30),Avg_Salaries varchar(30),Avg_interview varchar(30),Avg_Jobs varchar(30),Benifits varchar(30))")
#cursor.execute("select * from company_details.review ")
#for i in cursor.fetchall():
    #print(i)

