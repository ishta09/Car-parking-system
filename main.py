import heapq

def show_menu():
    
    print("\nPRESS:")
    print("\n (A) To park a new car\n (B) TO free a slot\n (C) To see status\n (D)To see all available slots\n (E)To see nearest available slot\n (F) To Exit ")
    optchoice=str(input())
    return optchoice

class Car:
    def __init__(self, reg_no,park_hours):
        self.reg_no = reg_no
        self.park_hours=park_hours
        
class ParkingLot:
    def __init__(self, total_slots):                          
        self.reg_slot_dict = dict()
        self.car_charge_ticket=dict()
        
        # initialize all slots as free
        self.free_parking_lots = []
        # Using min heap to get give minimun slot number
        for i in range(1, total_slots+1 ):
            heapq.heappush(self.free_parking_lots, i)
           
    def get_nearest_slot(self):
        if self.free_parking_lots:
            return heapq.heappop(self.free_parking_lots) 
            
        else:
            None
         
    def get_nearest_slot_demo(self):
        if self.free_parking_lots:
            return sorted(self.free_parking_lots)[0]
            
        else:
            None
            
    def calculateCharges(self,numHour):
        parking_charge=0
        if(numHour<=3):
            parking_charge=30
        elif(numHour>3 and numHour<18):
            parking_charge=30+5*(numHour-3)
        elif(numHour>=18):
            parking_charge=150
        return parking_charge

    def park_car(self, car):
        slot_no = self.get_nearest_slot()
        if slot_no is None:
            print("Sorry, parking lot is full")
            return
        
        self.reg_slot_dict[car.reg_no] = slot_no
        
        print("car no."+car.reg_no+" parked successfully"+" at slot number"+str(slot_no)+" for "+str(car.park_hours)+" hours")
        #charges calculation
        park_time=car.park_hours
        parking_charge=self.calculateCharges(park_time)
        
        self.car_charge_ticket[car.reg_no]=parking_charge

    
    def free_slot(self, slot_to_be_freed):
        found = None
        for registration_no, slot in self.reg_slot_dict.items():
            if slot == slot_to_be_freed:                            
                found = registration_no

        # remove car from all places
        if found:
            del self.reg_slot_dict[found]
            
            
            print("slot freed ", slot_to_be_freed)
            print('the charges to pay for car no. '+str(found)+' are: '+str(self.car_charge_ticket[found])+'Rs.')
            del self.car_charge_ticket[found]
        else:
            print("slot is not in use")
            
    def status(self):
            for car,slot in self.reg_slot_dict.items():
                print("Car no: {} slot no: {}".format(car,slot))
        
            
    
                           
if __name__ == "__main__":
    
    
    no_of_pl=10
    
    parking_lot=ParkingLot(no_of_pl)
    print("Free parking lots at initial are:")
    print(parking_lot.free_parking_lots) 
    
    while(1):
        choice=show_menu()
        
        if(choice=='A'):
            print("Enter car registration number:")
            reg_no=str(input())
            print("Enter time you want to park for:")
            hours=int(input())
            car=Car(reg_no,int(hours))
            parking_lot.park_car(car)
            
        elif(choice=='B'):
            print("enter the slot no. you want to free\n")
            slot_no_to_be_freed=int(input())
            parking_lot.free_slot(slot_no_to_be_freed)
            heapq.heappush(parking_lot.free_parking_lots, slot_no_to_be_freed)
            #parking_lot.free_parking_lots.append(slot_no_to_be_freed)
        elif(choice=="C"):
                print("the cars parked currently are:\n")
                parking_lot.status()
            
        elif(choice=='D'):
            print("All avaiable slots right now are:",end=' ')
            print(parking_lot.free_parking_lots)
        
        elif(choice=="E"):
            print("The nearest free slot is:",end=' ')
            print(parking_lot.get_nearest_slot_demo())
            
        elif(choice=="F"):
            print("Have a safe journey ahead!")
            break
        else:
            print("please enter a valid input")