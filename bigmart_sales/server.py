from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_columns', methods=['GET'])
def get_columns():
    response = jsonify({'columns': util.get_data_columns()})

    return response


@app.route('/predict_sales_price', methods=['POST'])
def predict_sales_price():
    Item_Weight = float(request.form['item_weight'])
    Item_Visibility = float(request.form['item_visibility'])
    Item_MRP = float(request.form['item_MRP'])
    Outlet_Identifier = float(request.form['outlet_identifier'])
    Years = float(request.form['years'])
    Item_Fat_Content = request.form['item_fat_content']
    Item_Type = request.form['item_type']
    Outlet_Size = request.form['outlet_size']
    Outlet_Location_Type = request.form['outlet_location_type']
    Outlet_Type = request.form['outlet_type']
    New_Type = request.form['new_type']

    response = jsonify({"estimated_sales": util.get_predicted_price(Item_Weight,
                                                                    Item_Visibility,
                                                                    Item_MRP,
                                                                    Outlet_Identifier,Years,
                                                                    Item_Fat_Content,
                                                                    Item_Type,Outlet_Size,
                                                                    Outlet_Location_Type,
                                                                    Outlet_Type,New_Type)})
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Sales Value Prediction...")
    util.load_saved_artifacts()
    app.run()
