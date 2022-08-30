class Solution:
    def myAtoi(self, s: str) -> int:
        new_string = s.strip()
        if new_string == '':
            return 0
        if len(new_string) == 1:
            if new_string.isdigit():
                return int(new_string)
            else:
                return 0
        if (new_string[0] == '-') and (new_string[1].isdigit()) and (new_string[1] != '0'):
            int_string = new_string[1:]
            int_string = ''.join(ch for ch in int_string if ch.isdigit() or ch == '.')
            final_answer = -int(int_string)
            if final_answer >= -2147483648:
                return final_answer
            else:
                return -2147483648
        elif (new_string[0] == '+') and (new_string[1].isdigit()) and (new_string[1] != '0'):
            int_string = new_string[1:]
            int_string = ''.join(ch for ch in int_string if ch.isdigit() or ch == '.')
            final_answer = int(int_string)
            if final_answer <= 2147483647:
                return final_answer
            else:
                return 2147483647
        elif new_string[0].isdigit():
            int_string = ''.join(ch for ch in new_string if ch.isdigit() or ch == '.')
            if '.' in int_string:
                int_string = int_string.split('.')[0]
            final_answer = int(int_string)
            if final_answer <= 2147483647:
                return final_answer
            else:
                return 0
        else:
            return 0