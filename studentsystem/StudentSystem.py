from Student import Student


class StudentSystem(object):
    def __init__(self):
        self.__student_dicts = {}

    @staticmethod
    def show_menu():
        """显示菜单"""
        print('*' * 10 + '欢迎使用学生管理系统V1.0' + '*' * 10)
        print('1.添加学生')
        print('2.删除学生')
        print('3.修改学生')
        print('4.查询学生')
        print('5.查询所有学生')
        print('6.退出系统')

    def insert_student(self):
        """添加学生"""
        # 获取学生id
        name = input('请输入学生姓名：')
        # 判断学生id是否存在
        if id in self.__student_dicts:
            print('学生信息已存在，请重新核对需要添加学生的信息')
            return
        else:
            age = input('请输入学生的年龄：')
            score = input('请输入学生的分数：')
            stu = Student(name, age, score)
            self.__student_dicts[name] = stu
            print("%s添加成功" % stu.name)

    def delstudent(self):
        """删除学生"""
        # 判断学生信息是否存在
        name = input("请输入要删除的学生姓名：")
        if name in self.__student_dicts:
            print(f"学生{name}删除成功")
            del self.__student_dicts[name]
        else:
            print("抱歉该学生信息不存在，删除失败")

    def select_student(self):
        """查询学生"""
        name = input('请输入要查询的学生姓名：')
        # 判断学生是否存在
        if name in self.__student_dicts:
            print(self.__student_dicts[name])
        else:
            print('该学生不存在')

    def update_student(self):
        """修改学生信息"""
        name = input('请输入要修改的学生姓名：')
        if name in self.__student_dicts:
            print(self.__student_dicts[name])
            stu = self.__student_dicts[name]
            stu.age = input("请输入修改后的年龄：")
            stu.score = input("请输入修改后的分数：")
            print(f"学生{stu.name}信息修改成功")
        else:
            print("该学生不存在，无法修改")

    def select_all_student(self):
        """查询所有学生"""
        for i in self.__student_dicts.values():
            print(i)

    def open_file(self):
        """保存文件"""
        # 1.打开文件
        f = open('student.txt', 'a', encoding='utf-8')
        # 2.写入文件
        for i in self.__student_dicts.values():
            f.write(str(i) + '\n')
        # 3.关闭文件
        f.close()

    def write_file(self):
        """读取文件"""
        try:
            f = open("student.txt", 'r', encoding='utf-8')
        except FileNotFoundError:
            return
        else:
            buf_list = f.readlines()
            for i in buf_list:
                i = i.strip()
                i_list = i.split(",")
                my_list2 = []
                for i in i_list:
                    my_list = i.split(":")
                    my_list2.extend(my_list)

                print(my_list2)
                stu = Student(my_list2[1], my_list2[3],my_list2[5])
                self.__student_dicts[my_list2[1]] = stu
                f.close()

    def run(self):
        """程序入口"""
        self.write_file()
        while True:
            self.show_menu()
            id = input('请输入要操作的序号：')
            if id == '1':
                print('添加学生')
                self.insert_student()
            elif id == '2':
                print('删除学生')
                self.delstudent()
            elif id == '3':
                print('修改学生')
                self.update_student()
            elif id == '4':
                print('查询学生')
                self.select_student()
            elif id == '5':
                print('查询所有学生')
                self.select_all_student()
            elif id == '6':
                self.open_file()
                print('系统退出，欢迎下次继续使用')
                break


if __name__ == '__main__':
    # 创建对象
    stu_sys = StudentSystem()
    stu_sys.write_file()
