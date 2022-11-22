"""This program will converts temperatures from Celsius to Fahrenheit  and
Fahrenheit to Celsius.  The user should be able to enter a temperature,
click a button and see its equivalent temparature. it will have
have two buttons -- one to treat the input as Fahrenheit and convert it to
Celsius; and one to treat the input as Celsius and convert it to Fahrenheit"""


from breezypythongui import EasyFrame

class temparatureConvert(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Convert temparature")
        self.setSize(350,150)
        # Label and field for the Celcious

        self.addLabel(text = "Celcious", row = 0, column = 0, sticky = "NSEW")
        self.celciousField = self.addTextField(text = "", row = 0, column = 1)

        # Label and field for Furhenhite

        self.addLabel(text = "Furhenhite", row = 1, column = 0, sticky = "NSEW")
        self.furhenhiteField = self.addTextField(text = "", row = 1, column = 1)

        # The command button to convert celcious to furhenhiter

        self.addButton(text = "Convert furhenhite", row = 2, column = 1, 
                       command = self.convertFur)

         # The command button to convert furhenhiter to Celcious

        self.addButton(text = "Convert celcious", row = 2, column = 2, 
                       command = self.convertCel)

    # The event handling method for button
    def convertFur(self):
        """Inputs the temparature and convert it"""
        text = self.celciousField.getText()
        temparature = int(text)
        result = round((9/5) * temparature + 32, 2)
        self.furhenhiteField.setText(result)

     # The event handling method for button
    def convertCel(self):
        """Inputs the temparature and convert it"""
        text = self.furhenhiteField.getText()
        temparature = int(text)
        result = round((5/9) * (temparature - 32),2)
        self.celciousField.setText(result)

def main():
    """Instantiate and pop up the window."""
    temparatureConvert().mainloop()

if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("\nProgram closed.")
