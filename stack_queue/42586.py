def solution(progresses, speeds):
    answer = []
    while True:
        count = 0
        print(progresses)
        if progresses[0] >= 100:
            for i in progresses:
                if i >= 100:
                    count += 1
                else:
                    break
        if count != 0:
            for i in range(count):
                progresses.pop(0)
                speeds.pop(0)
            answer.append(count)
        if len(progresses) == 0:
            break
        for i, j in enumerate(progresses):
            progresses[i] += speeds[i]
    print(answer)
    return answer
