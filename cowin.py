import requests
import json
import datetime
import csv
from requests.exceptions import HTTPError
from SlotDetails import SlotDetails

# ///////////////      CONFIGURATIONS     //////////////////////////////////
OUTPUT_FILE = 'availibility.csv'
INPUT_PINCODE_FILE = 'pincodes.csv'

BASE_URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}"
DAYS_TO_CHECK = 7
AGE = 37
# //////////////////////////////////////////////////////////////////////////

def getPinCodes(input_file):
    pincodes = []
    with open(input_file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            pincodes.append(row["Pincode"])

    return pincodes

def getAvailibilityForRangePinCodes(days_to_check, age, pincodes):
    slots = []
    for code in pincodes:
        getAvailibilityForPincode(code, days_to_check, age, slots)

    return slots


def getAvailibilityForPincode(pin_code, days_to_check, age, slots):
    print("Checking for PIN_CODE: ", pin_code, "...")

    today = datetime.datetime.today()
    day_list = [today + datetime.timedelta(days=x) for x in range(days_to_check)]
    date = [x.strftime("%d-%m-%Y") for x in day_list]

    number_of_available = 0

    for current_date in date:
        url = BASE_URL.format(pin_code, current_date)
        response = requests.get(url)

        if response.ok:
            json_response = response.json()

            if json_response["centers"]:
                    for center in json_response["centers"]:
                        for session in center["sessions"]:
                            if session["min_age_limit"] <= age:

                                if int(session["available_capacity"]) > 0:
                                    s = SlotDetails(pin_code,
                                                    current_date, 
                                                    center["name"], 
                                                    center["block_name"],
                                                    center["fee_type"],
                                                    session["available_capacity"],
                                                    session["vaccine"],
                                                    )
                                    slots.append(s)

                                    number_of_available = number_of_available + 1
    
    if number_of_available > 0:
        print("AVAILABLE SLOTS FOR PIN_CODE ",pin_code," ARE: ",number_of_available)

    
def writeSlotsToCSV(slots, output_file):
    with open(output_file, 'w',) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Pincode', 'Date', 'Center', 'Block','Fee Type','Capacity','Vaccine'])

        for s in slots:
            writer.writerow([s.pincode, s.date, s.center, s.block, s.fee_type, s.available_capacity, s.vaccine])

if __name__ == '__main__':
    pincodes = getPinCodes(INPUT_PINCODE_FILE)
    slots = getAvailibilityForRangePinCodes(DAYS_TO_CHECK, AGE, pincodes)
    writeSlotsToCSV(slots, OUTPUT_FILE)
