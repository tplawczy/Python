class Tree(object):
    "Generic tree node."
    def __init__(self, name='root', children=None):
        self.name = name
        self.a=" "
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)


    def display(self, Tree):


        print(self.a+Tree.name)
        self.a.replace(" ", "")
        for x in Tree.children:
                self.a.replace(" ", "")
                (self.display(x))
                self.a.replace(" ", "")
        self.a += self.a
        self.a.replace(" ", "")


t = Tree('*', [Tree('1'),
               Tree('2'),
               Tree('+', [Tree('3'),
                          Tree('4', [Tree('7'),
                                     Tree('8')])])])

t.display(t)


