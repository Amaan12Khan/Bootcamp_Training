class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        units=0
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        for i in range(len(boxTypes)):
            if truckSize>0:
                boxes_to_take = min(boxTypes[i][0], truckSize)
                units+=boxes_to_take*boxTypes[i][1]
                truckSize-=boxes_to_take
            else:
                break
        return units