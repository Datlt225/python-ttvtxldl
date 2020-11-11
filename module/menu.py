from module.database import *
import module.job as job
import module.jobseeker as jobseeker
from os import system
import matplotlib.pyplot as plt
import numpy as np


def GetNewJob():
    # Connect to database (collection: job)
    databaseJob = connectToDatabase('job')

    print('[INFO] Chờ vài phút!...')

    # Get and update ~ 3 page
    for page in range(1, 4):
        for x in job.GetLinkJob(f'http://vieclam.laodong.com.vn/tim-kiem-ky-tuyen-dung.html?page={page}'):
            key = {'_id': job.GetID(x)}
            value = {'$set': job.AllInformation(x)}
            insertToDataBase(key, value, databaseJob)

    print('Đã xong!')


def GetNewJobSeeker():
    # Connect to database (collection: jobseeker)
    databaseJobSeeker = connectToDatabase('jobseeker')

    print('[INFO] Chờ vài phút!...')

    # Get and update ~ 3 page
    for page in range(1, 4):
        for x in jobseeker.GetLink(f'http://vieclam.laodong.com.vn/ung-vien/?page={page}'):
            key = {'_id': jobseeker.GetID(x)}
            value = {'$set': jobseeker.AllInformation(x)}
            insertToDataBase(key, value, databaseJobSeeker)

    print('Đã xong!')


def FindJob():
    system('cls')

    # Search text
    searchText = input('Từ khóa: ')

    # Connect to database with "job" collection
    db = connectToDatabase('job')

    # Create Index
    db.create_index([('Search', 'text')])

    # Search and return a list
    data = list(db.find({"$text": {"$search": searchText}}).limit(10))

    # Check search
    if len(data) == 0:
        print(f'\n\nKhông tìm thấy bài viết có từ khóa "{searchText}"!\n\n')
        return

    # Print search list
    i = 0
    print(f'Các bài viết có từ khóa "{searchText}":\n')
    for x in data:
        i += 1
        print(f"     {i}. {x['JobDesciption']['title']}")

    # Choose post
    while True:
        choose = input("\nBài viết muốn xem (Enter để bỏ qua): ")
        if choose == '':
            break

        try:
            # Job information
            print('\nMÔ TẢ CÔNG VIỆC:')
            print(f"  - Ngành nghề: {data[int(choose) - 1]['JobDesciption']['career']}")
            print(f"  - Cấp bậc: {data[int(choose) - 1]['JobDesciption']['level']}")
            print(f"  - Mô tả công việc: {data[int(choose) - 1]['JobDesciption']['description']}")
            print(f"  - Yêu cầu công việc: {data[int(choose) - 1]['JobDesciption']['requirements']}")
            print(f"  - Lương: {data[int(choose) - 1]['JobDesciption']['salary']}")
            print(f"  - Chế độ quyền lợi khác: {data[int(choose) - 1]['JobDesciption']['otherAdvanced']}")
            print(f"  - Địa điểm làm việc: {data[int(choose) - 1]['JobDesciption']['location']}")

            # Contact information
            print('\nTHÔNG TIN LIÊN HỆ:')
            print(f"  - Địa chỉ liên hệ: {data[int(choose) - 1]['ContactInformation']['address']}")
            print(f"  - Người liên hệ: {data[int(choose) - 1]['ContactInformation']['person']}")
            print(f"  - Số điện thoại liên hệ: {data[int(choose) - 1]['ContactInformation']['phone']}")
            print(f"  - Email liên hệ: {data[int(choose) - 1]['ContactInformation']['email']}")
            print(f"  - Hạn nộp HS: {data[int(choose) - 1]['ContactInformation']['expiryDate']}")
            print(f"  - Địa điểm làm việc: {data[int(choose) - 1]['ContactInformation']['workLocation']}")

            # Profile Requirements
            print('\nYÊU CẦU HỒ SƠ:')
            print(f"  - Độ tuổi: {data[int(choose) - 1]['ProfileRequirements']['minAge']} - {data[int(choose) - 1]['ProfileRequirements']['maxAge']}")
            print(f"  - Giới tính: {data[int(choose) - 1]['ProfileRequirements']['gender']}")
            print(f"  - Trình độ: {data[int(choose) - 1]['ProfileRequirements']['educationLevel']}")
            print(f"  - Kinh nghiệm: {data[int(choose) - 1]['ProfileRequirements']['experience']}")
            print(f"  - Yêu cầu khác: {data[int(choose) - 1]['ProfileRequirements']['orther']}")

            print()
            system('pause')
            break
        except:
            print("\nBài viết không tồn tại!")


def AllCareer():
    counts = dict()
    name = []
    value = []

    # Connect to database (Collection: job)
    db = connectToDatabase('job')
    data = db.find()

    # Get all carrer
    for x in data:
        career = x['JobDesciption']['career']

        for word in career.split(','):
            word = ' '.join(word.split())
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

    # Get name and value list
    print("CHI TIẾT SỐ LƯỢNG NGÀNH NGHỀ ĐANG TUYỂN DỤNG: ")
    for x, y in counts.items():
        print(f'   - {x}: {y}')
        name.append(x)
        value.append(y)

    # Chart carrer
    y_pos = np.arange(len(name))
    plt.bar(y_pos, value)
    plt.title("BIỂU ĐỒ SỐ LƯỢNG NGÀNH NGHỀ ĐANG TUYỂN DỤNG")
    plt.xticks(y_pos, name, rotation=90, fontsize=3)
    plt.savefig('../image/chart.png', dpi=1500)


AllCareer()
