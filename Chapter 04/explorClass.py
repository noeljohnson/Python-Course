##GTG

# A program to explore classes

class Worker:
  def __init__(self, name, pay):
    self.name = name
    self.pay = pay

  def lastName(self):
    return(self.name.split()[-1])

  def giveRise(self, percent):
    self.pay = (1 + percent / 100) * self.pay

bob = Worker("Bob Smith", 50000)
sue = Worker("Sue Jones", 60000)
##TYJC
