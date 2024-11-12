num = 5
word = "hello"
my_list = [99, 98, 97]
my_bool = True

# float(num)
# print(num.__float__())
#  5 +6
# word
word.upper()
print(word)

my_list.append(60)
print(my_list)

list1 = []
w1 = "aaa"

def get_days_in_year():
    # return 365
    num = 365

t = get_days_in_year()
print(t)


def get_mul(num1, num2):
    print("inside get_mul")
    if num1 is not None and num2 is not None:
        return num1 * num2
    else:
        raise Exception("One of multiplicators is None")


try:
    result = get_mul(5, None)
    print(result)
except Exception as error:
    print("sorry, the following error occurred:", error)

print("bye")


def convert_bytes(bytes_amount, unit="mb"):
    print("the unit is", unit)

convert_bytes(1000, "kb")
convert_bytes(1267352376434)

def foo(a, b, c, d=3, e=5, f=None):
    pass

foo(2,3,4,5)
# foo(2,3,4,5,6,7,8,9)
foo(2,3,4, f=79)
foo(a=2, b=3, c=4, f=89)
# foo(a=2, 4, 5)

foo(b=2, a=4, f=7, c=5)


def bar(a, b, *args):
    print(args)

bar(2,3, "tt", True, 687, 987)

def bar1(*args):
    print(args)

print("aaa", "bbbb", sep="_", end="***")
print("ccc")

def bar2(a, b, *args, c=5, d=6, **kwargs):
    print("a", a)
    print("b", b)
    print("args", args)
    print("c", c)
    print("d", d)
    print("kwargs", kwargs)

bar2(10, 20, "yy", "tt",
     valeria="YYYYYY", yogev="RRRRRR")

# if dxfxfgdfg:
#     pass
# if dxfxfgdfg:
#     pass
#
# if sdfsdf:
#     pass
# elif:
#     pass
# elif:

#len(), sorted(), sum(), max(), min(), abs(), round(), divmod()

my_list = [10,2,-3]
my_tuple = (1,2,3)

print(len(my_tuple))

print(sorted(my_list, reverse=True))

print(sum(my_list))

print(min(my_list))

print(round(4.6789, 2))

# result = divmod(17, 4)
# print("remainder", result[1])
full, remainder = divmod(17, 4)
print("remainder", remainder)


def foo1():
    return 1, 2, 3, 4, 5

# num1, num2, _ = foo1()
# num1, *t = foo1()

first, *t, last = foo1()

print(5 in my_list)
print(5 not in my_list)
print("t" in "hello")
