class Parent():
    """ This class use a parent to explain a parent class. """

    def __init__(self, last_name, eye_color):
        print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name: "+ self.last_name)
        print("Eye Color: "+ self.eye_color)

marshall_law = Parent("Law", "Brown")
marshall_law.show_info()
