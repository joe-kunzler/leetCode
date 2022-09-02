class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            int_string = str(x)
            int_list = []
            for i in int_string:
                int_list.append(i)
            int_list.reverse()
            reversed_string = ''.join(int_list)
            if int_string == reversed_string:
                return True
            else:
                return False
