A = int(input())
B = int(input())


def euclidAlgo(A, B):
    if (B == 0):
        return A
    else:
        return euclidAlgo(B, A % B)

print(euclidAlgo(A, B))
