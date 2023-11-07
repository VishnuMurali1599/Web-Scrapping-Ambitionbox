from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

app = Flask(__name__)

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/review',methods=['POST','GET']) # route to show the review comments in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
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
            for page in range(1,10):
                headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
                url=f"https://www.ambitionbox.com/list-of-companies?page={page}"
                webpage=requests.get(url,headers=headers).text
                soup=bs(webpage,'html.parser')
                
                reviews=[]
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
                
                mydict={"Company_Name":Company_Name,"Ratings":Ratings,"Company_Type":Company_type,"Total_Employees":Total_Employee,"Sector":Sector,"Total_Years":Total_Years,"Head_Quaters":Head_Quaters,"Total_Review_Count":Total_Review_Count,"Avg_salaries":Avg_Salaries,"Avg_Interview":Avg_interview,"Avg_Jobs":Avg_Jobs,"Benifits":Benifits}
                reviews.append(mydict)
            
            return render_template('results.html', reviews=reviews[0:(len(reviews)-1)])
    
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
            # return render_template('results.html')

    else:
        return render_template('index.html')

if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True)
