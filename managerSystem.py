from student import *

class ManagerSystem(object):
    def __init__(self):
        self.students_list = []

    # 定义程序的入口函数，启动程序后执行的函数
    def run(self):
        # 1加载学员信息
        self.load_student()

        # 建立循环（需要反复进入操作界面以及选择功能序号）
        while True:
            # 显示操作界面
            self.show_menu()

            # 提示用户输入功能序号
            menu_num = int(input("请输入您需要执行的功能序号："))

            # 根据用户输入的功能序员执行功能代码
            if menu_num == 1:
                # 添加学员
                self.add_student()
            elif menu_num == 2:
                # 删除学员
                self.del_student()
            elif menu_num == 3:
                # 修改学员
                self.modify_student()
            elif menu_num == 4:
                # 查询学员
                self.search_student()
            elif menu_num == 5:
                # 显示所有学员
                self.show_students()
            elif menu_num == 6:
                # 保存学员信息
                self.save_student()
            elif menu_num == 7:
                # 退出系统
                break

    @staticmethod  # 因为不需要参数，可以定义静态方法
    def show_menu():
        print("请选择如下功能：\n1.添加学员\n2.删除学员\n3.修改学员信息\n4.查询学员信息\n5.显示所有学员信息\n6.保存学员信息\n7.退出系统")

    def add_student(self):
        # 输入学员信息
        name = input("请输入学员姓名：")
        gender = input("请输入学员性别：")
        tel = input("请输入学员电话：")
        # 创建学员对象
        student = Student(name, gender, tel)
        # 添加到列表
        self.students_list.append(student)

    def del_student(self):
        # 删除学员：指定姓名删除
        del_name = input("请输入需要删除的学员姓名：")
        # 遍历列表查找学员
        for i in self.students_list:
            if i.name == del_name:
                self.students_list.remove(i)
                break
            else:
                print("查无此人！")

    def modify_student(self):
        # 修改学员信息
        modify_name = input("请输入需要修改的学员姓名：")
        # 遍历列表查找学员
        for i in self.students_list:
            if i.name == modify_name:
                i.name = input("请输入修改后的学员姓名：")
                i.gender = input("请输入修改后的学员性别：")
                i.tel = input("请输入修改后的学员电话：")
                print(f"修改该学员信息成功。\n姓名：{i.name}\t性别：{i.gender}\t电话：{i.tel}")
            else:
                print("该学员不存在。")

    def search_student(self):
        search_name = input("请输入需要查找的学员姓名：")

        for i in self.students_list:
            if i.name == search_name:
                print(f"您查找的学员信息如下：\n姓名：{i.name}\t性别：{i.gender}\t电话：{i.tel}")
                break
            else:
                print("查无此人！")

    def show_students(self):
        print("姓名\t性别\t电话")
        for i in self.students_list:
            print(f"{i.name}\t{i.gender}\t{i.tel}")

    def save_student(self):
        # 打开文件
        f = open("student.data","w")
        # 写入数据
        # 注意：写入的数据不能是学员对象的内存地址，需要把学员对象的数据转换为列表字典类型再存储
        new_list = [i.__dict__ for i in self.students_list]
        # 注意：文件内数据要求的是字符串类型，需要先将列表数据转换为字符串数据
        f.write(str(new_list))
        # 关闭文件
        f.close()

    def load_student(self):
        # 加载学员信息数据
        # 首先尝试以”r“模式打开文件，如果文件不存在，则提示用户，文件存在，则读取文件数据
        try:
            f = open("student.data","r")
        except:
            f = open("student.data","w")
        else:
            # 读取数据
            data = f.read()
            # 文件中读取到的数据都是字符串，并且字符串内部为字典数据，故需要转换数据类型再转换字典为对象后再存储到学员列表
            new_list = eval(data)
            self.students_list = [Student(i["name"],i["gender"],i["tel"]) for i in new_list]
        finally:
            # 关闭文件
            f.close()
