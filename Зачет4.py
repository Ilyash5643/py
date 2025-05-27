class FlattenIterator:
    def __init__(self, nested_list):
        self.stack = [iter([nested_list])]

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            current_iter = self.stack[-1]
            try:
                next_item = next(current_iter)
            except StopIteration:
                self.stack.pop()
                continue
            if isinstance(next_item, list):
                self.stack.append(iter(next_item))
            else:
                return next_item
        raise StopIteration


nested_list = [1, [2, [3, 4], 5], 6]
flat = FlattenIterator(nested_list)
for num in flat:
    print(num)
    

