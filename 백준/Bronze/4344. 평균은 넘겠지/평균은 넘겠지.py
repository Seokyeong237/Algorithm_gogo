count = int(input())

r_ratio = []
ff_ratio = []

for i in range(0, count):
    score = list(map(int, input().split()))

    average = sum(score[1:])/score[0]

    ratio = []
    
    for j in range(1, len(score)):
        if (score[j] > average):
            ratio.append(score[j])
    ro_ratio = (len(ratio) / score[0]) * 100
    roo_ratio = f'{ro_ratio:.3f}%'
    
    print(roo_ratio)