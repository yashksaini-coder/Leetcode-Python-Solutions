class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        line = []
        line_length = 0
        
        for word in words:
            # Check if the current word can fit in the current line
            if line_length + len(line) + len(word) <= maxWidth:
                line.append(word)
                line_length += len(word)
            else:
                # Distribute spaces evenly in the line
                spaces = maxWidth - line_length
                if len(line) == 1:
                    result.append(line[0] + ' ' * spaces)
                else:
                    extra_spaces = spaces % (len(line) - 1)
                    space_per_word = spaces // (len(line) - 1)
                    line_str = ""
                    for i in range(len(line) - 1):
                        line_str += line[i]
                        line_str += ' ' * (space_per_word + (1 if i < extra_spaces else 0))
                    line_str += line[-1]
                    result.append(line_str)
                
                # Reset the line
                line = [word]
                line_length = len(word)
        
        # Left-justify the last line
        last_line = ' '.join(line)
        last_line += ' ' * (maxWidth - len(last_line))
        result.append(last_line)
        
        return result

sol = Solution()
words1 = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth1 = 16
result1 = sol.fullJustify(words1, maxWidth1)
print(result1)

words2 = ["What","must","be","acknowledgment","shall","be"]
maxWidth2 = 16
result2 = sol.fullJustify(words2, maxWidth2)
print(result2)

words3 = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth3 = 20
result3 = sol.fullJustify(words3, maxWidth3)
print(result3)
