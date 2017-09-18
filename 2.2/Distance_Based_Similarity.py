import math

def EuclideanDistance(X,Y):
    EU = 0
    if len(X) == len(Y):
        for i in range(len(X)):
            EU = EU + (X[i] - Y[i])**2
        return math.sqrt(EU)
    else:
        return -1

def AbsoluteDifference(X,Y):
    AD = 0
    if len(X) == len(Y):
        for i in range(len(X)):
            AD = AD + abs(X[i] - Y[i])
        return math.sqrt(AD)
    else:
        return -1

def MaximumDistanceMetric(X,Y):
    D_max = -99999
    if len(X) == len(Y):
        for i in range(len(X)):
            if D_max < abs(X[i]- Y[i]):
                D_max = abs(X[i]- Y[i])
        return D_max
    else:
        return -1

if __name__ == '__main__':
    x = [1, 4, -1, 5, 100, 0.9]
    y = [3, -1, 0, 2.7, 0, 9.5]

    print(EuclideanDistance(x,y))
    print(AbsoluteDifference(x,y))
    print(MaximumDistanceMetric(x,y))

