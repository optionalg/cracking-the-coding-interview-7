class hanoi_towers_with_stacks(object):
    """
    In classic Towers of Hanoi you have three towers and N disks of different sizes
    which can slide onto any tower. The puzzle starts with disks sorted in ascending order
    of size from top to bottom (each disk sits atop an even larger one)
    1. only one disk can be moved at a time
    2. a disk is slid off the top of one tower onto another one
    3. a disk can only be placed on top of a larger disk
    write a program that moves the disks from the top tower to the last using
    stacks
    """

    def __init__(self, size):
        self.size = size
        self.towers = [[], [], []]
        self.towers[0] = [x for x in range(size, 0, -1)]

    def play_hanoi(self):
        print self.towers
        self.moveDisk(self.size, 1, 2, 3)
        print self.towers

    def moveDisk(self, size, fr, helper, to):
        if size == 1:
            disk = self.towers[fr-1].pop()
            self.towers[to-1].append(disk)
        else:
            self.moveDisk(size-1, fr, to, helper)
            self.moveDisk(1, fr, helper, to)
            self.moveDisk(size-1, helper, fr, to)

