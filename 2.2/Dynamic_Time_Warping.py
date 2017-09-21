

import pandas as pd
import matplotlib.pyplot as plt

# DTW値が小さい程似ている(近い)
def DTW(X,Y):
    cum_dist = [[-1 for i in range(len(X))] for j in range(len(Y)) ]
    for i in range(len(X)):
        for j in range(len(Y)):
            if i == 0 and j == 0:
                cum_dist[i][j] = ED(X[i],Y[j])
            elif i == 0 and j >= 1:
                cum_dist[i][j] = ED(X[i],Y[j]) + cum_dist[i][j-1]
            elif i >= 1 and j == 0:
                cum_dist[i][j] = ED(X[i],Y[j]) + cum_dist[i-1][j]
            else:
                cum_dist[i][j] = ED(X[i],Y[j]) + min([cum_dist[i-1][j-1], cum_dist[i-1][j], cum_dist[i][j-1]])
    return cum_dist[-1][-1]

def ED(x,y):
    return abs(x - y)
    # 直線距離ではないのでは？

if __name__ == '__main__':

    data = pd.read_csv("temp.csv", delimiter=',', encoding= "shift-jis")
    timeA = data['気温(℃)'][0:24]
    timeB = data['気温(℃)'][24:48].reset_index(drop=True)
    timeC = data['気温(℃)'][48:72].reset_index(drop=True)
    timeD = data['気温(℃)'][72:96].reset_index(drop=True)

    print("AB: "+str(DTW(timeA,timeB)))
    print("CB: "+str(DTW(timeC,timeB)))
    print("DB: "+str(DTW(timeD,timeB)))

    plt.plot(timeA, label="A")
    plt.plot(timeB, label="B")
    plt.plot(timeC, label="C")
    plt.plot(timeD, label="D")
    plt.legend()
    plt.show()