def GetNormalizedTime(oldTime):
    result = 0
    minutes = 0

    oldTime = oldTime.split(':')

    minutes = int(oldTime[1][0] + oldTime[1][1])

    if oldTime[1][2] == 'a':
        result += minutes  # add minutes
        if int(oldTime[0]) != 12:
            result += int(oldTime[0]) * 60

    else:
        result += minutes + 720  # add minutes
        result += int(oldTime[0]) * 60  # add hours

    return result


def TimeDifference(strArr):
    lenght = len(strArr)
    minimum = 1440

    diffAfterMidnight = 0
    diffBeforeMidnight = 0

    normAfterMidnight = []
    normBeforeMidnight = []

    for timeUnit in strArr:
        normAfterMidnight.append(GetNormalizedTime(timeUnit))
        normBeforeMidnight.append(minimum - GetNormalizedTime(timeUnit))

    for i in range(0, lenght - 1):
        for j in range(i, lenght - 1):
            diffAfterMidnight = normAfterMidnight[i] - normAfterMidnight[j + 1]

            if diffAfterMidnight < 0:
                diffAfterMidnight = -1 * diffAfterMidnight

            if minimum > diffAfterMidnight:
                minimum = diffAfterMidnight

    for i in range(0, lenght):
        for j in range(0, lenght):
            if i != j:
                diffBeforeMidnight = normBeforeMidnight[i] + normAfterMidnight[j]
                if minimum > diffBeforeMidnight:
                    minimum = diffBeforeMidnight

    print('min = ', minimum)
    return normBeforeMidnight + normAfterMidnight


print(TimeDifference(["10:00am", "11:45pm", "5:00am", "12:01am"]))
