list1 = []

for i in range(9):
    list1.append(int(input()))

maxx = list1[0]

for j in range(len(list1)):
    if (j==8):
        break

    if (maxx < list1[j+1]):
        maxx = list1[j+1]

print(maxx)
print(list1.index(maxx)+1)