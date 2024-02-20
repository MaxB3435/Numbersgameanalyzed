import random
ng = 1
h = 100
l = 1
g = int(h/2)
game = 1
ngtot = 0
number = random.randint(l,h)


while True:
    if game < 10000:
        if g != number:
            ng = ng +1
            if g > number:
               h = g - 1
               g = int((h+l)/2)
            elif g < number:
                l = g + 1
                g = int((h+l)/2)
        else:
            game = game +1
            h = 100
            l = 1
            g = int(h/2)
            number = random.randint(l,h)
            ngtot = ngtot + ng
            ng = 1
    else:
        avg = ngtot / 10000
        print(avg)
        exit()
