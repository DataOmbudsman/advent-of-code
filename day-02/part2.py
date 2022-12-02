ROCK = "Rock"
PAPER = "Paper"
SCISSORS = "Scissors"
LOSE = "LOSE"
DRAW = "DRAW"
WIN = "WIN"


decode_opponent_choice = {
    'A': ROCK,
    'B': PAPER,
    'C': SCISSORS,
}


decode_expected_outcome = {
    'X': LOSE,
    'Y': DRAW,
    'Z': WIN,
}


what_loses_to_this = {
    PAPER: ROCK,
    ROCK: SCISSORS,
    SCISSORS: PAPER
}

what_beats_this = {v: k for k, v in what_loses_to_this.items()}


def _get_score_shape(shape):
    if shape == ROCK:
        return 1
    elif shape == PAPER:
        return 2
    return 3


def _get_score_outcome(opponent_shape, my_shape):
    if my_shape == what_loses_to_this[opponent_shape]:
        return 0
    elif my_shape == what_beats_this[opponent_shape]:
        return 6
    return 3


def _get_my_shape(opponent_shape, expected_outcome):
    if expected_outcome == LOSE:
        return what_loses_to_this[opponent_shape]
    elif expected_outcome == WIN:
        return what_beats_this[opponent_shape]
    return opponent_shape


def calculate_score(opponent_choice, expected_outcome):
    opponent_shape = decode_opponent_choice[opponent_choice]
    expected_outcome = decode_expected_outcome[expected_outcome]
    my_shape = _get_my_shape(opponent_shape, expected_outcome)

    score_shape = _get_score_shape(my_shape)
    score_outcome = _get_score_outcome(opponent_shape, my_shape)
    return score_shape + score_outcome


def main():
    with open('input') as lines:
        total_score = 0
        for line in lines:
            line = line.rstrip()
            opponent_choice, expected_outcome = line.split()
            score = calculate_score(opponent_choice, expected_outcome)
            total_score += score

    print(total_score)


if __name__ == "__main__":
    main()
