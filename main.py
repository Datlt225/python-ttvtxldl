from module.menu import *

menu = """

Menu:

1. Cập nhật công việc.
2. Cập nhật ứng viên.
3. Thống kê ngành nghề đang tuyển dụng.
4. Thống kê ngành nghề đang cần tìm việc làm.
5. Tìm kiếm thông tin tuyển dụng.
0. Exit/Quit
"""

while True:
    print(menu)
    ans = input("Chọn chức năng: ")
    if ans == "1":
        GetNewJob()

    elif ans == "2":
        GetNewJobSeeker()

    elif ans == "3":
        AllCareer()

    elif ans == "4":
        CareerNeedJob()

    elif ans == "5":
        FindJob()

    elif ans == "0":
        break

    else:
        print('Không tồn tài chức năng này!')
        system('pause')
