NESTED_LIST = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]

# 1.Итератор


class FlatIterator(list):

    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.unp_list = []

    def list_unpack(self):
        for elements in self.nested_list:
            for element in elements:
                self.unp_list.append(element)
        return self.unp_list

    def __iter__(self):
        self.counter = 0
        self.el = iter(self.list_unpack())
        return self

    def __next__(self):
        if self.counter == len(self.unp_list):
            raise StopIteration
        next_elem = next(self.el)
        self.counter += 1
        return next_elem


# 2.Генераторы


def flat_generator_var1(nested_list: list):
    unpack_list = [element for elements in nested_list for element in elements]
    return unpack_list


def flat_generator_var2(nested_list: list):
    unpack_gen = (element for elements in nested_list for element in elements)
    return unpack_gen


def flat_generator_var3(nested_list: list):
    for elements in nested_list:
        for element in elements:
            yield element


def run():
    for items in FlatIterator(NESTED_LIST):
        print(items)
    flat_list = [items for items in FlatIterator(NESTED_LIST)]
    print(flat_list)


def run2():
    for item in flat_generator_var1(NESTED_LIST):
        print(item, end='  ')
    print()
    for item in flat_generator_var2(NESTED_LIST):
        print(item, end='  ')
    print()
    for item in flat_generator_var3(NESTED_LIST):
        print(item, end='  ')
    print()


run()
run2()

