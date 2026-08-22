class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)

        if max(freq.values()) > (len(s) + 1) // 2:
            return ""
        
        heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(heap)

        res = []
        prev_count = 0
        prev_char = ""

        while heap:

            count, char = heapq.heappop(heap)

            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_char))
            
            res.append(char)

            count += 1

            prev_count = count
            prev_char = char
        return "".join(res)