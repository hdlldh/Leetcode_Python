# Given two strings first and second, consider occurrences in some text of the 
# form "first second third", where second comes immediately after first, and third 
# comes immediately after second. 
# 
#  Return an array of all the words third for each occurrence of "first second 
# third". 
# 
#  
#  Example 1: 
#  Input: text = "alice is a good girl she is a good student", first = "a", 
# second = "good"
# Output: ["girl","student"]
#  Example 2: 
#  Input: text = "we will we will rock you", first = "we", second = "will"
# Output: ["we","rock"]
#  
#  
#  Constraints: 
# 
#  
#  1 <= text.length <= 1000 
#  text consists of lowercase English letters and spaces. 
#  All the words in text a separated by a single space. 
#  1 <= first.length, second.length <= 10 
#  first and second consist of lowercase English letters. 
#  
#  Related Topics String 👍 281 👎 266


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """

        word_arr = text.split(" ")
        n = len(word_arr)
        print(word_arr)

        if n <= 2: return []
        ans = []
        for i in range(2, n):
            if word_arr[i-2] == first and word_arr[i-1] == second:
                ans.append(word_arr[i])
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
