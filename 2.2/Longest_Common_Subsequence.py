
import pandas as pd
import matplotlib.pyplot as plt

# Discovering Similar Multidimentional Trajectories を参考に.
# LCSS値が大きい程似ている(近い)
def LCSS(X,Y):
    cum_dist = [[0 for i in range(len(X))] for j in range(len(Y)) ]
    for i in range(len(X)):
        for j in range(len(Y)):
            if ED(X[i],Y[j]) < 2.5:
                cum_dist[i][j] = 1 + (cum_dist[i - 1][j - 1])
            else:
                cum_dist[i][j] = max([cum_dist[i - 1][j], cum_dist[i][j - 1]])

    return cum_dist[-1][-1]

def ED(x,y):
    return abs(x - y)


if __name__ == '__main__':
    data = pd.read_csv("temp.csv", delimiter=',', encoding= "shift-jis")
    timeA = data['気温(℃)'][0:24]
    timeB = data['気温(℃)'][24:48].reset_index(drop=True)
    timeC = data['気温(℃)'][48:72].reset_index(drop=True)
    timeD = data['気温(℃)'][72:96].reset_index(drop=True)

    print("AB: "+str(LCSS(timeA,timeB)))
    print("CB: "+str(LCSS(timeC,timeB)))
    print("DB: "+str(LCSS(timeD,timeB)))

    plt.plot(timeA, label="A")
    plt.plot(timeB, label="B")
    plt.plot(timeC, label="C")
    plt.plot(timeD, label="D")
    plt.legend()
    plt.show()
