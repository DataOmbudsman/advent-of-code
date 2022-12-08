def count_visible_trees(matrix):
    visible_trees = set()  # represented by coordinates
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    def _update_if_visible(i_, j_, max_height_in_direction):
        tree_height = matrix[i_][j_]
        if tree_height > max_height_in_direction:
            visible_trees.add((i_, j_))
            max_height_in_direction = tree_height
        return max_height_in_direction

    for i in range(n_rows):

        # in each row, left to right
        max_height = -1
        for j in range(n_cols):
            max_height = _update_if_visible(i, j, max_height)

        # in each row, right to left
        max_height = -1
        for j in reversed(range(n_cols)):
            max_height = _update_if_visible(i, j, max_height)

    for j in range(n_cols):

        # in each column, top to bottom
        max_height = -1
        for i in range(n_rows):
            max_height = _update_if_visible(i, j, max_height)

        # in each column, bottom to top
        max_height = -1
        for i in reversed(range(n_rows)):
            max_height = _update_if_visible(i, j, max_height)

    print(len(visible_trees))


def main():
    with open('input') as lines:
        tree_matrix = []
        for line in lines:
            line = line.rstrip()
            row = [int(char) for char in line]
            tree_matrix.append(row)
        count_visible_trees(tree_matrix)


if __name__ == "__main__":
    main()
