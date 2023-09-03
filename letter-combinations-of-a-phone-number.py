class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        digit_to_letters = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }
        
        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                result.append(combination)
            else:
                for letter in digit_to_letters[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])
        
        result = []
        backtrack("", digits)
        return result

# Test cases
solution = Solution()
num=input("Enter a num:-")
print(solution.letterCombinations("23")) # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(solution.letterCombinations(""))    # Output: []
print(solution.letterCombinations("2"))   # Output: ["a","b","c"]

#print(solution.letterCombinations(num)) 
