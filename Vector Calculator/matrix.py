A = [[1,2,3],
     [2,3,3],
     [1,2,5]]

B = [[1,2,3,5],
     [2,3,3,5],
     [1,2,5,1]]

I = [ [0 for i in range(4) ] for j in range(4) ]

# print I // [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

def shape(M):
    r=len(M)
    c=len(M[0])
    return r,c

# print shape(I) // (4, 4)
# print shape(I)[0] // 4
print shape(B)
def matxRound(M, decPts=4):
    for i in range(shape(M)[0]):
        for j in range(shape(M)[1]):
            M[i][j]=round(M[1][j], decPts)

# matxRound(I)
# print I // [[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]]

def transpose(M):
    N=[[M[i][j] for i in range(shape(M)[0])] for j in range(shape(M)[1])]
    return N
    # W =  [ [ 0 for i in range(shape(M)[0]) ] for j in range(shape(M)[1]) ]
    # for i in range(shape(M)[0]):
    #     for j in range(shape(M)[1]):
    #         W[j][i]=M[i][j]
    # return W

# print transpose(B)

def matxMultiply(A, B):
    N =  [ [ 0 for i in range(shape(B)[1]) ] for j in range(shape(A)[0]) ]
    if shape(A)[1]==shape(B)[0]: #如果 A 的列与 B 的行数量不等，则不能相乘
        k=shape(A)[1]
        for ai in range(shape(A)[0]): #从 A 的第一行开始遍历（ai 每走一步，得一行数）
            for bj in range(shape(B)[1]): #从 B 的第一列开始遍历（bj 每走一步，得一个数）
                for kk in range(k): #从 A 的第一行的左边第一个/以及从 B 的第一列的上边第一个开始算起（kk 每走一步，还得不到一个数，走完一轮才得一个数）
                    N[ai][bj]+=A[ai][kk]*B[kk][bj]
        return N
    else:
        return None

# print matxMultiply(A,B)
