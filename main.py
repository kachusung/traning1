# 导入管理系统模块
from managerSystem import *

# 启动学员管理系统
# 保证当前文件允许才能启动管理系统，使用if --创建对象并调用run方法
if __name__ == "__main__":
    student_manager = ManagerSystem()

    student_manager.run()

