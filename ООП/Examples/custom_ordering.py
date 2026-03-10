class Driver:
    def __init__(self, name, time):
        self.name = name
        self.time = time
        self.total = sum(time)

    def __lt__(self, other):
        return self.total < other.total


m, n = [int(x) for x in input().split()]
array = []
for i in range(m):
    name = input()
    time = [int(x) for x in input().split()]
    array.append(Driver(name,time))

print(min(array).name)