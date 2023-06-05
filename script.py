#1
for x in range(0,151):
    print(x)


#2
for y in range(5, 1000,5):
    print(y)


#3
for z in range(1, 101):
    if z % 10 == 0:
        print('Coding Dojo')
    elif z % 5 == 0:
        print('Coding')
    else:
        print(z)


#4
sum = 0
for big in range(0, 500000, 2):
        sum += big
print(sum)


#5
for j in range(2018, 0, -4):
        print(j)


#6

def counter (lowNum, highNum, mult):
    for sum in range(lowNum, highNum+1):
        if sum % mult == 0:
                print(sum)
counter(2, 9, 3)            

