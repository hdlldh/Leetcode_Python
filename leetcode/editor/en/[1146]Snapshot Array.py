# Implement a SnapshotArray that supports the following interface: 
# 
#  
#  SnapshotArray(int length) initializes an array-like data structure with the g
# iven length. Initially, each element equals 0. 
#  void set(index, val) sets the element at the given index to be equal to val. 
# 
#  int snap() takes a snapshot of the array and returns the snap_id: the total n
# umber of times we called snap() minus 1. 
#  int get(index, snap_id) returns the value at the given index, at the time we 
# took the snapshot with the given snap_id 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: ["SnapshotArray","set","snap","set","get"]
# [[3],[0,5],[],[0,6],[0,0]]
# Output: [null,null,0,null,5]
# Explanation: 
# SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
# snapshotArr.set(0,5);  // Set array[0] = 5
# snapshotArr.snap();  // Take a snapshot, return snap_id = 0
# snapshotArr.set(0,6);
# snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= length <= 50000 
#  At most 50000 calls will be made to set, snap, and get. 
#  0 <= index < length 
#  0 <= snap_id < (the total number of times we call snap()) 
#  0 <= val <= 10^9 
#  
#  Related Topics Array


# leetcode submit region begin(Prohibit modification and deletion)
class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.snap_id = 0
        self.snap_val = [[] for _ in range(length)]

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if not self.snap_val[index]:
            self.snap_val[index].append([self.snap_id, val])
        else:
            if self.snap_id == self.snap_val[index][-1][0]:
                self.snap_val[index][-1][1] = val
            else:
                self.snap_val[index].append([self.snap_id, val])

    def snap(self):
        """
        :rtype: int
        """
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        n = len(self.snap_val[index])
        if n == 0: return 0
        low = 0
        high = n - 1

        while low <= high:
            mid = low + (high - low) // 2
            if self.snap_val[index][mid][0] > snap_id:
                high = mid - 1
            else:
                low = mid + 1
        return self.snap_val[index][high][1] if high >= 0 else 0

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
# leetcode submit region end(Prohibit modification and deletion)
