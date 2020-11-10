from module.database import *
import module.job as job
import module.jobseeker as jobseeker
from os import system


def GetNewJob():
    # Connect to database (collection: job and jobseeker)
    databaseJob = connectToDatabase('job')
    databaseJobSeeker = connectToDatabase('jobseeker')

    print('[INFO] Chờ vài phút!...')

    # Get and update ~ 3 page
    for page in range(1, 4):
        for x in jobseeker.GetLink(f'http://vieclam.laodong.com.vn/ung-vien/?page={page}'):
            key = {'_id': jobseeker.GetID(x)}
            value = {'$set': jobseeker.AllInformation(x)}
            insertToDataBase(key, value, databaseJobSeeker)

        for x in job.GetLinkJob(f'http://vieclam.laodong.com.vn/tim-kiem-ky-tuyen-dung.html?page={page}'):
            key = {'_id': job.GetID(x)}
            value = {'$set': job.AllInformation(x)}
            insertToDataBase(key, value, databaseJob)

    print('Đã xong!')


def FindJob():
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
            print(f"\nNội dung: {data[int(choose) - 1]['JobDesciption']['description']}")
            print()
            system('pause')
            break
        except:
            print("\nBài viết không tồn tại!")


FindJob()
