class Parent():
    """ This class use a parent to explain a parent class. """

    def __init__(self, last_name, eye_color):
        print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name: "+ self.last_name)
        print("Eye Color: "+ self.eye_color)

class Child(Parent):
    """ This class create child of the Parent class. """

    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child constructor called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

marshall_law = Parent("Law", "Brown")
marshall_law.show_info()
forrest_law = Child("Law", "Brown", 5)
forrest_law.show_info()
