def solution(phone_book):
    answer = True
    dic = dict()
    for nums in phone_book:
        insert(dic, nums)
    for nums in phone_book:
        num = search(dic, nums)
        if num != nums:
            return False
    return answer

def insert(dic, nums):
    node = dic
    for num in nums:
        if num not in node:
            node[num] = dict()
        node = node[num]
    node['nums'] = nums

def search(dic, nums):
    node = dic
    for num in nums:
        if num in node:
            node=node[num]
            if 'nums' in node:
                return node['nums']