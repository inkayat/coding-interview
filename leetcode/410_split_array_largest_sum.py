from collections import defaultdict
import itertools

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        dp = defaultdict(lambda:defaultdict(lambda:-1))
        prefix_sum = [0] + list(itertools.accumulate(nums))
                
        for subarray_count in range(1, m + 1):
            for curr_index in range(n):
              
                if subarray_count == 1:
                    dp[curr_index][subarray_count] = prefix_sum[n] - prefix_sum[curr_index]
                    continue
                minimum_largest_split_sum = prefix_sum[n]
                for i in range(curr_index, n - subarray_count + 1):
                    first_split_sum = prefix_sum[i + 1] - prefix_sum[curr_index]

                    largest_split_sum = max(first_split_sum, dp[i + 1][subarray_count - 1])

                    minimum_largest_split_sum = min(minimum_largest_split_sum, largest_split_sum)

                    if first_split_sum >= minimum_largest_split_sum:
                        break

                dp[curr_index][subarray_count] = minimum_largest_split_sum
        
        return dp[0][m]
    
  
