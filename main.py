from typing import List

def twoSum(nums: List[int], target: int)-> List[int]:
    # 전체 조합을 전부 검사
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                # targer two-sum을 찾았으면 return
                return [i, j]
    # 못 찾았을 때 빈 리스트를 return
    return []

# 실행 코드
'''
if __name__ == "__main__":
    arr = [2,7,11,15]
    target = 9
    print(twoSum(arr, target))
'''