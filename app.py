from flask import Flask, request, render_template, redirect
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

username = os.getenv("MONGO_USER")
password = os.getenv("MONGO_PASS")

uri = f"mongodb+srv://{username}:{password}@cluster0.szp99ew.mongodb.net/?appName=Cluster0"
client = MongoClient(uri)
db = client["data"]
collection = db["users"]

app = Flask(__name__)

@app.route("/", methods=["GET"] )
def form():
      return render_template("form.html")

@app.route("submittodoitem", methods=["POST"])
def submit():
     item_name=request.form.get("name")
     item_desc=request.form.get("desc")
     collection.insert_one({"name": item_name, 
                            "desc": item_desc})
    

if __name__ == "__main__":
    app.run(debug=True)