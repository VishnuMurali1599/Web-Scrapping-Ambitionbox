from flask import Flask,render_template,request,jsonify
from flask_cors import CORS,cross_origin
import requests
from pymongo.mongo_client import MongoClient
import json

app=Flask(__name__)

@app.route('/',methods=['GET']) 
@cross_origin()
def homepage():
    return render_template("index.html")

@app.route("/Submit",methods=['POST','GET'])
@cross_origin()
def index():
    if request.method=="POST":
        reviews=[]
        from pymongo.mongo_client import MongoClient
        import json
        uri ="mongodb+srv://vishnumurali835:Vishnu8748803252@vishnumurali.gan12f1.mongodb.net/?retryWrites=true&w=majority"

        # Create a new client and connect to the server
        client = MongoClient(uri)
        database=client['Database']
        collection=database['Company_review']
        
        search_string=request.form['companyName']
        query = {"Company_Name":search_string}
        for i in collection.find(query):
            reviews.append(i)
            
            return render_template('results.html',reviews=reviews[0:(len(reviews)-1)])
    
    else:
        return "Something wrong"



if __name__=="__main__":
    app.run(debug=True)