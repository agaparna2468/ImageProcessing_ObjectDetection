class Solution:
    def checkunique(self, y: str) -> bool:
        for i in range(0, len(y)):
            ch = y[i]
            if y[i:].find(ch) != -1:
                return False
        return True

    def lengthOfLongestSubstring(self, s: str) -> int:
        for i in range(0, len(s)):
            y = s[0:len(s) - i]
            h = len(y)
            if self.checkunique(y):
                return h
        return 0


chat = "yy"
print(chat[1:1])