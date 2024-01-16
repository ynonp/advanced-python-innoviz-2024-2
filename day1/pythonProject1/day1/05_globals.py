g_total = 0
items = []
d = {}

def add_item():
    items.append(5)


def add_dict_item():
    d['one'] = 1


def put_value_in_variable():
    # x is an internal variable of the function,
    # regardless of what happens outside
    x = 10


def show():
    print(g_total)




def add(val):
    global g_total
    g_total += int(val)

add(10)
add('20')
add(5)
show()

