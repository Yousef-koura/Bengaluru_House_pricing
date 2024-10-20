import json
import pickle

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
    with open("./server/Artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']  # Ensure 'data_columns' is correct
        __locations = __data_columns[4:]  # Assuming the first 3 columns are non-location-related

    # Load the trained model from pickle file
    with open("./server/Artifacts/banglore_home_price_model.pickle", "rb") as f:
        __model = pickle.load(f)

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
