from turtle import *
from math import *
from time import *
from copy import deepcopy
sc=Screen()
sc.tracer(0,0)
ht()

def y3dr(listxyz,rotateAnger=1):
    x=listxyz[0]
    y=listxyz[1]
    z=listxyz[2]
    xn=x*cos(radians(rotateAnger))+z*sin(radians(rotateAnger))
    zn=-x*sin(radians(rotateAnger))+z*cos(radians(rotateAnger))
    return xn,y,zn
def x3dr(listxyz,rotateAnger=1):
    x=listxyz[0]
    y=listxyz[1]
    z=listxyz[2]
    yn=y*cos(radians(rotateAnger))-z*sin(radians(rotateAnger))
    zn=y*sin(radians(rotateAnger))+z*cos(radians(rotateAnger))
    return x,yn,zn
def z3dr(listxyz,rotateAnger=1):
    x=listxyz[0]
    y=listxyz[1]
    z=listxyz[2]
    xn=x*cos(radians(rotateAnger))+y*sin(radians(rotateAnger))
    yn=-x*sin(radians(rotateAnger))+y*cos(radians(rotateAnger))
    return xn,yn,z

def xy2d(listxyz,pos=(0,0,0)):
    #x2d=listxyz[0]-(listxyz[2]*cos(radians(45)))
    #y2d=listxyz[1]-(listxyz[2]*sin(radians(45)))
    
    #x2d=(listxyz[0]-listxyz[2])/(2**0.5)
    #y2d=(listxyz[0]+(listxyz[1]*2)+listxyz[2])/(6**0.5)
    #return -x2d,-y2d
    viewer_pos=0,0,1000
    camera_pos=0-pos[0],0-pos[1],1000+pos[2]
    a, b, c = viewer_pos
    d, e, f = camera_pos
    x, y, z = listxyz
    x, y, z = x - d, y - e, z - f
    t4 = c/z
    return (a - t4*x, b - t4*y)
shapetype={0:[[[-50,-50,-50],[50,-50,-50]],
     [[50,-50,-50],[50,50,-50]],
     [[50,50,-50],[-50,50,-50]],
     [[-50,50,-50],[-50,-50,-50]],
     [[-50,-50,50],[50,-50,50]],
     [[50,-50,50],[50,50,50]],
     [[50,50,50],[-50,50,50]],
     [[-50,50,50],[-50,-50,50]],
     [[-50,-50,-50],[-50,-50,50]],
     [[50,-50,-50],[50,-50,50]],
     [[50,50,-50],[50,50,50]],
     [[-50,50,-50],[-50,50,50]]],
           1:[
    [[100, 100, -100], [0, -200, 0]],
    [[-100, 100, -100], [0, -200, 0]],
    [[-100, 100, 100], [0, -200, 0]],
    [[100, 100, 100], [0, -200, 0]],
    [[-100, 100, -100], [100, 100, -100]],
    [[-100, 100, -100], [-100, 100, 100]],
    [[-100, 100, 100], [100, 100, 100]],
    [[100, 100, -100], [100, 100, 100]]]}

def shape3dr():
    global rotateAnger
    global LRUD
    global shapelist
    global turtlelist
    for T in range(len(shapelist)):
        turtlelist[T].clear()
    for T in range(len(shapelist)):
        shape3d(turtlelist[T],shapelist[T][0],shapelist[T][1])
        for c in shapelist[T][0]:
            c[0]=eval(LRUD)(c[0],rotateAnger)
            c[1]=eval(LRUD)(c[1],rotateAnger)
    #sleep(0.01)
    sc.update()
def shape3d(turtle,shapelist,pos):
    for c in range(len(shapelist)):
        turtle.penup()
        turtle.goto(xy2d(shapelist[c][0],pos))
        turtle.pendown()
        turtle.goto(xy2d(shapelist[c][1],pos))
        
#shape3dr(lines,(-100,100,100))

def maomir():
    global STOP
    global rotateAnger
    global shapelist
    global turtlelist
    global curvelist
    color("red")
    for T in range(len(curvelist)):
        turtlelist[len(shapelist)+T].clear()
    for T in range(len(curvelist)):
        t=0
        turtlelist[len(shapelist)+T].penup()
        turtlelist[len(shapelist)+T].goto(xy2d(curvelist[T][0][0],curvelist[T][1]))
        turtlelist[len(shapelist)+T].pendown()
            
        for k in range(curvelist[T][2]):
            maomi(turtlelist[len(shapelist)+T],curvelist[T][0],curvelist[T][1])
            for c in range(len(curvelist[T][0])):
                curvelist[T][0][c]=y3dr(curvelist[T][0][c],360/curvelist[T][2])
        for c in range(len(curvelist[T][0])):
            curvelist[T][0][c]=y3dr(curvelist[T][0][c],rotateAnger)
    #sleep(0.01)
    sc.update()
        
def maomi(turtle,curvelist,pos):
    t=0
    turtle.penup()
    turtle.goto(xy2d(curvelist[0],pos))
    turtle.pendown()
    turtle.color("red")
    for i in range(100):
        t+=0.01
        cposd=curvelist.copy()
        for v in range(len(curvelist)-1):
            b=[]
            for c in range(len(cposd)-1):
                qx=((cposd[c+1][0]-cposd[c][0])*t)+cposd[c][0]
                qy=((cposd[c+1][1]-cposd[c][1])*t)+cposd[c][1]
                qz=((cposd[c+1][2]-cposd[c][2])*t)+cposd[c][2]

                b.append([qx,qy,qz])
            cposd=b.copy()
        turtle.goto(xy2d([qx,qy,qz],pos))
#maomi(5)
def appendposd(event):
    turtlelist[len(turtlelist)-1].clear()
    x=sc.cv.canvasx(event.x)
    y=-sc.cv.canvasy(event.y)
    posd.append([x,y,0])

    turtlelist[len(turtlelist)-1].color("black")
    turtlelist[len(turtlelist)-1].penup()
    turtlelist[len(turtlelist)-1].goto(xy2d(posd[0]))
    turtlelist[len(turtlelist)-1].pendown()
    for c in range(len(posd)-1):
        turtlelist[len(turtlelist)-1].goto(xy2d(posd[c+1]))
    turtlelist[len(turtlelist)-1].penup()
    turtlelist[len(turtlelist)-1].goto(xy2d(posd[0]))
    turtlelist[len(turtlelist)-1].pendown()
    if len(posd)<=1:
        pass
    else:
        maomi(turtlelist[len(turtlelist)-1],posd,(0,0,0))
    sc.update()

def cubeappendposd(event):
    global shapelist
    global turtlelist
    global CCS
    global STOP
    global CS
    turtlelist[len(turtlelist)-1].clear()
    x=sc.cv.canvasx(event.x)
    y=-sc.cv.canvasy(event.y)
    color("black")
    sc.cv.bind('<Button-1>',new_cubeposd)
    sc.cv.unbind('<Motion>')
    STOP=False
    shapelist.append([deepcopy(CS),(x,y,0)])
    shape3d(turtlelist[len(turtlelist)-1],CS,(x,y,0))
    CCS=False
    sc.update()
def new_cubeposd(event):
    global shapelist
    global turtlelist
    global STOP
    turtlelist[len(turtlelist)-1].clear()
    x=sc.cv.canvasx(event.x)-shapelist[len(shapelist)-1][1][0]
    y=-sc.cv.canvasy(event.y)-shapelist[len(shapelist)-1][1][1]
    sc.cv.unbind('<Button-1>')
    for c in shapelist[len(shapelist)-1][0]:
        for v in c:
            v[0]+=x
            v[1]+=y
    STOP=True
    sc.update()
    
def movecubeposd(event):
    global turtlelist
    global CS
    turtlelist[len(turtlelist)-1].clear()
    x=sc.cv.canvasx(event.x)
    y=-sc.cv.canvasy(event.y)
    color("black")
    shape3d(turtlelist[len(turtlelist)-1],CS,(x,y,0))
    sc.update()
    
def curve():
    global turtlelist
    sc.cv.bind('<Button-1>',appendposd)
    sc.cv.bind('<Button-3>',uncurve)
    _=Turtle()
    _.ht()
    _.color("black")
    turtlelist.append(_)
def uncurve(event):
    sc.cv.bind('<Button-1>',curvepos)
    sc.cv.bind('<Motion>',movecurve)
    sc.cv.unbind('<Button-3>')
def movecurve(event):
    x=sc.cv.canvasx(event.x)
    y=-sc.cv.canvasy(event.y)
    turtlelist[len(turtlelist)-1].clear()
    maomi(turtlelist[len(turtlelist)-1],posd,(x,y,0))
def curvepos(event):
    global curvelist
    global posd
    global STOP
    x=sc.cv.canvasx(event.x)
    y=-sc.cv.canvasy(event.y)
    sc.cv.unbind('<Button-1>')
    sc.cv.unbind('<Motion>')
    n=[int(x) for x in input("how many n").split()]
    if len(n)>1:
        if n[1]==0:
            x=0
            y=0
        else:
            pass
    else:
        pass
    curvelist.append([deepcopy(posd),(x,y,0),n[0]])
    posd=[]
    STOP=True
    sc.update()

def cubepos(event):
    global CCS
    global turtlelist
    _=Turtle()
    _.ht()
    _.color("black")
    turtlelist.append(_)
    sc.cv.bind('<Motion>', movecubeposd)
    sc.cv.bind('<Button-1>',cubeappendposd)
    CCS=True

def changeshape(event):
    global CS
    global SP
    global shapetype
    if SP>=len(shapetype)-1:
        SP=0
    else:
        SP+=1
    CS=shapetype[SP]

def reset():
    global STOP
    global posd
    global shapelist
    global curvelist
    global turtlelist
    global CS
    global CCS
    global SP
    global shapetype
    for c in turtlelist:
        c.clear()
    posd=[]
    shapelist=[]
    curvelist=[]
    turtlelist=[]
    CS=shapetype[0]
    CCS=False
    SP=0
    STOP=False

def Left():
    global LRUD
    global rotateAnger
    LRUD="y3dr"
    rotateAnger=1
def Right():
    global LRUD
    global rotateAnger
    LRUD="y3dr"
    rotateAnger=-1
def Up():
    global LRUD
    global rotateAnger
    LRUD="x3dr"
    rotateAnger=1
def Down():
    global LRUD
    global rotateAnger
    LRUD="x3dr"
    rotateAnger=-1

shapelist=[]
curvelist=[]
turtlelist=[]
posd=[[50,-100,0],[50,200,0],[200,200,0],[200,0,0]]
cposd=[]
CS=shapetype[0]
STOP=False
CCS=False
SP=0
LRUD="y3dr"
rotateAnger=1

while 1:
    sc.listen()
    if CCS:
        sc.cv.bind("s",changeshape)
    elif CCS==False:
        sc.cv.bind("s",cubepos)
    if STOP:
        shape3dr()
        maomir()
    sc.onkey(curve,"a")
    sc.onkey(reset,"r")
    sc.onkey(Left,"Left")
    sc.onkey(Right,"Right")
    sc.onkey(Up,"Up")
    sc.onkey(Down,"Down")
    sc.update()
sc.update()



