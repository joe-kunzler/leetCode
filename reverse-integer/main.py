class Solution:
    def reverse(self, x: int) -> int:
        new_string = ''
        if x < 0:
            int_string = str(x).replace('-', '')
            print(int_string)
        else:
            int_string = str(x)
        length = len(int_string)
        for i in range(length):
            new_string = new_string + int_string[length - 1]
            length = length - 1
        final_answer = int(new_string)
        if x < 0 and -final_answer >= -2147483647:
            return -final_answer
        elif x > 0 and final_answer <= 2147483647:
            return final_answer
        else:
            return 0
