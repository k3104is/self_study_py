import random

def hangman(word):
    # 初期値
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    # ゲーム手順
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        # 一文字判定
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        # 出力
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        # 完成判定
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    # 勝敗判定
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose! It was {}.".format(word))

def random_word():
    words = ["cat", "dog", "fish", "bird", "human"]
    words_idx = random.randint(0, len(words) - 1)
    return words[words_idx]

# hangman("cat")
hangman(random_word())