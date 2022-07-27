from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for ith_customer_list in accounts:
            wealth = 0
            for jth_bank_money in ith_customer_list:
                wealth += jth_bank_money
            if wealth > max_wealth:
                max_wealth = wealth
        return max_wealth

