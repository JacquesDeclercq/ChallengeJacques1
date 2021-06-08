score_dict = {"A": 1,
                 "B": 3,
                 "C": 3,
                 "D": 2,
                 "E": 1,
                 "F": 4,
                 "G": 2,
                 "H": 4,
                 "I": 1,
                 "J": 1,
                 "K": 5,
                 "L": 1,
                 "M": 3,
                 "N": 1,
                 "O": 1,
                 "P": 3,
                 "Q": 10,
                 "R": 1,
                 "S": 1,
                 "T": 1,
                 "U": 1,
                 "V": 4,
                 "W": 4,
                 "X": 8,
                 "Y": 4,
                 "Z": 10,}


def score(word):
    if not word or word == "":
        print(f'Without input the score is 0!')
        return 0

    total_score = 0
    for letter in word.upper():
        score = score_dict.get(letter, -1)
        if score != -1:
            total_score += score
        else:
            print(f'Without valid input the score is 0!')
            return 0

    print(f'The total score: {total_score}')
    return total_score


if __name__ == '__main__':
    score("test")

