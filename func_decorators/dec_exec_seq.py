# A Key feature of decorator is they run right after the decorated function is defined.
# That is usually at import time (Refer dec_exec_seq.py)
registry = []


def register(func):
    print('running register {}'.format(func))
    registry.append(func)
    return func


@register
def f1():
    print("Running f1()")


@register
def f2():
    print("Running f2()")


def f3():
    print("Running f3()")


def main():
    print("Running main()")
    print("Registry --> ", registry)
    f1()
    f2()
    f3()


if __name__ == '__main__':
    main()

"""
Output:
running register <function f1 at 0x0000023776145168>
running register <function f2 at 0x0000023776137948>
Running main()
Registry -->  [<function f1 at 0x0000023776145168>, <function f2 at 0x0000023776137948>]
Running f1()
Running f2()
Running f3()
"""