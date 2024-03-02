import random

def solution(cards):
    isOpened = [False] * len(cards)
    rest = []
    score = []
    
    def openBox(box, boxNum):
        cnt = 0
        while not isOpened[box-1]:
            isOpened[box-1] = True
            cnt += 1
            box = boxNum
            boxNum = cards[box-1]
        return cnt
    
    while False in isOpened:
        if True in isOpened:
            for i in range(len(isOpened)):
                if not isOpened[i]:
                    rest.append(i+1)
            box = random.choice(rest)
            boxNum = cards[box-1]
            score.append(openBox(box, boxNum))
        else:
            box = random.randint(1, len(cards))
            # 열어야 하는 상자가 이미 열려있을 때까지 반복
            boxNum = cards[box-1]
            score.append(openBox(box, boxNum))
         
    if len(score) == 1:
        return 0
    
    score.sort()
    return score[-1] * score[-2]

    
        
    