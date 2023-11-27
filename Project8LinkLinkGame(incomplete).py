#the real thing
import curses

choosing = True

workingList0 = [ 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 5, 1, 0, 0, 0, 0], 
[0, 0, 0, 0, 4, 3, 0, 0, 0, 0], 
[0, 0, 0, 5, 2, 1, 2, 0, 0, 0], 
[0, 0, 0, 0, 3, 4, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
] 


def hcontrolFunc(Key):
    if Key == 454:
        return 1
    elif Key == 452:
        return -1
    else:
        return 0
    
def vcontrolFunc(Key):
    if Key == 450:
        return -1
    elif Key == 456:
        return 1
    else:
        return 0
    

def isClear(ax, ay, bx, by):
    if workingList0[ay][ax] != workingList0[by][bx]:
        return False
    elif ax == bx and ay == by:
        return False
    if ay == by and ax != bx:
        for i in range(bx-ax-1):
            if workingList0[ay][ax+i] != 0:
                break
            else:
                return True
    if ax == bx and ay != by:
        for i in range(by-ay-1):
            if workingList0[ay+i][ax] != 0:
                break
            else:
                return True
    else:
        for i in range(10-ay):
            for j in range(10-ay-i):
                if workingList0[ay+1+j][ax] != 0:
                    break
                else:
                    for k in range(bx-ax):
                        if workingList0[ay+1+j][ax+k] != 0:
                            break
                        else:
                            for l in range(10-ay):
                                for m in range(10-ay-l):
                                    if workingList0[by+1+m][bx] != 0:
                                        break
                                    else:
                                        return True
        for i in range(ay):
            for j in range(ay-i):
                if workingList0[ay-1-j][ax] != 0:
                    break
                else:
                    for k in range(bx-ax):
                        if workingList0[ay+1+j][ax+k] != 0:
                            break
                        else:
                            for l in range(ay):
                                for m in range(ay-l):
                                    if workingList0[by-1-m][bx] != 0:
                                        break
                                    else:
                                        return True
        for i in range(10-ax):
            for j in range(10-ax-i):
                if workingList0[ay][ax+1+j] != 0:
                    break
                else:
                    for k in range(by-ay):
                        if workingList0[ay+k][ax+1+j] != 0:
                            break
                        else:
                            for l in range(10-ax):
                                for m in range(10-ax-l):
                                    if workingList0[by][bx+1+m] != 0:
                                        break
                                    else:
                                        return True
        for i in range(ax):
            for j in range(ax-i):
                if workingList0[ay][ax-1-j] != 0:
                    break
                else:
                    for k in range(by-ay):
                        if workingList0[ay+k][ax+1+j] != 0:
                            break
                        else:
                            for l in range(ax):
                                for m in range(ax-l):
                                    if workingList0[by][bx-1-m] != 0:
                                        break
                                    else:
                                        return True
                    
            

                    



def visualFunc(stdscr):
    x = 0
    y = 0
    chosen = False
    xPosit0 = 0
    yPosit0 = 0
    xPosit1 = 0
    yPosit1 = 0
    Check = 0
    Ok = False


    for i in range(10):
        for j in range(10):
            stdscr.addstr(j, i * 2, str(workingList0[j][i]))
            stdscr.refresh()

    for i in range(1000):

        
        stdscr.addstr(y, x* 2, str(workingList0[y][x]), curses.A_REVERSE)
        stdscr.refresh()
        arrowKey = stdscr.getch()
        
        if arrowKey == 32:
            if chosen == False:
                xPosit0 = x
                yPosit0 = y
                chosen = True
                Check += 1

            else:
                xPosit1 = x
                yPosit1 = y
                chosen = False

        stdscr.addstr(y, x* 2, str(workingList0[y][x]))
        stdscr.refresh()
        #stdscr.addstr(11, 0, str(arrowKey), curses.A_REVERSE)
        x = x + hcontrolFunc(arrowKey)
        y = y + vcontrolFunc(arrowKey)

        if chosen == True:
            stdscr.addstr(yPosit0, xPosit0* 2, str(workingList0[yPosit0][xPosit0]), curses.A_UNDERLINE)
            stdscr.refresh()
        else:
            stdscr.addstr(yPosit0, xPosit0* 2, str(workingList0[yPosit0][xPosit0]))
            stdscr.refresh()
        
        if Check >= 2:
            if xPosit0 >= xPosit1:
                Ok = isClear(xPosit1, yPosit1, xPosit0, yPosit0)
            else:
                Ok = isClear(xPosit0, yPosit0, xPosit1, yPosit1)
            Check == 0

        if Ok == True:
            workingList0[yPosit0][xPosit0] = 0
            workingList0[yPosit1][xPosit0] = 0

    stdscr.getch()




            
    
    
curses.wrapper(visualFunc)
