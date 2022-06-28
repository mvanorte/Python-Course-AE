#padding
import numpy as np
import pygame as pg
import os
# nx=10
# ny=10
# board=np.zeros((ny, nx))
#board[1:4, 1:4]=[[0, 1, 0], [0, 0, 1], [1, 1, 1]]


#import numpy as np
#import pygame as pg

xlist=[]
ylist=[]
coordinates=[]
f = open(r"C:\Users\tocas\OneDrive\Documents\Bsc1\Q4\Python\b52bomber_106.lif", "r")
lines=f.readlines()
f.close()


#print(lines)

for line in lines:
    line=line.strip("\n")
    coordinates.append(line.split(" "))

coordinates=coordinates[1:]
#print(coordinates)
for i in range(len(coordinates)):
    xlist.append(int(coordinates[i][0]))
    ylist.append(int(coordinates[i][1]))


xmax=max(xlist, key=abs)
ymax=max(ylist, key=abs)

if abs(xmax)>=abs(ymax):
    nx=abs(xmax)+1
    ny=abs(xmax)+1
elif abs(xmax)<abs(ymax):
    nx=abs(ymax)+1
    ny=abs(ymax)+1

if nx<10:
    nx=10
    ny=10
    

board=np.zeros((ny, nx))
# print(nx)
# print(ny)
# print(board)

for j in range(len(ylist)):
    a=int(ylist[j]) 
    b=int(xlist[j])
    board[b, a]=1
#print(board)
#board=np.pad(board, (1, 1), constant_values=0)
#print(board)

# print(board1)
# print(board2)
# print(board3)
# print(board4)
# print(board5)
# print(board6)
# print(board7)
# print(board8)
def update_cells(cells_in):
    cells=np.pad(cells_in, (1, 1), constant_values=0)
    cells_out=np.copy(cells)
    for y in range(1,ny+1):
        for x in range(1,nx+1):
            
            cell=cells[y,x]
            board1=np.pad(board, ((0, 2), (1,1)), constant_values=0) #1
            board2=np.pad(board, ((0, 2),(0,2)), constant_values=0 ) #2
            board3=np.pad(board, ((1,1),(0,2)), constant_values=0 )  #3
            board4=np.pad(board, ((2, 0),(0,2)), constant_values=0 ) #4
            board5=np.pad(board, ((2, 0),(1,1)), constant_values=0 ) #5
            board6=np.pad(board, ((2, 0),(2,0)), constant_values=0 ) #6
            board7=np.pad(board, ((1, 1),(2,0)), constant_values=0 ) #7
            board8=np.pad(board, ((0, 2),(2,0)), constant_values=0 ) #8
            finalboard=board1+board2+board3+board4+board5+board6+board7+board8
            #print(finalboard)
            neighbour_sum=finalboard[y,x]
            #print("y is: ",y)
            #print("x is: ", x)
            #print("sum is: ", neighbour_sum)
            if cell==1:
                if neighbour_sum<2:
                    cells_out[y, x]=0
                elif neighbour_sum in [2, 3]:
                    cells_out[y, x]=1
                elif neighbour_sum>3:
                    cells_out[y, x]=0
            elif cell==0:
                if neighbour_sum==3:
                    cells_out[y, x]=1
                else:
                    cells_out[y, x]=0
            #print("out goes: ",cells_out)
    return cells_out[1:-1, 1:-1]
board=update_cells(board)
#print(board)
scr=pg.display.set_mode((480, 480))
#scrrect=scr.get_rect()
black=(0, 0, 0)
pg.display.get_surface().fill(black)
pg.init()

white=(255, 255, 255)
#pg.event.pump()
#keys=pg.key.get_pressed()
running= True

while running:
    
    for event in pg.event.get():
        if (event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE)):
            pg.quit()
            #sys.exit()
            running=False

    #pg.draw.rect(scr, black, scr)
    ygrid=0 
    #print(board)
    for y in range(ny):
        
        xgrid=0
        for x in range(nx):
            
            #print(xgrid)
            #print(board[y,x], end=" ")
            if board[y, x]==1:
                pg.draw.rect(scr,white, [ygrid, xgrid, 480//nx, 480//ny] )
                #pg.display.update()
                #print(board)
            else:
                pg.draw.rect(scr,black, [ygrid, xgrid, 480//nx, 480//ny] )
                #pg.display.update()
    
            xgrid=xgrid+480//ny
        ygrid=ygrid+480//nx
        
    board=update_cells(board)
    pg.display.update()
    pg.time.wait(250)

#board=update_cells(board)
    #if keys[pg.K_ESCAPE]:
        #running=False
    


pg.quit()