class Solution:
    def combinationSum2(self, candidates, target):
        def backtrack(start, target, current_combination):
            if target == 0:
                result.append(current_combination[:])
                return
            if target < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue  # Skip duplicates to avoid duplicate combinations
                current_combination.append(candidates[i])
                backtrack(i + 1, target - candidates[i], current_combination)  # Use the next candidate
                current_combination.pop()

        result = []
        candidates.sort()  # Sort candidates to handle duplicates
        backtrack(0, target, [])
        return result

# Example test cases
candidates1 = [10, 1, 2, 7, 6, 1, 5]
target1 = 8

candidates2 = [2, 5, 2, 1, 2]
target2 = 5

solution = Solution()
print(solution.combinationSum2(candidates1, target1))
# Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

print(solution.combinationSum2(candidates2, target2))
# Output: [[1, 2, 2], [5]]

#Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

#Each number in candidates may only be used once in the combination.

#Note: The solution set must not contain duplicate combinations.
