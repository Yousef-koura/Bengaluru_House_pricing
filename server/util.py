import json
import pickle
import pandas as pd
import numpy as np 


__locations = None
__data_columns = None
__model = None


def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts ....start")
    global __data_columns
    global __locations
    global __model

    # Load column names from JSON file
    __data_columns = json.load(open("./server/Artifacts/columns.json", 'r'))['data_columns']  
    # Slice locations from the data columns 
    __locations = __data_columns[4:]  
    # Load the trained model from pickle file
    __model = pickle.load(open("./server/Artifacts/Housing_model.pkl", "rb"))


# Define the prediction function
def predict_price(location, area_type, bath, balcony, bedrooms, total_sqft):
    # Get the index of the location in the data columns (if it exists)
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1  # If location is not found in columns, use -1 (will remain 0)

# Prepare the input data as an array with zeros for all columns
    x = np.zeros(len(__data_columns))  # Ensure the input array has the same length as data_columns
    
    # Set the appropriate values for the input columns
    x[0] = area_type  # Area Type (label encoded)
    x[1] = bath       # Number of bathrooms
    x[2] = balcony    # Number of balconies
    x[3] = bedrooms   # Number of bedrooms
    x[-2] = total_sqft  # Total square feet (should be the last column)
    if loc_index >= False:
        x[loc_index] = True

    return round(__model.predict([x])[0],2)

if __name__ == "__main__":
    load_saved_artifacts()
    predicted_price = predict_price('yelachenahalli', 1, 3, 2, 3, 1500)  # Use 0 for area_type as an example
    print(f"The predicted price is: {predicted_price}")
