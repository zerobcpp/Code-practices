class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [0] * length
        self.snapshot = {}
        self.n = 0
        

    def set(self, index: int, val: int) -> None:
        self.arr[index] = val
        

    def snap(self) -> int:
        ret = self.n
        self.snapshot[self.n] = self.arr[:]
        self.n += 1
        return ret

    def get(self, index: int, snap_id: int) -> int:
        return self.snapshot[snap_id][index]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)