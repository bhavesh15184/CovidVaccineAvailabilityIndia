import flask
import json
import prettytable
from flask import request
from prettytable import from_csv
from SlotDetails import SlotDetails
from cowin import getAvailibilityForRangePinCodes, writeSlotsToCSV, getPinCodes

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "Welcome!!"

@app.route('/availibility', methods=['GET'])
def availibility():
    INPUT_PINCODE_FILE = 'pincodes.csv'
    age = 37
    days = 7 

    if 'pincode_file' in request.args:
        INPUT_PINCODE_FILE = request.args['pincode_file']    
    if 'age' in request.args:
        age = int(request.args['age'])
    if 'days' in request.args:
        days = int(request.args['days'])

    print("=====================================")
    print("Running checks for PINCODE file: ", INPUT_PINCODE_FILE, ", DAYS: ", days, ", AGE: ", age)
    pincodes = getPinCodes(INPUT_PINCODE_FILE)
    slots = getAvailibilityForRangePinCodes(days, age, pincodes)

    if len(slots) < 1:
        return "No Slots Available!!"
    else:
        OUTPUT_FILE = 'availibility.csv'
        writeSlotsToCSV(slots, OUTPUT_FILE)
        table = getTable(OUTPUT_FILE)
        table.format = True

        return table.get_html_string(attributes={"name":"my_table", "class":"red_table"})

def getTable(OUTPUT_FILE):
    fp = open(OUTPUT_FILE, "r")
    mytable = from_csv(fp)
    fp.close()
    return mytable

app.run()