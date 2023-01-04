class ParkingGarage():
    # I like the attributes without parameters here since we know what we have
    # but I don't know how we're going to differentiate spaces upon paying/leaving by looking
    # at these attributes.
    def __init__(self):
        self.tickets = 9
        self.parking_spaces = ["A1","A2","A3","B1","B2","B3","C1","C2","C3",]
        self.current_ticket = {"paid": False}

    def takeTicket(self):
        user_input = input("Do you want to buy a parking spot?: ")
        if user_input == "yes":
            self.tickets -= 1
            # Very interesting!  Be careful with using the global keyword in relation to a class
            # as this is sort of counter-intuitive with OOP
            global user_parkingspot
            user_parkingspot = input(f"Here are the available parking spots, which one would you like {self.parking_spaces}: ")
            self.parking_spaces.remove(user_parkingspot)
        else:
            print("Okay, goodbye.")

    def payForParking(self):
        while True:
            user_amount = input("Parking spots cost $5, please pay: ")
            if user_amount == str(5):
                print("Your ticket has been paid, you have 15 minutes to leave.")
                self.current_ticket.update({"paid": True})
                break
            else:
                print("Please pay!")
        
               
    def leaveGarage(self):
        if self.current_ticket == {"paid": True}:
            print("Thank You, have a nice day")
        else:
            print("Please pay!")
        self.parking_spaces.append(user_parkingspot)
        self.tickets += 1

    # This would be where to put in driver code to run the program:
    # def run(self):
    #     input = . . . . 
    #     while truuue:
    #         if input == 'blahblah':
    #             self.leaveGarage()

car = ParkingGarage()
# Ideally we would be using these methods in driver code for a program instead of calling 
# them individually so that the program keeps functioning
car.takeTicket()
car.payForParking()
car.leaveGarage()