import module.job as job
import module.jobseeker as jobseeker
from module.database import *

databaseJob = connectToDatabase('job')
databaseJobSeeker = connectToDatabase('jobseeker')

count = 0
for page in range(1, 501):
    for x in jobseeker.GetLink(f'http://vieclam.laodong.com.vn/ung-vien/?page={page}'):
        key = {'_id': jobseeker.GetID(x)}
        value = {'$set': jobseeker.AllInformation(x)}
        insertToDataBase(key, value, databaseJobSeeker)
        count += 1
        print(f'[INFO] {count}...')

    for x in job.GetLinkJob(f'http://vieclam.laodong.com.vn/tim-kiem-ky-tuyen-dung.html?page={page}'):
        key = {'_id': job.GetID(x)}
        value = {'$set': job.AllInformation(x)}
        insertToDataBase(key, value, databaseJob)
        count += 1
        print(f'[INFO] {count}...')

print('Done!')
