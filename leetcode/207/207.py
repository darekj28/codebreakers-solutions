class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build graph where prereqs point to more advanced courses
        graph = collections.defaultdict(list)
        for courseDependency in prerequisites:
            graph[courseDependency[1]].append(courseDependency[0])
        visitingStatus = {} # 1 for visiting, 2 for visited
        
        for course in range(numCourses):
            if self._isCycle(graph, visitingStatus, course):
                return False
        return True
    
    # helper function that dfs through graph
    # if a cycle exists, return True
    def _isCycle(self, graph, visitingStatus, node):
        if node in visitingStatus:
            # if we're still visiting this node, then there's a cycle
            if visitingStatus[node] == 1:
                return True
            # if we've seen the node before and didn't see a cycle, it can't be part of a cycle ever
            elif visitingStatus[node] == 2: 
                return False
        
        # set the current node's visiting status to visiting
        visitingStatus[node] = 1
        
        for neigh in graph[node]:
            # dfs through all the neighbors and make sure they don't have any cycles
            if self._isCycle(graph, visitingStatus, neigh):
                return True

        visitingStatus[node] = 2
        return False