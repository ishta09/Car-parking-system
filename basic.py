from fastapi import FastAPI
from typing import Optional
#from car import car
from basic import main

app = FastAPI()


@app.get('/')
def index():
    return {'key' : 'value'}

@app.post('/car_entry')
def create_car(numplate:str,parking_lot_id:int):
    carob=car(numplate)
    main(carob,"ENTRY",parking_lot_id)
    return "entry success"

@app.post('/car_exit')
def delete_car(numplate:str,parking_lot_id:int):
    carob=car(numplate)
    main(carob,"EXIT",parking_lot_id)
    return "exit success"





import heapq

class Car:
    def __init__(self, reg_no,park_hours):
        self.reg_no = reg_no
        self.park_hours=park_hours
        

class ParkingLot:
    def __init__(self, total_slots):                          
        self.reg_slot_dict = dict()
        self.car_charge_ticket=dict()
        self.free_parking_lots = []
        for i in range(1, total_slots + 1):
            heapq.heappush(self.free_parking_lots, i)
            
            
    def nearest_slot(self):
        if self.free_parking_lots:
            return heapq.heappop(self.free_parking_lots) 
            
        else:
            None
            
    def calculateCharges(self,numHour):
        parking_charge=0
        if(numHour<=3):
            parking_charge=30
        elif(numHour>3 and numHour<18):
            parking_charge=30+5*(numHour-3)
        elif(numHour>18):
            parking_charge=150
        return parking_charge

    def park_car(self, car):
        slot_no = self.nearest_slot()
        if slot_no is None:
            print("parking lot is full")
            return
        self.reg_slot_dict[car.reg_no] = slot_no
        print("car no."+car.reg_no+" parked successfully"+" at slot number"+str(slot_no)+" for "+str(car.park_hours)+" hours")
        #charges calculation
        park_time=car.park_hours
        parking_charge=self.calculateCharges(park_time)
        self.car_charge_ticket[car.reg_no]=parking_charge

    def free_slot(self, slot_free):
        found = None
        for registration_no, slot in self.reg_slot_dict.items():
            if slot == slot_free:                            
                found = registration_no

        # remove car from all places
        if found:
            del self.reg_slot_dict[found]
            heapq.heappush(parking_lot.free_parking_lots, slot_free)
            print("slot freed ", slot_free)
            print('the charges to pay for car no. '+str(found)+' are: '+str(self.car_charge_ticket[found])+'Rs.')
            del self.car_charge_ticket[found]
        else:
            print("slot is not in use")
            
    def status(self):
        for car,slot in self.reg_slot_dict.items():
            print("Car no: {} slot no: {}".format(car,slot))
            
    
            
            
   

if __name__ == "__main__":
    parking_lot = ParkingLot(8)
    print(parking_lot.free_parking_lots)

    car = Car("RJ20 JP4500",4)
    parking_lot.park_car(car)

    car = Car("RJ14 ZA3250",2)
    parking_lot.park_car(car)

    car = Car("RJ26 Pa5642",3)
    parking_lot.park_car(car)

    car = Car("RJ20 Kb1900",6)
    parking_lot.park_car(car)

    car = Car("RJ20 KK1800",7)
    parking_lot.park_car(car)

    car = Car("RJ14 JP1500",8)
    parking_lot.park_car(car)

    car = Car("RJ19 IK1434",18)
    parking_lot.park_car(car)

    car = Car("RJ16 JK1535",9)
    parking_lot.park_car(car)

    # When no slots are available then
    slot_no = parking_lot.nearest_slot()
    print(slot_no)
    
    # Leave slot no 2
    slot_no_to_be_freed = 2
    parking_lot.free_slot(slot_no_to_be_freed)

    

    car = Car("DL12 KA1545",5)
    parking_lot.park_car(car)

    car = Car("DL18 SA1757",6)
    parking_lot.park_car(car)
    parking_lot.status()
    print(parking_lot.free_parking_lots)
   
   





    