class Solution:
    def longestValidParentheses(self, s: str) -> int:
        longest_length = 0

        arr = list(s)
        stack = []
        # 짝이 생기는 경우 문자열을 변경하여, 정상적인 substring임을 체크
        for i, c in enumerate(arr):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    left_idx = stack.pop()
                    arr[i] = "-"
                    arr[left_idx] = "-"
        
        cur_length = 0
        for c in arr:
            if c == "-":
                cur_length += 1
            else:
                longest_length = max(longest_length, cur_length)
                cur_length = 0
        longest_length = max(longest_length, cur_length)
        return longest_length
