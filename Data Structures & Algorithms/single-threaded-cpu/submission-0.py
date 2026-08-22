class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sorted_tasks = [(enqueue, processing, i) for i, (enqueue, processing) in enumerate(tasks)]
        sorted_tasks.sort()

        heap = []
        res = []

        time = 0
        i = 0
        n = len(tasks)

        while i < n or heap:
            if not heap and time < sorted_tasks[i][0]:
                time = sorted_tasks[i][0]
            
            while i < n and sorted_tasks[i][0] <= time:
                enqueue, processing, index = sorted_tasks[i]
                heapq.heappush(heap, (processing, index))
                i += 1
            
            processing, index = heapq.heappop(heap)

            res.append(index)
            time += processing
        return res