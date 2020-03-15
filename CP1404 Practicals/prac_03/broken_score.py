"""CP1404 - Practical
Program to determine score status
"""
import random


def main():
    score = random.randrange(1, 100)
    print(score)
    print(determine_score(score))


def determine_score(score):
    if score < 0 or score > 100:
        return "Invalid number"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
