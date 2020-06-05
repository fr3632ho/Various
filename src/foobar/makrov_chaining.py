from fractions import gcd, Fraction

'''
Subtracts matrix A with B
'''
def sub(A, B):
    # Check fo correct dimensions
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise Exception("Wrong dimensions!!")

    s = []
    for i in range(len(A)):
        s_row = []
        for j in range(len(B)):
            s_row.append(A[i][j] - B[i][j])
        s.append(s_row)
    return s

'''
Returns an identity matrix of dimension dim
'''
def identity(dim):
    return [[1 if i==j else 0 for i in range(dim)] for j in range(dim)]

'''
Matrix multiplication (A * B)
'''
def mul(A, B):
    # Check for correct dimensions
    if len(A[0]) != len(B):
        return -1

    m = []
    rows, cols, iter = len(A), len(B[0]), len(A[0])

    for r in range(rows):
        m_row = []
        for c in range(cols):
            sum = 0
            for i in range(iter):
                sum += A[r][i]*B[i][c]
            m_row.append(sum)
        m.append(m_row)

    return m

'''
Transpose of matrix m
'''
def transpose(m):
    return map(list,zip(*m))

'''
Get minor matrices
'''
def minor_matrix(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

'''
Calculate the determinant of a nxn matrix
'''
def determinant(m):
    # if dimension is 2x2
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    det = 0
    for col in range(len(m)):
        det += ((-1)**col) * m[0][col] * determinant(minor_matrix(m, 0, col))

    return det

'''
Inverts a matrix of fractions
'''
def inv(m):
    det = determinant(m)
    if det == 0:
        raise Exception("Cannot get inverse of matrix with zero determinant")

    # 2x2 matrix
    if len(m) == 2:
        return [[m[1][1]/det, (-1)*m[0][1]/det ], [(-1)*m[1][0]/det, m[0][0]/det]]

    N = len(m)
    cofactor = []
    for r in range(N): # Construct cofactor matrix
        c_row = []
        for c in range(N): # Calculate determinat for every minor matrix
            minor = minor_matrix(m,r,c)
            c_row.append(((-1)**(r+c)) * determinant(minor))

        cofactor.append(c_row)

    adjugate = transpose(cofactor) # Adjugate matrix

    for row in range(len(adjugate)): # Divide each element with the determinant
        for col in range(len(adjugate)):
            adjugate[row][col] = adjugate[row][col]/det

    return adjugate

'''
Convert matrix of ints into matrix represented with fractions
'''
def into_fractions(m):
    n = []
    for r in range(len(m)):
        nRow = []
        s = sum(m[r])
        if s == 0:
            nRow = m[r]
        else:
            for c in m[r]:
                nRow.append(Fraction(c, s))

        n.append(nRow)

    return n

'''
Count terminal states
'''
def transient_count(m):
    return len(m) - len([ i for i in range(len(m)) if sum(m[i]) == 0])

def create_QR(matrix, t): # Q, R
    return [row[:t] for row in matrix[:t]], [row[t:] for row in matrix[:t]]

'''
Swap column i & j
'''
def swap(arr, i, j):
    rows, cols = len(arr), len(arr[0])
    temp = []
    for r1 in range(rows):
        temp.append(arr[r1][j])
        arr[r1][j] = arr[r1][i]

    for r2 in range(rows):
        arr[r2][i] = temp[r2]

'''
sort transition matrix
'''
def sort(m):
    non_empty, n = [], []
    empty = []
    for num,i in enumerate(m):
        if sum(i) == 0:
            empty.append(i)
        else:
            n.append(i)
            non_empty.append((num,i))

    # Swap columns in the non-empty list
    counter = 0
    for num,row in non_empty:
        if counter != num:
            z = num
            while z != counter:
                swap(n, z-1, z)
                z -= 1

        counter += 1

    return n + empty

def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b

    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1

    return lcm

def get_lcm(arr):
    return reduce(lambda x, y: lcm(x, y), arr)

'''
compute least common multiple (LCM) for the denominators
'''
def compute_lcm(arr):
    d_arr = [d.denominator for d in arr]
    lcm = d_arr[0]
    for i in d_arr[1:]:
        lcm = (lcm*i)/gcd(lcm,i)
    return lcm

'''
Alter from fractions to ints with LCM last
'''
def format_result(state):
    lcm, res = compute_lcm(state), [f.numerator for f in state]
    res.append(lcm)

    for i in range(len(state)):
        cur = state[i].denominator
        if cur < lcm:
            res[i] = res[i] * (lcm / cur)
    return res


def solution(m):
    # if ore zero is terminal
    transient = transient_count(m)
    if sum(m[0]) == 0:
        terminals = [0 for i in range(len(m) - transient - 1)]
        res = [1] + terminals + [1]
        return res

    matrix = sort(m)
    matrix = into_fractions(matrix)

    # Get Q & R matrices
    Q, R = create_QR(matrix, transient)

    # Calculate F = (I - Q)^(-1)
    F = inv(sub(identity(transient), Q))

    # Calculate B = F*R
    b = mul(F, R)
    # Take state 0
    b0 = b[0]
    return format_result(b0)

# [7, 6, 8, 21] is the expected solution
print solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])

# [0, 3, 2, 9, 14] is the expected solution
print solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
