# How may row and columns 
# Analysis 1st line how many star and space are there
# initilize st and sp
# Print st no of stars and sp no of spaces
# update st and sp for next line

# sp = 4 st = 1
# sp = 3 st = 2
# sp = 2 st = 3
# sp = 1 st = 4
# sp = 0 st = 5
# sp -1  st +1
sp = 4
st = 1
for star in range(5):
  
    for x in range(sp): print(" ", end=" ")
    for x in range(st): print("*", end= " ")
    sp -= 1;
    st += 1;
    print("")


def sum(a, twop = 10,c = 0):
    y = 10
    return a + twop

print (y)
print( sum(twop = 5,a = 10) )
print(10+ 10)
print(1+ 10)
print(5+ 10)
print(5+ 10)