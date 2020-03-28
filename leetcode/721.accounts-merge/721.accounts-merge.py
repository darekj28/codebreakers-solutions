class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # build our undirected graph
        graph = collections.defaultdict(set)
        for account in accounts:
            for email in account[2:]:
                graph[email].add(account[1])
                graph[account[1]].add(email)
        
        sol = []
        seen = set()
        for account in accounts:
            # if we already saw the email then we already associated it with a user
            if account[1] in seen:
                continue
            emails = self._dfs(sol, graph, seen, [], account[1])
            # problem requires that the emails are sorted
            emails.sort()
            sol.append([account[0]] + emails) # account[0] holds the username
        return sol
    
    def _dfs(self, sol, graph, seen, temp, currEmail):
        # ignore nodes already traversed in the graph
        if currEmail in seen:
            return
        # build our list of emails for the current user
        temp.append(currEmail)
        # update the nodes that have been visited
        seen.add(currEmail)
        # traverse the rest of current email's neighbors
        for neigh in graph[currEmail]:
            self._dfs(sol, graph, seen, temp, neigh)
        return temp