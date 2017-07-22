from shuffler import *
from simulator import *

##Asks for the input of the deckstring
deckcode = str(input("Enter the deckcode of the deck you wish to practice:"))

sim = simulator()

sim.simulate_mulligan(deckcode)

#sim.reset()

