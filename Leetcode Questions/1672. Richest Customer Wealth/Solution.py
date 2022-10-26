class Solution(object):
    def maximumWealth(self, accounts):
        results = []
        
        # For customers in the array of accounts
        for cust in accounts:
            # Initiate a running total for customer
            total = 0
            for bank in cust:
                # Add the value in bank to the customers total
                total += bank
            # For each of the customers append to new list the total each customer has (can be anon as this isnt needed for result)
            results.append(total)
        
        # Use in-built python method to find largest value in list
        return max(results)