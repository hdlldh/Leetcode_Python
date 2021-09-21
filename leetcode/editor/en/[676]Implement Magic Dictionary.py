#
#Implement a magic directory with buildDict, and search methods.
# 
#
# 
#For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.
# 
#
# 
#For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.
# 
#
# Example 1: 
# 
#Input: buildDict(["hello", "leetcode"]), Output: Null
#Input: search("hello"), Output: False
#Input: search("hhllo"), Output: True
#Input: search("hell"), Output: False
#Input: search("leetcoded"), Output: False
# 
# 
#
# Note: 
# 
# You may assume that all the inputs are consist of lowercase letters a-z. 
# For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest. 
# Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables are persisted across multiple test cases. Please see here for more details. 
# 
# Related Topics Hash Table Trie



#leetcode submit region begin(Prohibit modification and deletion)
class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dictionary = collections.defaultdict(set)
        

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: None
        """

        for word in dict:
            for i in range(len(word)):
                word1 = word[:i]+"*"+word[i+1:]
                self.dictionary[word1].add(word[i])

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for i in range(len(word)):
            word1 = word[:i] + "*" + word[i + 1:]
            if word[i] in self.dictionary[word1]:
                if len(self.dictionary[word1])>1: return True
            else:
                if len(self.dictionary[word1])>0: return True
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
#leetcode submit region end(Prohibit modification and deletion)
