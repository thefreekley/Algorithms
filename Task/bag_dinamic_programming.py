def find_min(A, K):
    INF = 10 ** 10
    F = [INF] * (K + 1)
    F[0] = 0
    for k in range(1, K + 1):

        for i in range(len(A)):

            if k - A[i] >= 0 and F[k - A[i]] < F[k]:
                F[k] = F[k - A[i]]
                print(A[i],F[k],F[k - A[i]],F)
        F[k] += 1

    Ans = []
    k = K

    while k != 0:
        for i in range(len(A)):
            if k - A[i] >= 0 and F[k] == F[k - A[i]] + 1:
                Ans.append(A[i])
                k -= A[i]
    return Ans

list = [1,4,5,3]

print(find_min(list,10))



