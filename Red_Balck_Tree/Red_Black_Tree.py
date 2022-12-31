from sys import maxsize


class Node:
    def __init__(self, val=3, color="red", parent=None, left=None, right=None) -> None:
        self.val = val
        self.p = parent
        self.color = color
        self.left = left
        self.right = right


def printTree(root):
    if not root:
        print()
        return
    print(
        f"val: {root.val} color: {root.color} parent: {root.p} left: {root.left} right: {root.right}"
    )
    printTree(root.left)
    printTree(root.right)


def RB_Insert(root, z):
    y = None
    x = root

    while x != None:
        y = x
        if z.val < x.val:
            x = x.left
        else:
            x = x.right
    z.p = y

    if y == None:
        root = z
    elif z.val < y.val:
        y.left = z
    else:
        y.right = z
    z.left = None
    z.right = None
    z.color = "red"
    RB_Insert_Fixup(root, z)


def insertRoot(r, val):
    r = Node(val=val, color="black")
    return r


def RB_Insert_Fixup(root, z):
    while z.p and z.p.color == "red":
        if z.p == z.p.p.left:
            y = z.p.p.right
            if y and y.color == "red":
                z.p.color = "black"
                y.color = "black"
                z.p.p.color = "red"
                z = z.p.p
            elif z == z.p.right:
                z = z.p
                Left_Rotate(root, z)
            if z.p and z.p.p:
                z.p.color = "black"
                z.p.p.color = "red"
                Right_Rotate(root, z.p.p)

        else:
            y = z.p.p.left
            if y and y.color == "red":
                z.p.color = "black"
                y.color = "black"
                z.p.p.color = "red"
                z = z.p.p
            elif z == z.p.left:
                z = z.p
                Right_Rotate(root, z)
            if z.p and z.p.p:
                z.p.color = "black"
                z.p.p.color = "red"
                Left_Rotate(root, z.p.p)
        root.color = "black"


def Left_Rotate(root, x):
    y = x.right
    x.right = y.left
    if y.left != None:
        y.left.p = x
    y.p = x.p
    if x.p == None:
        root = y
    elif x == x.p.left:
        x.p.left = y
    else:
        x.p.right = y
    y.left = x
    x.p = y


def Right_Rotate(root, x):
    y = x.left
    x.left = y.right
    if y.right != None:
        y.right.p = x
    y.p = x.p
    if x.p == None:
        root = y
    elif x == x.p.right:
        x.p.right = y
    else:
        x.p.left = y
    y.right = x
    x.p = y


if __name__ == "__main__":
    root = None
    nodes = int(input("Enter the number of nodes to insert: "))
    val = int(input("Enter val: "))
    root = insertRoot(root, val)
    for _ in range(1, nodes):
        val = int(input("Enter val: "))
        z = Node(val)
        RB_Insert(root, z)
    printTree(root)
