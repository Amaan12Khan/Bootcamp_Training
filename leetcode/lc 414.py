class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max=None
        second_max=None
        third_max=None
        for num in nums:
            if num==first_max or num==second_max or num==third_max:
                continue
            if first_max==None or num>first_max:
                third_max=second_max
                second_max=first_max
                first_max=num
            elif second_max==None or num>second_max:
                third_max=second_max
                second_max=num
            elif third_max==None or num>third_max:
                third_max=num
        if third_max==None:
            return first_max
        else:
            return third_max

