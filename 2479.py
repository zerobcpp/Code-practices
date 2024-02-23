class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        r_cnt = [0] * n
        room = [i for i in range(n)]
        r_use = []
        heapify(room)
        meetings.sort()
        
        
        for start, end in meetings:
            
            while r_use and r_use[0][0] <= start:
                _, free_room = heappop(r_use)
                heappush(room, free_room)

            if room:
                cur_room = heappop(room)
                heappush(r_use, (end, cur_room))
            else:
                f_end, cur_room  = heappop(r_use)
                heappush(r_use, (f_end + end, cur_room))
            
            r_cnt[cur_room] += 1
            
            #print(r_cnt, room, r_use)
        
        print(r_cnt)
        
        res = 0
        mx = -1
        for i in range(n):
            if r_cnt[i] > mx:
                mx = r_cnt[i]
                res = i
        
        return res
            