class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_dict = {}  # 값을 키로, 인덱스를 값으로 저장할 빈 딕셔너리
        
        for i, val in enumerate(nums):
            val2 = target - val  # 내가 지금 당장 필요한 짝꿍 숫자
            
            # 1. 내 짝꿍이 이미 딕셔너리(과거 기록)에 있는지 확인!
            if val2 in num_dict:
                return [num_dict[val2], i]  # 찾았다면 [짝꿍의 인덱스, 내 인덱스] 바로 리턴
                
            # 2. 짝꿍이 없다면, 나중에 다른 숫자가 나를 찾을 수 있게 내 정보 기록
            num_dict[val] = i
    
        