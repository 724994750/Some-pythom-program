#模拟比赛
from random import random

def printIntro():
    print("这个程序模拟两个选手的比赛")
    print("程序运行需要输入两个选手的能力值（介于0-1之间）")

def getIntro():
    a = eval(input("请输入a选手的能力值（0到1之间）："))
    b = eval(input("请输入b选手的能力值（0到1之间）："))
    z = eval(input("请输入模拟比赛的场次："))
    return a,b,z

def printSummary(winA,winB):
    n = winA+winB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手a获胜{}场！占比{:0.1%}".format(winA,winA/n))
    print("选手b获胜{}场！占比{:0.1%}".format(winB,winB/n))

def gameOver(a,b):
    return a==15 or b ==15 

def simOneGame(probA,probB):
    scoreA,scoreB=0,0
    seving="A"
    while not gameOver(scoreA,scoreB):
        if seving=="A":
            if random() < probA:
                scoreA+=1
            else:
                seving="B"
        else:
            if random() < probB:
                scoreB+=1
            else:
                seving="A"
    return scoreA,scoreB
            
def simNGame(z,probA,probB):
    winA=0
    winB=0
    for i in range(z):
        scoreA,scoreB = simOneGame(probA,probB)
        if scoreA>scoreB:
            winA +=1
        else:
            winB +=1
    return winA,winB
    
def main():
    printIntro()
    a,b,z=getIntro()
    winA,winB = simNGame(z,a,b)
    printSummary(winA,winB)

main()
