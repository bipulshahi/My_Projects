import pickle
import json
import numpy as np

__data_columns = None
__model = None

def get_predicted_price(Item_Weight,Item_Visibility,Item_MRP,
                        Outlet_Identifier,Years,Item_Fat_Content,
                        Item_Type,Outlet_Size,Outlet_Location_Type,
                        Outlet_Type,New_Type):
    
    loc1 = __data_columns.index(Item_Fat_Content.lower())
    loc2 = __data_columns.index(Item_Type.lower())
    loc3 = __data_columns.index(Outlet_Size.lower())
    loc4 = __data_columns.index(Outlet_Location_Type.lower())
    loc5 = __data_columns.index(Outlet_Type.lower())
    loc6 = __data_columns.index(New_Type.lower())

    x = np.zeros(len(__data_columns))
    x[0] = Item_Weight
    x[1] = Item_Visibility
    x[2] = Item_MRP
    x[3] = Outlet_Identifier
    x[4] = Years

    x[loc1] = 1
    x[loc2] = 1
    x[loc3] = 1
    x[loc4] = 1
    x[loc5] = 1
    x[loc6] = 1

    return __model.predict([x])[0]


def load_saved_artifacts():
    global __data_columns

    print("reading locations file")
    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']

        global __model
        if __model is None:
            with open('./artifacts/sales_value.pickle', 'rb') as f:
                __model = pickle.load(f)
        print("loading saved artifacts...done")

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()

'''
    print(get_predicted_price(9.30,0.02,249.80,49,14,
                              'Low Fat','Dairy','Medium','Tier 1',
                              'Supermarket Type1','Food'))
'''

        
