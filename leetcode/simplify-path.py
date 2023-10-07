import re
class Solution:
    def simplifyPath(self, path: str) -> str:
        routes = re.split('[/+]', path)
        result = []
        for route in routes:
            if not route or route == '.':
                continue
            if route == '..':
                if len(result) > 0:
                    result.pop()
            else:
                result.append(f'/{route}')
        if len(result) == 0:
            return '/'
        return ''.join(result)
