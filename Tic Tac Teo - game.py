def display(board):
    count1: int = 0
    for i, x in enumerate(board):
        if i == 0 or i == 3 or i == 6:
            print()
            print("|   ||   ||   |")
        if i == 3 or i == 6:
            print("---------------")
        if i == 3 or i == 6:
            print("|   ||   ||   |")
        print(f"| {x} |", end="")
        count1 += 1
    print()
    print("|   ||   ||   |")
def entry(lis):
    position = [1,2,3,4,5,6,7,8,9]
    inp = input("Enter the position from 1~9:")
    ca = True
    while ca:
        try:
            if int(inp) not in position and lis[int(inp)-1] == " ":
                inp = input("Enter the position from 1~9:")
        except:
            print("re-enter")
            inp = input("Enter the position from 1~9:")
            continue
        else :
            num = (int(inp))
            if lis[num - 1] not in ["X", "O"]:
                return num
            else:
                print("re-enter")
                inp = input("Enter the position from 1~9:")
                continue
def insert(li , pos,count,mark):
    opt = ["X","O"]
    if count == 0 and li[pos-1] not in opt:
        li[pos-1] = "X"
    elif count == 1 and li[pos-1] not in opt :
        li[pos-1] = "O"
    else:
        return li
    mark+=1
    return li,mark
def checkwin(g):
    opt = ["X", "O"]
    re = True
    count = 0
    a = 0
    b = 1
    c = 2
    for i in range(0, 2):
        if (g[a] == g[b] == g[c]) and (g[a] in opt):
            return re, g[a]
        else:
            a += 3
            b += 3
            c += 3
    a = 0
    b = 3
    c = 6
    for i in range(0, 2):
        if (g[a] == g[b] == g[c]) and (g[a] in opt):
            return re, g[a]
        else:
            a += 1
            b += 1
            c += 1
    if ((g[0] == g[4] == g[8])or (g[2] == g[4] == g[6])) and (g[4] in opt) :
        return re, g[4]
    return False,0


gamelist=[" "," "," "," "," "," "," "," "," "]
count = 0
index = 0
mark = 0
while (True):
    if mark >=9:
        display(gamelist)
        print("Both are fail")
        break
    if(count == 0):
        display(gamelist)
        entry1 = entry(gamelist)
        gamelist, mark = insert(gamelist, entry1, count, mark)
        c, y = checkwin(gamelist)
        if c:
            display(gamelist)
            print(f"The winner is {y}")
            exit(1)
        count = 1
        index +=1
    elif(count == 1):
        display(gamelist)
        entry1 = entry(gamelist)
        gamelist, mark = insert(gamelist, entry1, count, mark)
        c,y = checkwin(gamelist)
        if c:
            display(gamelist)
            print(f"The winner is {y}")
            exit(1)
        count = 0
        index += 1

