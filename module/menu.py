from module.database import *
import module.job as job
import module.jobseeker as jobseeker


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

    # Connect to database
    db = connectToDatabase('job')

    # Create Index
    db.create_index([('Search', 'text')])

    # Search
    data = db.find({"$text": {"$search": searchText}}).limit(10)

    for x in data:
        print(x)


FindJob()
