def solution(participant, completion):
    
    dic={} 

    # 딕셔너리에 참가한 선수 이름을 key, value를 카운드(동명이인 일 경우 +1)
    for name in participant:
        # 딕셔너리에 이름이 없다면 
        if name not in dic:
            dic[name] = 1
        # 이름이 있다면 value + 1
        else:
            dic[name] = dic[name]+1
    # 완주한 선수를 찾으면 value - 1 
    for name in completion:
        if dic[name] >= 1:
            dic[name] = dic[name]-1
            
    # value == 1인 선수가 완주하지 못한 선수
    for k, v in dic.items():
        if v==1:
            return k
        
def solution(participant, completion):
    
    dic={}
    for name in participant:
        if name not in dic:
            dic[name] = 1
        else:
            dic[name] = dic[name]+1

    for name in completion:
        if dic[name] >= 1:
            dic[name] = dic[name]-1
        if dic[name] == 0:
            del dic[name] #삭제하는 부분에서 시간이 많이 소요
            
    return list(dic)[0]

# collections의 Counter
from collections import Counter

def solution(participant, completion):
    # 참가자들의 이름을 카운트
    participant_count = Counter(participant)
    print(participant_count) #	Counter({'mislav': 2, 'stanko': 1, 'ana': 1})
    # 완주자들의 이름을 카운트
    completion_count = Counter(completion) #   Counter({'stanko': 1, 'ana': 1, 'mislav': 1})
    print(completion_count)
    
    # 참가자 목록에서 완주자 목록을 빼면, 완주하지 못한 사람이 남음
    non_complete_count = participant_count - completion_count
    print(non_complete_count) #   Counter({'mislav': 1})
    # 완주하지 못한 사람의 이름을 반환
    # non_complete_count는 완주하지 못한 사람의 이름과 그 수를 가진 Counter 객체이므로,
    # 여기서는 완주하지 못한 사람이 하나만 있다고 가정하여 첫 번째 키를 반환합니다.
    return list(non_complete_count.keys())[0]

