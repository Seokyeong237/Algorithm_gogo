num = int(input())

name_list = []

for i in range(num):
    name_list=input().split()
    name_list[0]='god'
        
    print(str.join('', name_list))