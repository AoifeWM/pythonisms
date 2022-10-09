from bst import BinarySearchTree, Node


class FancyTree(BinarySearchTree):

    def __init__(self, initial=None):
        super().__init__()
        if self.root:
            self.size = 1
        else:
            self.size = 0
        if initial:
            for item in initial:
                self.fancy_add(item)

    def __iter__(self):

        values = self.in_order()

        def get_values():
            for item in values:
                yield item

        return get_values()

    def __len__(self):
        return self.size

    def __str__(self):
        out = "Contains: "
        items = self.in_order()
        for item in items:
            out += "{ " + str(item) + " }, "
        if not items:
            out += "None  "
        return out[:len(out)-2]

    def fancy_add(self, value):
        self.size += 1
        self.add(value)


if __name__ == "__main__":
    data = [12, 7, 14, 32, 17, 19, 4, 3, 1, -3, 11, 400]
    ft = FancyTree(initial=data)
    print(ft.in_order())
    for item in ft:
        assert item in data
    assert len(ft) == len(data)
    print(str(ft))
    assert str(ft) == \
           "Contains: { -3 }, { 1 }, { 3 }, { 4 }, { 7 }, { 11 }, { 12 }, { 14 }, { 17 }, { 19 }, { 32 }, { 400 }"
    empty = FancyTree()
    assert len(empty) == 0
    assert str(empty) == "Contains: None"
