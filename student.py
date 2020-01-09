class Student(object):
    def __init__(self,name,gender,tel):
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f"姓名：{self.name}\t性别：{self.gender}\t电话：{self.tel}"

if __name__ == "__main__":
    aa = Student("Tom","man",123)
    print(aa)