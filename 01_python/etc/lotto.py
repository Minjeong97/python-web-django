
# "lotto"
import random

a = 1
b = [1, 2]

def pick_lotto():
    lucky = random.sample(range(1, 46), 6)
    return lucky

# test
if __name__ == '__main__':
    #print(__name__)  # lotto.py
    print('Test', pick_lotto())