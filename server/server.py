
from flask import Flask,request,jsonify
import pickle
import util


app = Flask(__name__)


@app.route("/get_location_names")
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')

    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bedrooms = int(request.form['bedrooms'])
    bath = int(request.form['bath'])
    balcony = int(request.form['balcony'])
    area_type = int(request.form['area_type'])
    
    response = jsonify({
        'estimated_price':util.predict_price(location, area_type, bath, balcony, bedrooms, total_sqft)
    })

    response.headers.add('Access-Control-Allow-Origin','*')

    return response 

if __name__ == "__main__":
    print("Starting Python Flask Server for Home Prediction")
    util.load_saved_artifacts()
    app.run()