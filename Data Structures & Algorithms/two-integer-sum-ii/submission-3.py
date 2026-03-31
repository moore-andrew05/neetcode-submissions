class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) -1

        while p2 > p1:

            current_sum = numbers[p1] + numbers[p2]

            if target == current_sum:
                return [p1 + 1, p2 + 1]
            
            if target > current_sum:
                p1 += 1

            if target < current_sum:
                p2 -= 1
                