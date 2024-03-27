# Hubert Jackowski
# Zadanie 1
def wszystkie_perm(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    result = []
    for i in range(len(lst)):
        m = lst[i]
        tempLst = lst[:i] + lst[i + 1:]
        for p in wszystkie_perm(tempLst):
            result.append([m] + p)
    return result
print(wszystkie_perm(["Ala"]))
print(wszystkie_perm(["Ala", "Cezary"]))
print(wszystkie_perm(["Ala", "Cezary", "Monika"]))
print(wszystkie_perm(["Ala", "Cezary", "Monika", "Dawid"]))

# Zadanie 2
def saper():
    row = int(input("Podaj ilość wierszy: "))
    col = int(input("Podaj ilość kolumn: "))

    board = []
    for i in range(row):
        for j in range(col):
            board.append(input(f"Podaj element (* lub .) na indexie [{i}, {j}]: "))


    for i in range(row * col):
        if(board[i] == "*"):
            continue
        board[i] = 0

        if((i + 1) % col != 0):
            if(board[i + 1] == "*"):
                board[i] += 1

        if(i % col != 0):
            if(board[i - 1] == "*"):
                board[i] += 1

        if(0 <= i - row and (i-row)//col != i//col):
            if(board[i - col] == "*"):
                board[i] += 1

        if(0 <= i - row - 1 and (i-row - 1)//col != i//col):
            if(board[i - col - 1] == "*"):
                board[i] += 1

        if(i - row + 1 >= 0 and (i-row+1)//col != i//col):
            if(board[i - col + 1] == "*"):
                board[i] += 1

        if(i + row < row * col and (i+row)//col != i//col):
            if (board[i + col] == "*"):
                board[i] += 1

        if(i + row - 1 < row * col and (i+row-1)//col != i//col):
            if (board[i + col - 1] == "*"):
                board[i] += 1

        if(i + row + 1 < row * col and (i+row+1)//col != i//col):
            if (board[i + col + 1] == "*"):
                board[i] += 1

    for i in range(row*col):
        if(i % col==0 and i > 0):
            print()
        print(board[i], end=" ")

saper()