def solution(arr):
    answer = []

    answer.append(arr[0])

    for number in arr[1:]:
        if(answer[-1] != number):
            answer.append(number)

    return answer