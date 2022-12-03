def game_score(a, b):
    if a == "A" and b == "X":
        return 4
    if a == "B" and b == "Y":
        return 5
    if a == "C" and b == "Z":
        return 6
    if a == "A" and b == "Y":
        return 8
    if a == "B" and b == "Z":
        return 9
    if a == "C" and b == "X":
        return 7
    if b == "X":
        return 1
    if b == "Y":
        return 2
    if b == "Z":
        return 3


def game_score_two(a, b):
    score = 0
    if b == "X":
        score += 0
        if a == "A":
            score += 3
        if a == "B":
            score += 1
        if a == "C":
            score += 2
    if b == "Y":
        score += 3
        if a == "A":
            score += 1
        if a == "B":
            score += 2
        if a == "C":
            score += 3
    if b == "Z":
        score += 6
        if a == "A":
            score += 2
        if a == "B":
            score += 3
        if a == "C":
            score += 1
    return score


def main():
    sum = 0
    with open("input.txt") as f:
        for line in f.readlines():
            sum += game_score_two(line[0], line[2])
    print(sum)


if __name__ == "__main__":
    main()
