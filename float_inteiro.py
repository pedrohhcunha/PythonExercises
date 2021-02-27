import math
import random
import time

while True:
    real = float(random.uniform(1, 100))

    int = math.floor(real)
    time.sleep(1)
    print('O numero float aleatório é {:.4f} e a dua parte inteira é {}' .format(
        real, int))
