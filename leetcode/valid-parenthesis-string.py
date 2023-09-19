class Solution:
    def checkValidString(self, s: str) -> bool:
        left, rest = [], []
        for i, c in enumerate(s):
            if c == "(":
                left.append(i)
            elif c == ")":
                if not left:
                    if rest:
                        rest.pop()
                    else:
                        return False
                else:
                    left.pop()
            else:
                rest.append(i)
        while left:
            i = left.pop()
            if not rest or rest[-1] < i:
                return False
            rest.pop()

        return True
