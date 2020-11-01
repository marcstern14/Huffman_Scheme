from ch08.linked_binary_tree import LinkedBinaryTree
from ch09.heap_priority_queue import HeapPriorityQueue

class Huffman:

    def __init__(self):
        self.text_to_binary = {}
        self.binary_to_text = {}

    def encode(self, s):
        map = {}
        for c in s:
            if not c in map:
                map[c] = 1
            else:
                map[c] += 1

        q = HeapPriorityQueue()

        for key in map:
            t = LinkedBinaryTree()
            r = t._add_root(key)
            q.add(map[key], t)

        while len(q) > 1:
            t1 = q.remove_min()
            t2 = q.remove_min()

            nt = LinkedBinaryTree()
            f = t1[0] + t2[0]

            root = nt._add_root(f)
            nt._attach(root, t1[1], t2[1])

            q.add(f, nt)

        tree = q.remove_min()

        for i in tree[1].preorder():

            if i._node._parent is not None:

                if i._node._left is None and i._node._right is None:
                    l = []
                    me = i._node
                    p = me._parent

                    while p is not None:
                        if me is p._left:
                            l.append('0')
                        elif me is p._right:
                            l.append('1')
                        me, p = p, p._parent

                    lrev = reversed(l)
                    binary = ''.join(lrev)

                    self.text_to_binary[i.element()] = binary
                    self.binary_to_text[binary] = i.element()

    def compression(self, s):
        l = list(s)
        nl = []
        for c in l:
            binary = self.text_to_binary[c]
            nl.append(binary)
        t = ' '.join(nl)
        return t

    def decompression(self, s):
        l = s.split()
        nl = []
        for binary in l:
            c = self.binary_to_text[binary]
            nl.append(c)
        t = ''.join(nl)
        return t

mytext = 'dogs do not spot hot pots or cats'
h = Huffman()
e = h.encode(mytext)
c = h.compression(mytext)
d = h.decompression(c)
print(d)
print(c)
