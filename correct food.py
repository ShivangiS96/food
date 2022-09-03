class parent():
    
    def __init__(self):
        print("This is parent class")
        
    def menu(dish):
        if dish=="pizza":
            print("You can add following toppings")
            print("More cheese | Add jalapeno")
        elif dish=="cold_coffee":
            print("You can add following toppings")
            print("Add chocolate flavour | Add caramel flavour")
        else:
            print("please enter valid dish")
            
    def final_amount(dish, add_ons):
        if dish=="pizza" and add_ons=="cheese":
            print("you need to pay 250 rs")
        elif dish=="pizza" and add_ons=="jalepeeno":
            print("you need to pay 255 rs")
        elif dish=="cold_coffee" and add_ons=="chocolate":
            print("you need to pay 175 rs")
        elif dish=="cold_coffee" and add_ons=="caramel":
            print("you need to pay 175 rs")
            
class child1(parent):
    
    def __init__(self,dish):
        self.new_dish = dish
        
    def  get_menu(self):
        parent.menu(self.new_dish)
        
class child2(parent):
    
    def __init__(self,dish,addons):
        self.new_dish = dish
        self.addons = addons
        
    def get_final_amount(self):
        parent.final_amount(self.new_dish,self.addons)
        
child1_object=child1("pizza")
child1_object.get_menu()

child2_object=child2("pizza","jalepeeno")
child2_object.get_final_amount()