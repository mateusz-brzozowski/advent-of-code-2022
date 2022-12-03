def max_calories(file_name):
    calories = []
    max_calories = 0
    with open(file_name) as f:
        for line in f.readlines():
            if line == '\n':
                current_calories = sum(int(x) for x in calories)
                if current_calories > max_calories:
                    max_calories = current_calories
                calories = []
            else:
                calories.append(int(line))
    return max_calories


def top_three_calories(file_name):
    calories = []
    top_calories = [0, 0, 0]
    with open(file_name) as f:
        for line in f.readlines():
            if line == '\n':
                current_calories = sum(int(x) for x in calories)
                print(current_calories)
                if current_calories >= min(top_calories):
                    top_calories[top_calories.index(
                        min(top_calories))] = current_calories
                calories = []
            else:
                calories.append(int(line))
        print(top_calories)
    return sum(top_calories)


def main():
    print(max_calories("input.txt"))
    print(top_three_calories("input.txt"))


if __name__ == "__main__":
    main()
