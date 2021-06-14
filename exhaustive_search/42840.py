def solution(answers):
    answer = []
    person1_ans = [1, 2, 3, 4, 5]
    person2_ans = [2, 1, 2, 3, 2, 4, 2, 5]
    person3_ans = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0, 0, 0]
    for i in range(0, len(answers), 1):
        if answers[i] == person1_ans[i%5]:
            count[0] += 1
        if answers[i] == person2_ans[i%8]:
            count[1] += 1
        if answers[i] == person3_ans[i%10]:
            count[2] += 1
    max = 0
    for i in count:
        if max < i:
            max = i
    for i in range(0, len(count), 1):
        if max == count[i]:
            answer.append(i+1)
    return answer
