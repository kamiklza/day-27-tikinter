# def add(total=0, *args):
#     for n in args:
#         total += n
#     print(total)

def add(**kwargs):
    print(kwargs.items())
    for key, value in kwargs.items():
        print(key)
        print(value)
