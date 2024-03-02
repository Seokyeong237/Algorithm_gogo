def solution(n, s):
    answer = []
    # 곱이 최대가 되려면 각 수의 차이가 작아야함
    
    if s < n:
        return [-1]
    
    for _ in range(n):
        answer.append(s//n)
    print(answer)
    
    index = len(answer)-1
    for i in range(s-sum(answer)):
        answer[index] += 1
        index -= 1
        
    return answer
        
        
            
 
