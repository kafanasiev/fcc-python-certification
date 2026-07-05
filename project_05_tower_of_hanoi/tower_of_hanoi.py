def hanoi_solver(disks_num: int):
    rod_1 = []
    rod_2 = []
    rod_3 = []
    for i in range (disks_num, 0, -1):
        rod_1.append(i)
    moves = []
    moves.append(f'{rod_1} {rod_2} {rod_3}')
    def add_move():
        moves.append(f'{rod_1} {rod_2} {rod_3}')
    def move(n, fr, to, spare):
        if n == 1:
            t = fr.pop()
            to.append(t)
            add_move()
            return
        else:
            move(n-1,fr, spare, to)
            move(1, fr, to, spare)
            move(n-1, spare, to ,fr)

    move(disks_num, rod_1, rod_3, rod_2)
    return "\n".join(moves)

print(hanoi_solver(5))


       

   


