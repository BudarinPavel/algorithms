def init_memory(max_n):
    memory = []
    for i in range(max_n):
        memory.append([0, i + 1, 0])
    return [memory, 0]


def new_node(mem_struct):
    memory, first_free = mem_struct
    mem_struct[1] = memory[first_free][1]
    return first_free


def del_node(mem_struct, index):
    memory, first_free = mem_struct
    memory[index][1] = first_free
    mem_struct[1] = index


def find(mem_struct, root, x):
    key = mem_struct[0][root][0]
    if x == key:
        return root
    elif x < key:
        left = mem_struct[0][root][1]
        if left == -1:
            return -1
        else:
            return find(mem_struct, left, x)
    elif x > key:
        right = mem_struct[0][root][2]
        if right == -1:
            return -1
        else:
            return find(mem_struct, right, x)


def create_and_fill_node(mem_struct, key):
    index = new_node(mem_struct)
    mem_struct[0][index][0] = key
    mem_struct[0][index][1] = -1
    mem_struct[0][index][2] = -1
    return index


def add(mem_struct, root, x):
    key = mem_struct[0][root][0]
    if x < key:
        left = mem_struct[0][root][1]
        if left == -1:
            mem_struct[0][root][1] = create_and_fill_node(mem_struct, x)
        else:
            add(mem_struct, left, x)
    elif x > key:
        right = mem_struct[0][root][2]
        if right == -1:
            mem_struct[0][root][2] = create_and_fill_node(mem_struct, x)
        else:
            add(mem_struct, right, x)


mem_struct = init_memory(20)
root = create_and_fill_node(mem_struct, 8)
add(mem_struct, root, 10)
add(mem_struct, root, 9)
add(mem_struct, root, 14)
add(mem_struct, root, 13)
add(mem_struct, root, 3)
add(mem_struct, root, 1)
add(mem_struct, root, 6)
add(mem_struct, root, 4)
add(mem_struct, root, 7)


def meke_tree(serialised):
    tree = {'left': None, 'right': None, 'up': None, 'type': 'root'}
    now_node = tree
    for sym in serialised:
        if sym == 'D':
            new_node = {'left': None, 'right': None, 'up': now_node, 'type': 'left'}
            now_node['left'] = new_node
            now_node = new_node
        elif sym == 'U':
            while now_node['type'] == 'right':
                now_node = now_node['up']
            now_node = now_node['up']
            new_node = {'left': None, 'right': None, 'up': now_node, 'type': 'right'}
            now_node['right'] = new_node
            now_node = new_node
    return tree


def traverse(root, prefix):
    if root['left'] is None and root['right'] is None:
        return [''.join(prefix)]
    prefix.append('0')
    ans = traverse(root['left'], prefix)
    prefix.pop()
    prefix.append('1')

    ans.extend(traverse(root['right'], prefix))
    prefix.pop()
    return ans

