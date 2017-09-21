
import pandas as pd
import matplotlib.pyplot as plt

# Information Mining Over Heterogeneous and High-Dimensional Time-Series Data in Clinical Trials Databases を参考に.
# SWC値が小さい程似ている(近い)
def SWC(X,Y):
    cum_dist = [[0 for i in range(len(X))] for j in range(len(Y)) ]
    pt = 0.01
    nt = -1 * pt
    diff_total = 0
    diff = 0
    for i in range(len(X)-1):
        XA = X[i] - X[i+1]
        XB = Y[i] - Y[i+1]
        SA = XA / (abs(X[i]) + abs(X[i+1]))
        SB = XB / (abs(Y[i]) + abs(Y[i+1]))
        if XA > 0:
            if SA < pt:
                if SB < pt:
                    diff = 0
                elif SB > pt:
                    diff = 0.25
                elif SB > nt:
                    diff = 0.5
                elif SB < nt:
                    diff = 0.75
            elif SB > pt:
                if SB < pt:
                    diff = 0.25
                elif SB > pt:
                    diff = 0
                elif SB > nt:
                    diff = 0.75
                elif SB < nt:
                    diff = 1
        elif XA < 0:
            if SA < pt:
                if SB < pt:
                    diff = 0.5
                elif SB > pt:
                    diff = 0.75
                elif SB > nt:
                    diff = 0
                elif SB < nt:
                    diff = 0.25
            elif SB > pt:
                if SB < pt:
                    diff = 0.75
                elif SB > pt:
                    diff = 1
                elif SB > nt:
                    diff = 0.25
                elif SB < nt:
                    diff = 0
        diff_total = diff_total + diff
    return  diff_total

def ED(x,y):
    return abs(x - y)
    #直線距離ではないのでは？

if __name__ == '__main__':
    data = pd.read_csv("temp.csv", delimiter=',', encoding= "shift-jis")
    timeA = data['気温(℃)'][0:24]
    timeB = data['気温(℃)'][24:48].reset_index(drop=True)
    timeC = data['気温(℃)'][48:72].reset_index(drop=True)
    timeD = data['気温(℃)'][72:96].reset_index(drop=True)

    print("AB: "+str(SWC(timeA,timeB)))
    print("CB: "+str(SWC(timeC,timeB)))
    print("DB: "+str(SWC(timeD,timeB)))

    plt.plot(timeA, label="A")
    plt.plot(timeB, label="B")
    plt.plot(timeC, label="C")
    plt.plot(timeD, label="D")
    plt.legend()
    plt.show()
