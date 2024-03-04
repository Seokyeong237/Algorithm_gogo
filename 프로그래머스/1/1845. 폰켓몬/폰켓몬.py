def solution(nums):
    cnt = int(len(nums) / 2)
    dic = {i:0 for i in nums}
    
    for i in nums:
        dic[i] += 1
        
    sorted_dic = dict(sorted(dic.items(), key= lambda item:item[1]))
    print(sorted_dic)
    
    # 1. 서로 다른 숫자 종류 >= cnt -> return cnt
    # 2. 서로 다른 숫자 종류 < cnt -> return cnt -1

    if len(sorted_dic.keys()) >= cnt:
        return cnt
    elif cnt - len(sorted_dic.keys()) == 1:
        return cnt - 1
    else:
        return len(sorted_dic.keys())