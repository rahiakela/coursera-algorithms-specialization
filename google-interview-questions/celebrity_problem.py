# Max # of persons in the party
N = 8

# Person with 2 is celebrity
MATRIX1 = [
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 1, 0]
]

MATRIX2 = [
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0]
]


def know(a, b):
    return MATRIX2[a][b]


def find_celebrity(n):
    # The graph needs not be constructed as the edges can be found by using knows function

    # degree array
    indegree = [0 for i in range(n)]
    outdegree = [0 for i in range(n)]

    # Query for all edges
    for i in range(n):
        for j in range(n):
            x = know(i, j)
            # Set the degrees
            outdegree[i] += x
            indegree[j] += x
    # Find a person with indegree n-1 and out degree 0
    for i in range(n):
        if indegree[i] == n - 1 and outdegree[i] == 0:
            return i
    return -1


def find_celebrity_recursive(n):
    """
    Returns -1 if celebrity is not present. If present, returns id (value from 0 to n-1).
    """

    # Base case
    if n == 1:
        return n - 1

    # Find the celebrity with n-1 persons
    id_ = find_celebrity_recursive(n - 1)

    # If there are no celebrities
    if id == -1:
        return n - 1
    elif know(id_, n - 1) and not (know(n - 1, id_)):  # If the celebrity knows the nth person
        return n - 1
    elif know(n - 1, id_) and not know(id_, n - 1):  # If the nth person knows the celebrity then return the id
        return id_

    # If there is no celebrity
    return -1


def celebrity(n):
    """
    Returns -1 if celebrity is not present. If present,returns id (value from 0 to n-1).
    a wrapper over findCelebrity
    """
    # Find the celebrity
    id_ = find_celebrity_recursive(n)

    # Check if the celebrity found is really the celebrity
    if id_ == -1:
        return id_
    else:
        c1, c2 = 0, 0

    # Check the id is really the celebrity
    for i in range(n):
        if i != id_:
            c1 += know(id_, i)
            c2 += know(i, id_)

    # If the person is known to everyone.
    if c1 == 0 and c2 == n - 1:
        return id_

    return -1


if __name__ == '__main__':
    n = 4
    id_ = find_celebrity(n)
    if id_ == -1:
        print("No celebrity")
    else:
        print("Celebrity ID", id_)

