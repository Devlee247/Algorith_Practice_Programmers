def solution(s):
    answer = ""
    i = 0
    while i < len(s):
        if ord(s[i]) < 90:
            answer += str(s[i])
            i += 1
        else:
            index = ord(s[i])
            # one
            if index == 111:
                answer += "1"
                i += 3
            # s
            elif index == 115:
                # seven
                if ord(s[i+1]) == 101:
                    answer += "7"
                    i += 5
                # six
                else:
                    answer += "6"
                    i += 3
            # eight
            elif index == 101:
                answer += "8"
                i += 5
            # f
            elif index == 102:
                # four
                if ord(s[i+1]) == 111:
                    answer += "4"
                    i += 4
                # five
                else:
                    answer += "5"
                    i += 4
            # t
            elif index == 116:
                # two
                if ord(s[i+1]) == 119:
                    answer += "2"
                    i += 3
                # three
                else:
                    answer += "3"
                    i += 5
            elif index == 122:
                # zero
                answer += "0"
                i += 4
            else:
                # nine
                answer += "9"
                i += 4
    return int(answer)
