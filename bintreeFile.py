

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Bintree:
    def __init__(self):
        self.root = None

    def __contains__(self, data):
        return finns(self.root, data)

    def put(self, newvalue):
        self.root = putta(self.root, newvalue)

    def write(self):
        skriv(self.root)


def putta(p, newdata):
    initialroot = p
    while True:
        if p == None:
            p = Node(newdata)
            inserting = False
            return p

        elif newdata < p.data:
            if p.left == None:
                p.left = Node(newdata)
                return initialroot
            else:
                p = p.left

        elif newdata > p.data:
            if p.right == None:
                p.right = Node(newdata)
                return initialroot
            else:
                p = p.right


def finns(p, data):
    letar = True
    while letar:
        if p == None:
            return False
        elif data == p.data:
            return True
        elif data < p.data:
            p = p.left
        elif data > p.data:
            p = p.right


def skriv(p):
    if p != None:
        skriv(p.left)
        print(p.data)
        skriv(p.right)
