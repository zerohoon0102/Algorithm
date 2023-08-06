from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        queue = deque([])
        chk = {}
        cur_length = 0
        for char in s:
            if char in chk:
                while 1:
                    preChar = queue.popleft()
                    if preChar == char:
                        queue.append(char)
                        break
                    else:
                        del chk[preChar]
                        cur_length -= 1
            else:
                queue.append(char)
                chk[char] = True
                cur_length += 1
                result = max(result, cur_length)
        
        return result