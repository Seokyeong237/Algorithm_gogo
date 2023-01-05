str_list = input()
num_list = list()
for i in str_list:
	num_list.append(int(i))

num_list = reversed(sorted(num_list))
res=''
for i in num_list:
    res += str(i)

print(res)
