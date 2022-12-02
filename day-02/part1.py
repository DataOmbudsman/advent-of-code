ROCK = "Rock"
PAPER = "Paper"
SCISSORS = "Scissors"


decode_opponent_choice = {
    'A': ROCK,
    'B': PAPER,
    'C': SCISSORS,
}


decode_my_choice = {
    'X': ROCK,
    'Y': PAPER,
    'Z': SCISSORS,
}


def _get_score_shape(shape):
    if shape == ROCK:
        return 1
    elif shape == PAPER:
        return 2
    return 3


def _get_score_outcome(opponent_shape, my_shape):
    if opponent_shape == my_shape:
        return 3
    elif (
            (opponent_shape == ROCK and my_shape == PAPER) or
            (opponent_shape == PAPER and my_shape == SCISSORS) or
            (opponent_shape == SCISSORS and my_shape == ROCK)
    ):
        return 6
    return 0


def calculate_score(opponent_choice, my_choice):
    opponent_shape = decode_opponent_choice[opponent_choice]
    my_shape = decode_my_choice[my_choice]

    score_shape = _get_score_shape(my_shape)
    score_outcome = _get_score_outcome(opponent_shape, my_shape)
    return score_shape + score_outcome


def main():
    with open('input') as lines:
        total_score = 0
        for line in lines:
            line = line.rstrip()
            opponent_choice, my_choice = line.split()
            score = calculate_score(opponent_choice, my_choice)
            total_score += score

    print(total_score)


if __name__ == "__main__":
    main()
