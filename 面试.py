student_infos = []
def show_help():
    print('-----这是帮助信息-------')

def print_menu():
    """打印显示功能"""
    print('='*70)
    print()
    print('欢迎使用计算机考试管理系统')
    print('计算机考试学生信息管理系统 V1.0')
    print('='*70)
    print('#. 显示帮助信息')
    print('*. 验证信息')
    print('1. 添加考生信息')
    print('2. 搜索考生信息')
    print('3. 删除考生信息')
    print('4. 修改考生的信息')
    print('5. 显示所有考生的信息')  # 保存到本地
    print('6. 保存信息')
    print('0. 退出系统')
    print()
    print('='*70)

#添加闭包用来验证身份
#如果身份证号长度小于18位，准考证号小于8位就验证失败
#当然验证失败不会影响后续的程序，但是可以初步判断自己输入的号是否正确
#这个验证可以自主验证，也可以在程序刚开始验证
def w1(func):
    def inner(ID,exam):
        print('开始验证')
        print('.................')
        if len(ID)==18 and len(exam)>=8:
            a='验证成功'
            print(a)
        else:
            a='验证失败，请重新输入'
            print(a)
                
        func(ID,exam)
    return inner

@w1
def shu_ru(ID,exam):
    print('身份证号是：{}准考证号是：{}'.format(ID,exam))
#既可以自主验证也可以输入对应的key键进行验证
shu_ru(input('请输入ID：'),input('请输入准考证号exam:'))
print('*'*70)
#添加考生信息

def add_info():
    """添加一个考生信息"""
    # 1. 你必须要知道考生有哪些信息(并且获取学生的信息)
    new_name = input('请输入学生的名字:')
    exam_number=input('请输入学生准考证号:')
    ID_number=input('请输入学生身份证号')
    new_sex = input('请输入学生的性别:(男/女):')
    new_phone = input('请输入学生的手机号:')
    # 2. 把考生的信息 放在一个字典里面
    new_infos = {}
    new_infos['name'] = new_name
    new_infos['exam']=exam_number
    new_infos['ID']=ID_number
    new_infos['sex'] = new_sex
    new_infos['phone'] = new_phone
    # 3. 把考生的字典 放在 全局的列表(他是记录我们所有学生信息的)
    student_infos.append(new_infos)

# 搜索考生的信息
def search_student():
    print("-"*70)
    print("功能:搜索考生")
#先根据名字找到该考生
    find_name = input("请输入要搜索的内容:")
    for new_infos in student_infos:
        if new_infos["name"] == find_name:
            print(" 姓名\t\t准考证号\t\t身份证号\t性别  手机号\t")
            print("-" * 70)
            print()
            print("%s\t%s\t    %s\t\t%s\t%s" % (new_infos["name"],new_infos["exam"],new_infos["ID"],new_infos["sex"],new_infos["phone"]))
            print("-" * 60)
            break
        else:
            print("没有找到 %s" % find_name)

#删除考生信息
def del_info(student):
    """删除学生的信息"""
    del_number = int(input('请输入要删除的考生的序列号'))
    del student[del_number-1]

# 修改考生的信息
def modify_info():
    # 得到要求改的考生  到底是哪个考生
    student_id = int(input('请输入要修改的学生的序号:'))
    # 你需要 把你要修改的内容你得输入一下
    # 以下5个变量  是用户输入的
    new_name = input('请输入修改后的学生的名字:')
    exam_number=input('请输入修改后学生准考证号:')
    ID_number=input('请输入修改后学生身份证号')
    new_sex = input('请输入修改后的学生的性别(男/女):')
    new_phone = input('请输入修改后的学生的手机号:')
   
    # 当我们 拿到用户输入的信息后  我们就去找
    #  去所有学生里面找到要修改的哪个考生
    # 去全局的列表里面去找

    student_infos[student_id-1]['name'] = new_name
    student_infos[student_id-1]['exam'] =exam_number
    student_infos[student_id-1]['ID'] = ID_number
    student_infos[student_id-1]['sex'] = new_sex
    student_infos[student_id-1]['phone'] = new_phone

# 显示考生的所有信息
def show_infos():
    """展示所有考生的信息"""
    # 展示了一下 横线
    print('='*70)
    # 普通的输出
    print('学生信息如下:')
    # 一条横线
    print('-'*70)
    # excel 表头(其实就是第一行显示的内容)
    print(' 序号   姓名\t\t准考证号\t    身份证号\t   性别  手机号')
    # 其实就是序号
    print('-'*70)
    i = 1
    # 遍历列表----> 列表装了所有考生的信息
    # 每一次遍历出来 或者说每一次循环出来的  就是一个考生的信息
    for student_dict in student_infos:
        print(' %d %s \t%s\t     %s    \t%s  %s ' % (
            i, student_dict['name'],student_dict['exam'],student_dict['ID'], student_dict['sex'], student_dict['phone']))
        i += 1
    print('='*70)

# 保存学生的信息(文件版,保存到本地)

def save_to_file():
    """保存考生的信息到文件中"""
    # 打开文件
    file = open('student.data', 'w')
    # 写入内容
    file.write(str(student_infos))
    # 关闭
    file.close()
# 读取信息

#  先看一下  有没有  存在本地的信息
def recover_data():
    global student_infos
    try:
        # 1. 打开文件
        file = open('student.data','r')
            # 2. 读取文件
        # content 内容
        content = file.read()
        student_infos = eval(content)
        # 3. 关闭
        file.close()
    except:
        print('没有历史数据')

# main  主程序----> 调用其他函数
def main():
    # 1. 先恢复数据
    recover_data()
    while True:
        print_menu()
        # 用户去输入一个数字--->判断他要实使用什么功能
        key = input('请输入对应功能:')
        if key == '#':
            #显示帮助信息
            show_help()
        elif key == '*':
            #验证身份
            shu_ru(input('请输入ID：'),input('请输入准考证号exam:'))
        elif key == '1':
            # 添加考生信息
            add_info()
        elif key == '2':
            # 搜索考生信息
            search_student()
        elif key == '3':
            # 删除考生信息
            del_info(student_infos)
        elif key == '4':
            # 修改
            modify_info()
        elif key == '5':
            # 查看所有
            show_infos()
        elif key == '6':
            # 保存信息
            save_to_file()
        elif key == '0':  
             # 退出系统
            quit_confirm = input('亲,你真的要退出吗?(Yes/No):')
            if quit_confirm == 'Yes':
                break
            else:
                print('输入有误,请重写输入')
main()

