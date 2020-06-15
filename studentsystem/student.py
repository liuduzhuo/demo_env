class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return f"姓名：{self.name}, 年龄：{self.age}, 分数：{self.score}"

if __name__ == '__main__':
    # 创建学生对象
    zhangsan = Student('张三', 20, 60)
    print(zhangsan)