class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_list = [word for word in s.split()]
        return len(new_list[len(new_list)-1])
        