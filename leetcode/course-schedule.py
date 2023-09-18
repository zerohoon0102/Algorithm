from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses

        for a, b in prerequisites:
            indegree[a] += 1
            pre[b].append(a)
        
        queue = deque([])
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        cnt = 0
        while queue:
            course = queue.popleft()
            cnt += 1
            for nxt_course in pre[course]:
                indegree[nxt_course] -= 1
                if indegree[nxt_course] == 0:
                    queue.append(nxt_course)
        if cnt == numCourses:
            return True
        else:
            return False
