# python3 eventual_safe_states_802.py

class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        outdegree = [0] * len(graph)
        indegree = [[] for _ in range(len(graph))]

        for i in range(len(graph)):
            outdegree[i] = len(graph[i])
            for j in range(len(graph[i])):
                indegree[graph[i][j]].append(i)
                
        queue = []
        for i in range(len(outdegree)):
            if outdegree[i] == 0:
                queue.append(i)
        res = []   
        while queue:
            node = queue.pop(0)
            res.append(node)
            if indegree[node]:
                for rest in indegree[node]:
                    outdegree[rest] -= 1
                    if outdegree[rest] == 0:
                        queue.append(rest)
                    
        return sorted(res)

sol = Solution()
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
print(sol.eventualSafeNodes(graph))
