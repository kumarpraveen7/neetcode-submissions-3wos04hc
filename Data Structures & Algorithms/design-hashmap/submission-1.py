class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.l = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        x = key % self.size

        for pair in self.l[x]:
            if pair[0] == key:
                pair[1] = value
                return

        self.l[x].append([key, value])

    def get(self, key: int) -> int:
        x = key % self.size

        for pair in self.l[x]:
            if pair[0] == key:
                return pair[1]

        return -1

    def remove(self, key: int) -> None:
        x = key % self.size

        for i, pair in enumerate(self.l[x]):
            if pair[0] == key:
                self.l[x].pop(i)
                return