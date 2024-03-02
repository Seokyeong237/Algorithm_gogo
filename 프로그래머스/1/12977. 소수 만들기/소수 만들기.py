import itertools

def solution(nums):
    answer = 0
    num_list = []

    def isPrime(num):
        if num < 2:
            return False
        for i in range(3, num//2 + 1):
            if num % i == 0:
                return False
        return True
    
    nCr = list(itertools.combinations(nums, 3))
    for i in nCr:
        num_list.append(list(i))
        
    for i in num_list:
        num = sum(i)
        if isPrime(num):
            answer += 1
            
    return answer