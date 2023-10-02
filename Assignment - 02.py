#Assignment -2 Code in Python


def matrix_mul(dim):
    n = len(dim)
    m = [[0] * n for _ in range(n)]
    parenthesization = [[0] * n for _ in range(n)]

    for i in range(1, n):
        m[i][i] = 0

    # length of the matrix multiplication chain
    for chain-len in range(2, n):
        for i in range(1, n - chain-len + 1):
            j = i + chain-len - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                c = m[i][k] + m[k + 1][j] + dim[i - 1][0] * dim[k][1] * dim[j][1]
                if c < m[i][j]:
                    m[i][j] = c
                    parenthesization[i][j] = k

    # obtaining the optimal parenthesization
    def opt_parenthesization(i, j):
        if i == j:
            return f'M{str(i)}'
        else:
            k = parenthesization[i][j]
            lchain = opt_parenthesization(i, k)
            rchain = opt_parenthesization(k + 1, j)
            return f'({l_chain} x {r_chain})'

    opt_parenthesization = opt_parenthesization(1, n - 1) #recursively calling the function.

    return opt_parenthesization, m[1][n - 1]

# Example :
dim = [(2, 3), (3, 4), (4, 2)]
opt_parenthesization, min_scalar_mul = matrix_mul(dim)
print("Optimal Parenthesization:", opt_parenthesization)
print("Minimum Scalar Multiplications:", min_scalar_mul)