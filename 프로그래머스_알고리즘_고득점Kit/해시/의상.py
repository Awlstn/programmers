def solution(clothes):
    answer = 0
    answer += len(clothes)
    dic = {}
    for k, v in clothes:
        if v in dic:
            dic[v].append(k)
        else:
            dic[v] = [k]
    if len(dic) == 1:
        return answer
    elif len(dic) == 2:
        n = 1
        for i in list(dic.values()):
            n *= len(i)
        return answer+n
    elif len(dic) == 3:
        n = 0
        lst = [[0,1], [0,2], [1,2]]
        val = list(dic.values())
        for i, j in lst:
            n += len(val[i])*len(val[j])
        n += len(val[0])*len(val[1])*len(val[2])
        return answer+n
    else:
        n = 0
        lst = [[0,1], [0,2], [0,3], [1,2], [1,3], [2,3]]
        val = list(dic.values())
        for i, j in lst:
            n += len(val[i])*len(val[j])
        lst2 = [[0,1,2],[0,1,3],[1,2,3]]
        for i,j,k in lst2:
            n += len(val[i])*len(val[j])*len(val[k])
        n += len(val[0])*len(val[1])*len(val[2])*len(val[3])
        return answer+n
    
import itertools

def solution(clothes):
    answer = 0
    answer += len(clothes)
    dic = {}
    for k, v in clothes:
        if v in dic:
            dic[v].append(k)
        else:
            dic[v] = [k]
    num = []
    for i in list(dic.values()):
        num.append(len(i))
    if len(dic) == 1:
        return answer
    for i in range(2, len(num)+1):
        ncr = itertools.combinations(num, i)
        for j in list(ncr):
            n=1
            for k in j:
                n*=k
            answer+=n
    return answer

def solution(clothes):
    answer = 1
    type_count = {}
    for _, c_type in clothes:
        type_count[c_type] = type_count.get(c_type, 0) + 1 # 딕셔너리에 옷타입이 있으면 값을 가져오고 없으면 기본값 0
    
    for count in type_count.values():
        answer *= (count+1) # 안입는 경우까지 생각해서 + 1 해주는 거 
    
    return answer - 1 # 아무것도 안입는 경우 뺌
    
