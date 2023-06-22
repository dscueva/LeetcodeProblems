class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        my_set = set()
        tracker = {}
        totalSum = 0
        for num in arr:
            if num in tracker:
                tracker[num] += 1
            else:
                tracker[num] = 1

        for value in tracker.values():
            if value in my_set:
                return False
            my_set.add(value)


        return True
            

