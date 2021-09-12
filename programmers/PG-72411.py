# https://programmers.co.kr/learn/courses/30/lessons/72411
from itertools import combinations


def solution(orders, course):
    answer = []

    for k in course:
        if k == 1:
            continue
        course_table  = {}
        max_count = -1
        for order in orders:
            combination = list(combinations(order, k))
            for course_combination in combination:
                course_combination_string = "".join(sorted(list(course_combination)))
                if course_combination_string not in course_table:
                    course_table[course_combination_string] = 1
                    if course_table[course_combination_string] > max_count:
                        max_count = course_table[course_combination_string]
                else:
                    course_table[course_combination_string] += 1
                    if course_table[course_combination_string] > max_count:
                        max_count = course_table[course_combination_string]
        for course_combination_string, count in course_table.items():
            if count >= 2 and count == max_count:
                answer.append(course_combination_string)
    answer.sort()

    return answer
