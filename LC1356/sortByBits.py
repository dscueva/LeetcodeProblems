from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # lets create new array thats empty
        # now lets loop through the array and convert it into its binary number and put into new array
        # as we do that we place the binary number and count the number of 1's into the hash map we create 
        # we then loop through the hash map and place into the original array based on the number of 1's if equal we place them in ascending order.
        temp_arr = []
        tracker = {}
        
        for num in arr:
            curr_binary = bin(num)
            count_ones = curr_binary.count('1')
            tracker[num] = count_ones

        def custom_sort_key(x):
            return (tracker[x], x)

        sorted_arr = sorted(arr, key=custom_sort_key)

        return sorted_arr