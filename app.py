import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import numpy as np


#final=pd.DataFrame()
for page in range(0,10):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
    url=f"https://www.ambitionbox.com/list-of-companies?page={page}"
    webpage=requests.get(url,headers=headers).text
    soup=bs(webpage,'html.parser')
      
    Company_Name=[]
    Ratings=[]    
    Company_Type=[]
    Total_Employees=[]
    Sector=[]
    Total_Years=[]
    Head_Quaters=[]
    Total_Review_Count=[]
    Avg_Salaries=[]
    Avg_interview=[]
    Avg_Jobs=[]
    Benifits=[]
    
    for k in range(len(soup.find_all('span',class_='companyCardWrapper__companyRatingValue'))):
        big_container=soup.find_all("div",{"class":"companyListing__cardsContainer"})
        for i in big_container:
            
            try:
                Company_Name.append(i.find_all("h2")[k].text.replace('\n','').replace('\t',''))
            except:
                Company_Name.append(np.nan)
                
                
            try:
                Ratings.append(i.find_all('span',class_='companyCardWrapper__companyRatingValue')[k].text)
            except:
                Ratings.append(np.nan)
            
            try:
                Company_Type.append(i.find_all("span",{'class':"companyCardWrapper__interLinking"})[k].text.strip().split("|")[0])
            except:
                Company_Name.append(np.nan)
                
            try:
                Total_Employees.append(i.find_all("span",{'class':"companyCardWrapper__interLinking"})[k].text.strip().split("|")[1])
            except:
                Total_Employees.append(np.nan)
                
            try:
                Sector.append(i.find_all("span",{'class':"companyCardWrapper__interLinking"})[k].text.strip().split("|")[2])
            except:
                Sector.append(np.nan)
            
            try:
                Total_Years.append(i.find_all("span",{'class':"companyCardWrapper__interLinking"})[k].text.strip().split("|")[3])
            except:
                Total_Years.append(np.nan)
                
                
            #Head_Quaters.append(i.find_all("span",{'class':"companyCardWrapper__interLinking"})[k].text.strip().split("|")[4])
        

            try:
                original_statement=soup.find_all("div",{'class':"companyCardWrapper__tertiaryInformation"})[k].text
        
                transformed_statement = ''.join([f',{char}' if char.isupper() and index > 0 else char for index, char in enumerate(original_statement)])
        
                Total_Review_Count.append(transformed_statement.replace(',','').replace('Reviews','Reviews, ').replace('Salaries','Salaries, ').replace('Interviews','Interviews, ').replace('Jobs',' Jobs, ').replace('Benefits',' Benefits, ').replace('k','k').replace(' Photos', ' photos').split(",")[0])
        
            except:
                Total_Review_Count.append(np.nan)
                
            
            try:
                original_statement=soup.find_all("div",{'class':"companyCardWrapper__tertiaryInformation"})[k].text
        
                transformed_statement = ''.join([f',{char}' if char.isupper() and index > 0 else char for index, char in enumerate(original_statement)])
        
                Avg_Salaries.append(transformed_statement.replace(',','').replace('Reviews','Reviews, ').replace('Salaries','Salaries, ').replace('Interviews','Interviews, ').replace('Jobs',' Jobs, ').replace('Benefits',' Benefits, ').replace('k','k').replace(' Photos', ' photos').split(",")[1])
        
            except:
                Avg_Salaries.append(np.nan)
                
                
            try:
                original_statement=soup.find_all("div",{'class':"companyCardWrapper__tertiaryInformation"})[k].text
        
                transformed_statement = ''.join([f',{char}' if char.isupper() and index > 0 else char for index, char in enumerate(original_statement)])
        
                Avg_interview.append(transformed_statement.replace(',','').replace('Reviews','Reviews, ').replace('Salaries','Salaries, ').replace('Interviews','Interviews, ').replace('Jobs',' Jobs, ').replace('Benefits',' Benefits, ').replace('k','k').replace(' Photos', ' photos').split(",")[2])
        
            except:
                Avg_interview.append(np.nan)
                
            
            try:
                original_statement=soup.find_all("div",{'class':"companyCardWrapper__tertiaryInformation"})[k].text
        
                transformed_statement = ''.join([f',{char}' if char.isupper() and index > 0 else char for index, char in enumerate(original_statement)])
        
                Avg_Jobs.append(transformed_statement.replace(',','').replace('Reviews','Reviews, ').replace('Salaries','Salaries, ').replace('Interviews','Interviews, ').replace('Jobs',' Jobs, ').replace('Benefits',' Benefits, ').replace('k','k').replace(' Photos', ' photos').split(",")[3])
        
            except:
                Avg_Jobs.append(np.nan)
                
                
            try:
                original_statement=soup.find_all("div",{'class':"companyCardWrapper__tertiaryInformation"})[k].text
        
                transformed_statement = ''.join([f',{char}' if char.isupper() and index > 0 else char for index, char in enumerate(original_statement)])
        
                Benifits.append(transformed_statement.replace(',','').replace('Reviews','Reviews, ').replace('Salaries','Salaries, ').replace('Interviews','Interviews, ').replace('Jobs',' Jobs, ').replace('Benefits',' Benefits, ').replace('k','k').replace(' Photos', ' photos').split(",")[4])
        
            except:
                Benifits.append(np.nan)
                
    #d={"Company_Name":Company_Name,"Ratings":Ratings,"Company_Type":Company_Type,"Total_Employees":Total_Employees,"Sector":Sector,"Total_Years":Total_Years,"Head_Quaters":Head_Quaters,"Total_Review_Count":Total_Review_Count,"Avg_salaries":Avg_Salaries,"Avg_Interview":Avg_interview,"Avg_Jobs":Avg_Jobs,"Benifits":Benifits}
    df=pd.DataFrame({"Company_Name":Company_Name,"Ratings":Ratings,"Company_Type":Company_Type,"Total_Employee":Total_Employees,"Sector":Sector,"Total_years":Total_Years,"Total_Review_count":Total_Review_Count,"Avg_salaries":Avg_Salaries,"Avg_Interview":Avg_interview,"Avg_Jobs":Avg_Jobs,"Benifits":Benifits})
    print(df)

