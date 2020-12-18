all_inp = []
file = open("input.txt", "r") 
for i in file:
    i = i.strip("\n")
    all_inp.append(i)


for first in all_inp:
    for secon in all_inp:
        for third in all_inp:
            first = int(first)
            secon = int(secon)
            third = int(third)
            add_sum = first + secon + third
            if add_sum == 2020:
                mul_sum = first * secon * third
                print(str(first) + " + " + str(secon) + " + " + str(third) + " = 2020")
                print(str(first) + " * " + str(secon) + " * " + str(third) + " = "+str(mul_sum))
                break
