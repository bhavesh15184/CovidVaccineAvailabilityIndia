import json

class SlotDetails(object):  
    def __init__ (self, pincode, date, center, block, fee_type, available_capacity, vaccine):  
         self.pincode   = pincode
         self.date   = date  
         self.center    = center  
         self.block = block 
         self.fee_type = fee_type  
         self.available_capacity = available_capacity 
         self.vaccine = vaccine 

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

    def serialize(self):
        return {
            'pincode': self.pincode, 
            'date': self.date,
            'center': self.center,
            'block': self.block,
            'fee_type': self.fee_type,
            'available_capacity': self.available_capacity,
            'vaccine': self.vaccine,
        }