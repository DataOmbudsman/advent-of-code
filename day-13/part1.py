def _parse_array(array):
    return eval(array)


def _are_in_order(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        elif left > right:
            return -1
        return 0

    elif isinstance(left, list) and isinstance(right, list):
        max_length = max(len(left), len(right))
        for i in range(max_length):
            if i >= len(left):
                return 1
            elif i >= len(right):
                return -1

            l, r = left[i], right[i]
            in_order = _are_in_order(l, r)
            if in_order in [1, -1]:
                return in_order
        return 0

    else:
        left = [left] if isinstance(left, int) else left
        right = [right] if isinstance(right, int) else right
        return _are_in_order(left, right)


def sum_of_indices_in_good_packets(pairs):
    pairs = [(_parse_array(pair[0]), _parse_array(pair[1])) for pair in pairs]
    good_pair_indices = [ix + 1 for ix, pair in enumerate(pairs)
                         if _are_in_order(pair[0], pair[1]) == 1]

    return sum(good_pair_indices)


def main():
    with open('input') as lines:
        pairs = []
        pair = []
        for line in lines:
            line = line.rstrip()
            if line != '':
                pair.append(line)
            else:
                pairs.append(pair)
                pair = []
        pairs.append(pair)

    print(sum_of_indices_in_good_packets(pairs))


if __name__ == "__main__":
    main()
