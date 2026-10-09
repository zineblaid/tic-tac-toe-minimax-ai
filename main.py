
# Tic-Tac-Toe avec IA utilisant l'algorithme Minimax

def create_board():
    return [" "] * 9

def display_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_winner(board):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]   # 'X' ou 'O'
    if " " not in board:
        return "Draw"
    return None

def human_move(board):
    while True:
        try:
            pos = int(input("Votre coup (1-9) : ")) - 1
            if 0 <= pos < 9 and board[pos] == " ":
                return pos
            else:
                print("Case invalide.")
        except:
            print("Entrée incorrecte.")

# -------------------------------
#  PARTIE MINIMAX (IA)
# -------------------------------

def minimax(board, is_maximizing):
    winner = check_winner(board)

    # Valeurs finales des feuilles de l'arbre :
    if winner == "O": return 1      # L'IA gagne
    if winner == "X": return -1     # Humain gagne
    if winner == "Draw": return 0   # Match nul

    if is_maximizing:  
        best_score = -999
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"  # IA joue
                score = minimax(board, False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score

    else:  
        best_score = 999
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"  # humain joue
                score = minimax(board, True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score

def ai_move(board):
    best_score = -999
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i

    return best_move

# -------------------------------
#  PROGRAMME PRINCIPAL
# -------------------------------

def main():
    board = create_board()
    print("Vous êtes X. L'IA est O.")
    display_board(board)

    while True:
        # Tour humain
        hmove = human_move(board)
        board[hmove] = "X"
        display_board(board)

        result = check_winner(board)
        if result == "X":
            print("Vous avez gagné ! ")
            break
        elif result == "Draw":
            print("Match nul.")
            break

        # Tour IA
        print("IA réfléchit...")
        amove = ai_move(board)
        board[amove] = "O"
        display_board(board)

        result = check_winner(board)
        if result == "O":
            print("L'IA a gagné ! ")
            break
        elif result == "Draw":
            print("Match nul.")
            break

if __name__ == "__main__":
    main()
