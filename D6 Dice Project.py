D6 = [1,2,3,4,5,6]
import random
roll = input("Type 'roll' to roll the dice:")
if roll == "roll":
    print(random.choice(D6))