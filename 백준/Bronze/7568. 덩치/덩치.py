import re

list1 = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

lee = 0
list2 = []
for i in range(len(list1)):
    for a in re.findall(list1[i], word):
        lee += len(a)
        new_word = word.replace(a, '')
        list2.append(a)
cnn = len(list2)
print(list2)

lenn = len(new_word)
for j in range(len(list(new_word))-1):
    for k in range(1, len(list(new_word))):
        if list(new_word[j]) == list(new_word[k]):
            lenn -= 1

print(lenn)
print(len(word))
print(lee)
print(cnn)
print(cnn + lenn)

    