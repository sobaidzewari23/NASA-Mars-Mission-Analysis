# Import Dependencies 
from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_mars
import os


# Hidden authetication file
#import config 

# from flask import Flask
# from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

# Create an instance of Flask app
# app = Flask(__name__)

#Use flask_pymongo to set up connection through mLab
# app.config["MONGO_URI"] = os.environ.get('authentication')
# mongo = PyMongo(app)



# Use flask_pymongo to set up mongo connection locally 
# app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
# mongo = PyMongo(app)

# Create route that renders index.html template and finds documents from mongo
@app.route("/")
def home(): 

    # Find data
    mars_info = mongo.db.mars_info.find_one()

    # Return template and data
    return render_template("index.html", mars_info=mars_info)

# Route that will trigger scrape function
@app.route("/scrape")
def scrape(): 

    # Run scrapped functions
    mars_info = mongo.db.mars_info
    mars_data = {}
    mars_data["news"] = scrape_mars.scrape_mars_news()
    mars_data["image"] = scrape_mars.scrape_mars_image()
    mars_data["facts"] = scrape_mars.scrape_mars_facts()
    mars_data["weather"] = scrape_mars.scrape_mars_weather()
    mars_data["hemispheres"] = scrape_mars.scrape_mars_hemispheres()
    mars_info.update({}, mars_data, upsert=True)

    return redirect("/", code=302)

if __name__ == "__main__": 
    app.run()
