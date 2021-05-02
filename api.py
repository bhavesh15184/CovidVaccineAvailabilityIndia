import flask
import json
import prettytable
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
    pincodes = getPinCodes(INPUT_PINCODE_FILE)
    slots = getAvailibilityForRangePinCodes(7, 37, pincodes)

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