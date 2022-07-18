##GTG

# using the random modules

import random

s_random = random.random() #useful for getting a floating point from 0 to 1
s_randint = random.randint(1, 2) #useful for playing heads or tails
s_events = ["Incarnation", "Transfiguration", "Crucifixion", "Resurrection"]
s_favEvent = random.choice(s_events)
s_shuffle = [i for i in s_events]
random.shuffle(s_shuffle)
##TYJC
