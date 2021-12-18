from copy import deepcopy


def magnitude(f_number):
    if isinstance(f_number, int):
        return f_number
    else:
        return 3 * magnitude(f_number[0]) + 2 * magnitude(f_number[1])


class Node:
    def __init__(self, value, parent=None):
        if parent is None:
            self.deep = 0
        else:
            self.deep = parent.deep + 1
        if isinstance(value, int):
            self.right = None
            self.left = None
        else:
            self.right = Node(parent=self, value=value[1])
            self.left = Node(parent=self, value=value[0])
        self.value = value
        self.parent = parent

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


def print_t(t):
    if t is not None:
        print_t(t.left)
        print(t, 'd: ', t.deep)
        print_t(t.right)


def get_last(t):
    while t.right is not None:
        t = t.right
    return t


def get_first(t):
    while t.left is not None:
        t = t.left
    return t


def should_explode(root):
    current = root
    stack = []
    last_int = None
    while True:
        if current is not None:
            if isinstance(current.value, int):
                last_int = current
            if current.right is not None and current.left is not None:
                if current.deep >= 4 and isinstance(current.right.value, int) and isinstance(current.left.value, int):
                    stack.append(current)
                    return True, stack, last_int, root
            stack.append(current)
            current = current.left
        elif len(stack):
            current = stack.pop()
            current = current.right
        else:
            break
    return False, None, last_int, root


def explode(root):
    s, n, li, r = should_explode(root)
    # print('Explode: ', s)
    if s:
        current = n[-1]
        root = r
        if li is not None:
            if li.parent.left == li:
                val = li.parent.value
                val[0] = val[0] + current.value[0]
                li.parent = Node(value=li.parent.value, parent=li.parent.parent)
            elif li.parent.right == li:
                val = li.parent.value
                val[1] = li.value + current.value[0]
                li.parent = Node(value=li.parent.value, parent=li.parent.parent)
        fi = right_int(current)
        if fi is not None:
            if fi.parent.left == fi:
                val = fi.parent.value
                # print('Val: ', val)
                # print('Cur 0: ', current.value[0])
                val[0] = fi.value + current.value[1]
                fi.parent = Node(value=fi.parent.value, parent=fi.parent.parent)
            elif fi.parent.right == fi:
                val = fi.parent.value
                val[1] = fi.value + current.value[1]
                fi.parent = Node(value=fi.parent.value, parent=fi.parent.parent)
        if current.parent.right == current:
            current.parent.value[1] = 0
            current.parent = Node(value=current.parent.value, parent=current.parent.parent)
        elif current.parent.left == current:
            current.parent.value[0] = 0
            current.parent = Node(value=current.parent.value, parent=current.parent.parent)
    return root, s


def split(root):
    current = root
    stack = []
    while True:
        if current is not None:
            if isinstance(current.value, int):
                if current.value > 9:
                    l_v = int(current.value / 2)
                    r_v = current.value - l_v
                    if current.parent.right == current:
                        val = current.parent.value
                        val[1] = [l_v, r_v]
                        current.parent = Node(value=current.parent.value, parent=current.parent.parent)
                    elif current.parent.left == current:
                        val = current.parent.value
                        val[0] = [l_v, r_v]
                        current.parent = Node(value=current.parent.value, parent=current.parent.parent)
                    else:
                        print('Error')
                    return root, True

            stack.append(current)
            current = current.left
        elif len(stack) > 0:
            current = stack.pop()
            current = current.right
        else:
            break
    return root, False


def find_first_int(root):
    current = root
    stack = []
    first_int = None
    while True:
        if current is not None:
            if isinstance(current.value, int):
                first_int = current
                return first_int
            stack.append(current)
            current = current.left
        elif len(stack):
            current = stack.pop()
            current = current.right
        else:
            break
    return first_int


def right_int(root: Node):
    # print('Root: ', root)
    current = root.parent
    last = root
    # print('Current: ', current)
    # print('Last: ', last)
    while current.right == last:
        aux = current
        current = current.parent
        last = aux
        # print('Current: ', current)
        # print('Last: ', last)
        if current.parent is None and current.right == last:
            return None
    # print(current)
    return find_first_int(current.right)


def add(f_number_1, f_number_2):
    new = [f_number_1, f_number_2]
    tree = Node(deepcopy(new))
    been_split = True
    been_explode = True
    n = 0
    while been_split or been_explode:
        tree, been_explode = explode(tree)
        tree = Node(deepcopy(tree.value))
        while been_explode:
            tree, been_explode = explode(tree)
            tree = Node(deepcopy(tree.value))
        tree, been_split = split(tree)
        tree = Node(deepcopy(tree.value))
        n += 1
    return deepcopy(tree.value)


numbers = [eval(i) for i in open('input.txt')]
result = numbers[0]
for i in range(1, len(numbers)):
    result = add(result, numbers[i])
print('Magnitude: ', magnitude(result))

max_magnitude = 0
for i in numbers:
    for j in numbers:
        max_magnitude = max(max_magnitude, magnitude(add(i, j)))
print('Max: ', max_magnitude)
