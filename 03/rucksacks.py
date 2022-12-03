def priority(letter):
    if letter.isupper():
        return ord(letter) - 38
    return ord(letter) - 96


def common_letter(first, second):
    for a in set(first):
        for b in set(second):
            if a == b:
                return b


def common_letter_three(first, second, third):
    for a in set(first):
        for b in set(second):
            for c in set(third):
                if a == b == c:
                    return a


def rucksack_priority(file_name):
    sum = 0
    with open(file_name) as f:
        for line in f.readlines():
            line = line.strip()
            letter = common_letter(
                line[:int(len(line)/2)], line[int(len(line)/2):])
            sum += priority(letter)
    return sum


def three_rucksacks_priority(file_name):
    sum = 0
    i = 0
    backpacks = ["", "", ""]
    with open(file_name) as f:
        for line in f.readlines():
            backpacks[i] = line = line.strip()
            i += 1
            if i % 3 == 0:
                i = 0
                letter = common_letter_three(
                    backpacks[0], backpacks[1], backpacks[2])
                sum += priority(letter)
    return sum


def main():
    print(rucksack_priority("input.txt"))
    print(three_rucksacks_priority("input.txt"))


if __name__ == "__main__":
    main()
