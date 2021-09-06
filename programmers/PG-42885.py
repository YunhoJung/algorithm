# https://programmers.co.kr/learn/courses/30/lessons/42885


def solution(people, limit):
    answer = 0
    left = 0
    right = len(people) - 1
    people.sort(reverse=True)

    while left <= right:
        weight_sum = people[left] + people[right]
        if weight_sum <= limit:
            right -= 1
        left += 1
        answer += 1

    return answer

