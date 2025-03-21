def tic_tac_toe():
    B, P = [["-"]*3 for _ in range(3)], "XO"
    W = lambda p: any(all(c == p for c in r) for r in B) or any(all(B[r][c] == p for r in range(3)) for c in range(3)) or all(B[i][i] == p for i in range(3)) or all(B[i][2-i] == p for i in range(3))
    for t in range(9):
        print("\n".join(" ".join(r) for r in B))
        r, c = map(int, input(f"Player {P[t%2]}, enter row and col: ").split())
        if B[r][c] == "-":  
            B[r][c] = P[t%2]
            if W(P[t%2]): return print("\n".join(" ".join(r) for r in B)), print(f"Player {P[t%2]} wins!")
    print("\n".join(" ".join(r) for r in B)), print("It's a draw!")

tic_tac_toe()

#output
- - -
- - -
- - -
Player X, enter row and col: 1 1
- - -
- X -
- - -
Player O, enter row and col: 1 0
- - -
O X -
- - -
Player X, enter row and col: 0 2
- - X
O X -
- - -
Player O, enter row and col: 2 1
- - X
O X -
- O -
Player X, enter row and col: 2 0
- - X
O X -
X O -
Player X wins!
