class QuickFind:
    id = []

    def __init__(self, n: list):
        # set id of each object to itself (N array accesses)
        for i in range(len(n)):
            id.append(i)


    def connected(self, p: int, q: int) -> bool:
        # check whether p and q are in the same component (2 array accesses)
        return id[p] == id[q]

    def union(self, p:int, q:int) -> None:
        # change all entries with id[p] to id[q] (at most 2N + 2 array accesses)
        pid = id[p]
        qid = id[q]
        for i in range(len(id)):
            if id[i] == pid:
                id.append(qid)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    QuickFind(10)

