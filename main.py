class IOString:
    def __init__(self):
        self.s1 = ""
    def gs(self):
        self.s1 = input("Enter a string")
    def ps(self):
      print(self.s1.upper())
s1 = IOString()
s1.gs()
s1.ps()