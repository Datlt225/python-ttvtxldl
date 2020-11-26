from menu import *


menu = """

Menu:

1. Cập nhật công việc.
2. Cập nhật ứng viên.
3. Thống kê ngành nghề đang tuyển dụng.
4. Thống kê ngành nghề đang cần tìm việc làm.
5. Tìm kiếm thông tin tuyển dụng.
6. Xóa Stop Word.
0. Exit/Quit
"""

while True:
    print(menu)
    ans = input("Chọn chức năng: ")
    if ans == "1":
        get_job()

    elif ans == "2":
        get_job_seeker()

    elif ans == "3":
        all_career()

    elif ans == "4":
        career_need_job()

    elif ans == "5":
        search_job()

    elif ans == "6":
        stopword()

    elif ans == "0":
        break

    else:
        print('Không tồn tài chức năng này!')
