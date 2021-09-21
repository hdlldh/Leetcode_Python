# Design an in-memory file system to simulate the following functions: 
# 
#  ls: Given a path in string format. If it is a file path, return a list that o
# nly contains this file's name. If it is a directory path, return the list of fil
# e and directory names in this directory. Your output (file and directory names t
# ogether) should in lexicographic order. 
# 
#  mkdir: Given a directory path that does not exist, you should make a new dire
# ctory according to the path. If the middle directories in the path don't exist e
# ither, you should create them as well. This function has void return type. 
# 
#  addContentToFile: Given a file path and file content in string format. If the
#  file doesn't exist, you need to create that file containing given content. If t
# he file already exists, you need to append given content to original content. Th
# is function has void return type. 
# 
#  readContentFromFile: Given a file path, return its content in string format. 
# 
# 
#  
# 
#  Example: 
# 
#  
# Input: 
# ["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
# [[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]
# 
# Output:
# [null,[],null,null,["a"],"hello"]
# 
# Explanation:
# 
#  
# 
#  
# 
#  Note: 
# 
#  
#  You can assume all file or directory paths are absolute paths which begin wit
# h / and do not end with / except that the path is just "/". 
#  You can assume that all operations will be passed valid parameters and users 
# will not attempt to retrieve file content or list a directory or file that does 
# not exist. 
#  You can assume that all directory names and file names only contain lower-cas
# e letters, and same names won't exist in the same directory. 
#  
#  Related Topics Design


# leetcode submit region begin(Prohibit modification and deletion)
class FileSystem(object):

    def __init__(self):
        self.root = {}
        self.root['#'] = {}

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        ans = []
        path_list = ('#' + path).strip('/').split('/')
        p = self.root
        for d in path_list:
            p = p[d]
            if not isinstance(p, dict):
                ans.append(d)
                return ans
        for k in p.keys():
            ans.append(k)
        ans.sort()
        return ans

    def mkdir(self, path):
        """
        :type path: str
        :rtype: None
        """
        path_list = ('#' + path).strip('/').split('/')
        p = self.root
        for d in path_list:
            if d not in p: p[d] = {}
            p = p[d]

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: None
        """
        path_list = ('#' + filePath).strip('/').split('/')
        p = self.root
        for d in path_list[:-1]:
            p = p[d]
        if path_list[-1] not in p:
            p[path_list[-1]] = content
        else:
            p[path_list[-1]] += content

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        path_list = ('#' + filePath).strip('/').split('/')
        p = self.root
        for d in path_list[:-1]:
            p = p[d]
        return p[path_list[-1]]

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
# leetcode submit region end(Prohibit modification and deletion)
