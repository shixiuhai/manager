def abc(*args, **kwargs):
    print(args,kwargs)
def a_b(*args):
    print(args[0])
    print(args[1])
    print(args[2])

def a_c(**kwargs):
    print(kwargs)
def a_b_test(a):
    print(a)
a_list=["1"]
if __name__ == "__main__":
    a="1"
    a=1
    # 指针
    # print(id(a))
    # print(a_b(123,234,324,234))
    # print(a_c(a=1,b=2))
    print(abc(1,2,3,4,c=2,b=5))
    # print(a_b_test(123,23,234,2342))