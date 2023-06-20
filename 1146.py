# 1146. Snapshot Array

class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[(0, 0)] for i in range(length)]
        self.n = 0
        
        

    def set(self, index: int, val: int) -> None:
        self.arr[index].append((self.n, val))
        #print(self.arr)
        

    def snap(self) -> int:
        ret = self.n
        self.n += 1
        return ret

    def get(self, index: int, snap_id: int) -> int:
        idx = bisect_right(self.arr[index], (snap_id, float('inf')))
        #print(idx)
        return self.arr[index][idx-1][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)