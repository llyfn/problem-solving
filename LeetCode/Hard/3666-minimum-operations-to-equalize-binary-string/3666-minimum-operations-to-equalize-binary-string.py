class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        zeros = s.count('0')
        if zeros == 0: return 0
        unvisited = [SortedList(), SortedList()]
        for i in range(n + 1):
            if i != zeros: unvisited[i % 2].add(i)
        q = deque([(zeros, 0)])
        while q:
            u, d = q.popleft()
            min_x = max(k - n + u, 0)
            max_x = min(u, k)
            l = u + k - 2 * max_x
            r = u + k - 2 * min_x
            sl = unvisited[l % 2]
            idx = sl.bisect_left(l)
            rmv = []
            while idx < len(sl) and sl[idx] <= r:
                curr = sl[idx]
                if curr == 0: return d + 1
                q.append((curr, d + 1))
                rmv.append(curr)
                idx += 1
            for x in rmv: sl.remove(x)
        return -1