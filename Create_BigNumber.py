import os
os.system('cls')

def solution(number, k):
    v, cnt, start = k, 0, 0
    while v > 0 :
        flag = 0
        v-=1
        for i in range(start, len(number)-1) :
            if number[i] < number[i+1] :
                start = i-1 if i > 0 else 0
                cnt += 1
                flag = 1
                number = number[:i] + number[i+1:]
                break
        if not flag : break;
    return number[:len(number)-(k-cnt)]

print(solution("1924",2))
print(solution("1231234",3))
print(solution("4177252841", 4))