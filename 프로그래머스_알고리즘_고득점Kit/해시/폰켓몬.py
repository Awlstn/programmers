def solution(nums):

    N2 = len(nums)//2 # 최대로 고를 수 있는 값
    dnum = [] # 다른 종류만 들어갈 리스트  
    
    for num in nums: # 다양한 종류의 폰켓몬 리스트를 돌면서
        if num not in dnum: # 다른 종류의 포켓몬 리스트에 num값이 없다면
            dnum.append(num) # 다른 종류 모으는 리스트에 저장

    if len(dnum) < N2: # 서로 다른 종류의 수가 최대로 고를 수 있는 수보다 작으면 
        return len(dnum)
    else: # 서로 다른 종류의 수가 최대로 고를 수 있는 수보다 같거나 크면
        return N2