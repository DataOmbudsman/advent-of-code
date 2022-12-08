def _calculate_viewing_distance(baseline, array):
    i = 0
    for element in array:
        i += 1
        if element >= baseline:
            break
    return i


def max_scenic_score(matrix):
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    max_score = 0

    for row_index in range(n_rows):
        for col_index in range(n_cols):
            current_tree = matrix[row_index][col_index]

            trees_above = [tree
                           for i, row in enumerate(matrix)
                           for j, tree in enumerate(row)
                           if i < row_index and j == col_index][::-1]

            trees_below = [tree
                           for i, row in enumerate(matrix)
                           for j, tree in enumerate(row)
                           if i > row_index and j == col_index]

            trees_left = [tree
                          for i, row in enumerate(matrix)
                          for j, tree in enumerate(row)
                          if i == row_index and j < col_index][::-1]

            trees_right = [tree
                           for i, row in enumerate(matrix)
                           for j, tree in enumerate(row)
                           if i == row_index and j > col_index]

            dist_up = _calculate_viewing_distance(current_tree, trees_above)
            dist_down = _calculate_viewing_distance(current_tree, trees_below)
            dist_left = _calculate_viewing_distance(current_tree, trees_left)
            dist_right = _calculate_viewing_distance(current_tree, trees_right)

            score = dist_up * dist_down * dist_left * dist_right
            max_score = max(score, max_score)

    return max_score


def main():
    with open('input') as lines:
        tree_matrix = []
        for line in lines:
            line = line.rstrip()
            row = [int(char) for char in line]
            tree_matrix.append(row)
        print(max_scenic_score(tree_matrix))


if __name__ == "__main__":
    main()
