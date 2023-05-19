# def abc(*args, **kwargs):
#     print(args,kwargs)
# def a_b(*args):
#     print(args[0])
#     print(args[1])
#     print(args[2])

# def a_c(**kwargs):
#     print(kwargs)
# def a_b_test(a):
#     print(a)
# a_list=["1"]
# if __name__ == "__main__":
#     a="1"
#     a=1
#     # 指针
#     # print(id(a))
#     # print(a_b(123,234,324,234))
#     # print(a_c(a=1,b=2))
#     print(abc(1,2,3,4,c=2,b=5))
#     # print(a_b_test(123,23,234,2342))
# [(1, '张三', '男', '80', '90', '80', '80', '80', '80', '80', '80', '初一3班', 'nan', datetime.datetime(2023, 5, 
# 13, 16, 6, 9)), (4, '张三', '男', '80', '90', '80', '80', '80', '80', '80', '80', '初一3班', 'nan', datetime.datetime(2023, 5, 13, 16, 6, 9))]
class DynamicVariable(object):
    def __init__(self,valueList) -> None:
        self.names = self.__dict__
        for i in range(len(valueList)):
            self.names[valueList[i]] = valueList[i]
    def return_value(self):
        return self.names
b1 = DynamicVariable(['b','2','3','4'])
# print(b1.names)

# print("--{}--{}".format({1},{2}))
b=object()
print(b)