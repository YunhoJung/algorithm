# https://programmers.co.kr/learn/courses/30/lessons/62048
import math

def solution(w,h):
    gcd = math.gcd(w, h)

    return w * h - (w + h - gcd)

