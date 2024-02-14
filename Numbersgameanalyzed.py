import random
ng = 1

h = 100
l = 1
g = int(h/2)

#print ('Välj ett nummer')
#number = int(input())
number = random.randint(l,h)
print(number)
while True:
    if g != number:
        ng = ng +1
        print(g)
        if g > number:
            print('Nix, lägre')
            h = g - 1
            g = int((h+l)/2)
        elif g < number:
            l = g + 1
            print('Nix, högre')
            g = int((h+l)/2)
    else:
         print('Jag klarade spelet på', ng,'gissningar!')
         exit()

    