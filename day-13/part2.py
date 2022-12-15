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


def _sort_packets(packets):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(packets)):
            a = packets[i-1]
            b = packets[i]
            if _are_in_order(a, b) > 0:
                packets[i-1] = b
                packets[i] = a
                swapped = True
    return packets


def calculate_decoder_key(packets):
    packets_sorted = _sort_packets(packets)[::-1]
    index1 = packets_sorted.index([[2]]) + 1
    index2 = packets_sorted.index([[6]]) + 1
    return index1 * index2


def main():
    with open('input') as lines:
        packets = [[[2]], [[6]]]
        for line in lines:
            line = line.rstrip()
            if line != '':
                parsed_array = _parse_array(line)
                packets.append(parsed_array)

    print(calculate_decoder_key(packets))


if __name__ == "__main__":
    main()
