class User():
  def __init__(self, name, address, email, phone,id):
    self.__name = name                                                      
    self.__address = address                                      #this class is used to take users details and assign to the variables
    self.__email = email
    self.__phone = phone
    self.__id=id

class Account:
  def __init__(self, user_name, password, person):                #this class takes the account of the user and the password
    self.__user_name = user_name
    self.__password = password
    self.__person = person

  def reset_password(self):
    None


class Admin(Account):
  def __init__(self, user_name, password, person):                  #class for declaring thr methods of the admin like checking adding parking spot and check_password
    super().__init__(user_name, password, person)


  def check_pass(self,password):
      if password==Password:
        print("Valid")
      else:
          return


  def add_parking_spot(self, floor_name, spot):
    None

    
from abc import ABC, abstractmethod
from ctypes.wintypes import HRSRC  

class Vehicle(ABC):
  def __init__(self, license_number, vehicle_type, slot_num=None, dam=None):
    self.__license_number = license_number                                     #vehicle class taking the paraeters of vehicle number,type of thr vrhivle and the slot assignment of the vehicle
    self.__type = vehicle_type
    self.__slot_num = slot_num
    self.__dam=dam

  def assign_slot(self, slotnum):
    self.__slotnum = slotnum


class Car(Vehicle):
  hrfare=20
  def __init__(self, license_number, slot_num=None):
    super().__init__(license_number, VehicleType.CAR, slot_num)


class Bike(Vehicle):
  hrfare=10
  def __init__(self, license_number, slot_num=None):
    super().__init__(license_number, VehicleType.BIKE, slot_num)


class Truck(Vehicle):
  hrfare=25
  def __init__(self, license_number, slot_num=None):
    super().__init__(license_number, VehicleType.TRUCK, slot_num)

class Electric_vehic(Vehicle):
  hrfare=15
  def __init__(self, license_number, slot_num=None):
    super().__init__(license_number, VehicleType.Electric, slot_num)

class ParkingSpot(ABC):
  def __init__(self, number, parking_spot_type):
    self.__number = number                        
    self.__free = True
    self.__vehicle = None
    self.__parking_spot_type = parking_spot_type

  def is_free(self):
    return self.__free

  def assign_vehicle(self, vehicle):                 #method to assign a parking slot to the vrhicle
    self.__vehicle = vehicle
    free = False

  def remove_vehicle(self):
    self.__vehicle = None                            #method to remove the parking spot
    free = True


class Carspot(ParkingSpot):
  def __init__(self, number):
    super().__init__(number, ParkingSpotType.Car)                       #classes of different types of parking spot


class LargeSpot(ParkingSpot):
  def __init__(self, number):
    super().__init__(number, ParkingSpotType.LARGE)


class bikeSpot(ParkingSpot):
  def __init__(self, number):
    super().__init__(number, ParkingSpotType.MOTORBIKE)


class ElectricSpot(ParkingSpot):
  def __init__(self, number):
    super().__init__(number, ParkingSpotType.ELECTRIC)


class Pyment():                                                           #class to make payment

    def __init__(self,user,id,amnt):
        self.user_name=user
        self.user_id=id
        self.fare=amnt
    def pay(self,user,amntpaid):
        self.req_sent=request
        self.amt_paid=amntpaid
        self.status=status
    
class Card(Payment):
    def pay(self,cardnum,cvv):
        self.cardnum=cardnum
        self.cvv=cvv

class UPI(Payment):
    def pay(self,upiapp,):
        self.upi_met=upiapp


class Calac_fare(self,hrs,type):
    self.type=type
    fare=type.hrfare*self.hrs                                         #calculate the fare according to the hours of parking and the panalty charges if there is any vilation of rules
    if self.dam==1:
        pen_charges=50
    net_amnt=fare+pen_charges
    pay()

    
    
    





