class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = dict()

        for i in range(len(numbers)):
            if(target-numbers[i] in d):
                return sorted([i+1,d[target-numbers[i]]+1])
            else:
                d[numbers[i]] = i
        