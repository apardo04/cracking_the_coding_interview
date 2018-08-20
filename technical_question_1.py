# Print all positive integer solutions to the equation a**3 + b**3 = c**3 + d**3 where a,b,c,d are integers between 1 and 1000
#page: 23, 68 - 69


from collections import defaultdict
n = 1000
myMap = defaultdict(list)

for x in range(1, n+1):
    for y in range(1, n+1):
        myMap[x**3 + y**3].append((x,y))

for results in myMap:
    for pair1 in myMap[results]:
        for pair2 in myMap[results]:
            print(str(results) + ": " + str(pair1) + " = " + str(pair2))