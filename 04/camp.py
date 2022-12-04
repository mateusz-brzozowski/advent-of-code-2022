def is_all_overlapping(first, second):
    if first[0] >= second[0] and first[1] <= second[1]:
        return True
    if first[0] <= second[0] and first[1] >= second[1]:
        return True
    return False


def is_any_overlapping(first, second):
    if first[0] >= second[0] and first[0] <= second[1]:
        return True
    if first[1] >= second[0] and first[1] <= second[1]:
        return True
    if first[0] <= second[0] and first[1] >= second[0]:
        return True
    if first[1] <= second[1] and first[1] >= second[1]:
        return True
    return False


def overlapped_pairs(file_name):
    overlapped_pairs = 0
    first_pair = [0, 0]
    second_pair = [0, 0]
    with open(file_name) as f:
        for line in f.readlines():
            pairs = line.strip().split(",")
            first_pair = pairs[0].split("-")
            second_pair = pairs[1].split("-")
            first_pair = [int(first_pair[0]), int(first_pair[1])]
            second_pair = [int(second_pair[0]), int(second_pair[1])]
            overlapped_pairs += is_any_overlapping(first_pair, second_pair)
    return overlapped_pairs


def main():
    print(overlapped_pairs("input.txt"))


if __name__ == "__main__":
    main()
