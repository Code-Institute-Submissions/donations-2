from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json
import os

app = Flask(__name__)

# MONGODB_HOST = 'localhost'
# MONGODB_PORT = 27017
MONGODB_URI = os.getenv('MONGODB_URI')
MONGODB_HOST = 'ds139187'
MONGODB_PORT = 39187
DBS_NAME = 'heroku_pxh82b97'

# DBS_NAME = 'donorsUSA'
# COLLECTION_NAME = 'projects'
#DBS_NAME = os.getenv('MONGO_DB_NAME','donorsUSA')
COLLECTION_NAME = 'projects'
FIELDS = {'funding_status': True, 'school_state': True, 'resource_type': True, 'poverty_level': True,
          'date_posted': True, 'total_donations': True,'primary_focus_area': True,'primary_focus_subject': True,'grade_level': True, '_id': False}


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup.html")
def sign():
    return render_template("signup.html")

@app.route("/register.html")
def register():
    return render_template("register.html")



@app.route("/donorsUS/projects")
def donor_projects():
    # connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    connection = MongoClient(MONGODB_URI)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    projects = collection.find(projection=FIELDS, limit=55000)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects)
    connection.close()
    return json_projects


if __name__ == "__main__":
    app.run(debug=True)