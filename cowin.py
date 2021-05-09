import requests
import json
import datetime
import csv
from requests.exceptions import HTTPError
from playsound import playsound
import os


# ///////////////      CONFIGURATIONS     //////////////////////////////////
OUTPUT_FILE = 'availibility.csv'
INPUT_PINCODE_FILE = 'pincode_small.csv'

BASE_URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}"
DAYS_TO_CHECK = 2
AGE = 37
# //////////////////////////////////////////////////////////////////////////

def getAvailibilityForRangePinCodes():

    with open(INPUT_PINCODE_FILE, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        slots = []
        for row in csv_reader:
            getAvailibilityForPincode(row["Pincode"], slots)

        writeSlotsToCSV(slots)

class SlotDetails:  
    def __init__ (self, pincode, date, center, block, fee_type, available_capacity, vaccine):  
         self.pincode   = pincode
         self.date   = date  
         self.center    = center  
         self.block = block 
         self.fee_type = fee_type  
         self.available_capacity = available_capacity 
         self.vaccine = vaccine 

def getAvailibilityForPincode(PIN_CODE, slots):
    print("Checking for PIN_CODE: ", PIN_CODE, "...")

    today = datetime.datetime.today()
    day_list = [today + datetime.timedelta(days=x) for x in range(DAYS_TO_CHECK)]
    date = [x.strftime("%d-%m-%Y") for x in day_list]

    number_of_available = 0

    for current_date in date:
        url = BASE_URL.format(PIN_CODE, current_date)
        response = requests.get(url)

        if response.ok:
            json_response = response.json()

            if json_response["centers"]:
                    for center in json_response["centers"]:
                        for session in center["sessions"]:
                            if session["min_age_limit"] <= AGE:

                                if int(session["available_capacity"]) > 0:
                                    s = SlotDetails(PIN_CODE,
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
        file = "beep.mp3"
        os.system("mpg123 " + file)
        print("AVAILABLE SLOTS FOR PIN_CODE ",PIN_CODE," ARE: ",number_of_available)

    
def writeSlotsToCSV(slots):
    with open(OUTPUT_FILE, 'w',) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Pincode', 'Date', 'Center', 'Block','Fee Type','Capacity','Vaccine'])

        for s in slots:
            writer.writerow([s.pincode, s.date, s.center, s.block, s.fee_type, s.available_capacity, s.vaccine])

if __name__ == '__main__':
    for x in range(100):
        getAvailibilityForRangePinCodes()
