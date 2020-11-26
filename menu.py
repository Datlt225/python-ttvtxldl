from database import *
import job
import jobseeker
import matplotlib.pyplot as plt
import numpy as np
import remove_stopword
from pyvi import ViTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from underthesea import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity


stop_word = remove_stopword.get_stopword()


def get_job():
    count = 0
    db = connect_database('job')

    print("[INFO] Chờ vài phút!...")

    # cập nhật bài viết mới ~ 3 trang
    for page in range(1, 543):
        for x in job.GetLinkJob("http://vieclam.laodong.com.vn/tim-kiem-ky-tuyen-dung.html?page={}".format(page)):
            key = {"_id": job.GetID(x)}
            value = {
                "$set": job.AllInformation(x)
            }
            insert_database(key, value, db)
            count += 1
            print("[Việc làm][{}] - Đã lấy được {} bài!".format(page, count))

    print("\n\n[INFO] Xong!...\n\n")


def get_job_seeker():
    count = 0
    db = connect_database('jobseeker')

    print('[INFO] Chờ vài phút!...')

    # cập nhật bài viết mới ~ 3 trang
    for page in range(1, 543):
        for x in jobseeker.GetLink(f'http://vieclam.laodong.com.vn/ung-vien/?page={page}'):
            key = {'_id': jobseeker.GetID(x)}
            value = {'$set': jobseeker.AllInformation(x)}
            insert_database(key, value, db)
            count += 1
            print("[Ứng cử viên][{}] - Đã lấy được {} bài!".format(page, count))

    print("\n\n[INFO] Xong!...\n\n")


def all_career():
    counts = dict()
    name = []
    value = []

    # Connect to database (Collection: job)
    db = connect_database('job')
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

    # Chart career
    y_pos = np.arange(len(name))
    plt.bar(y_pos, value, color='blue')
    plt.title("BIỂU ĐỒ SỐ LƯỢNG NGÀNH NGHỀ ĐANG TUYỂN DỤNG")
    plt.xticks(y_pos, name, rotation=90, fontsize=3)
    plt.savefig('./image/career-chart.png', dpi=1500)


def career_need_job():
    counts = dict()
    name = []
    value = []

    # Connect to database (Collection: job)
    db = connect_database('jobseeker')
    data = db.find()

    # Get all carrer
    for x in data:
        career = x['CareerAspirations']['expectedJobCategory']

        for word in career.split(','):
            word = ' '.join(word.split())
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

    # Get name and value list
    print("CHI TIẾT SỐ LƯỢNG NGÀNH NGHỀ ĐANG CẦN VIỆC LÀM: ")
    for x, y in counts.items():
        print(f'   - {x}: {y}')
        name.append(x)
        value.append(y)

    # Chart career
    y_pos = np.arange(len(name))
    plt.bar(y_pos, value, color='blue')
    plt.title("BIỂU ĐỒ SỐ LƯỢNG NGÀNH NGHỀ ĐANG CẦN VIỆC LÀM")
    plt.xticks(y_pos, name, rotation=90, fontsize=3)
    plt.savefig('./image/chart-career-need-job.png', dpi=1500)


def search_job():
    search_text = input("Từ khóa: ")
    db = connect_database('job')  # kết nối cơ sở dữ liệu

    all_job = []
    for x in db.find():
        text = remove_stopword.remove_stopword(x['JobDesciption']['title'], stop_word) + "| " + remove_stopword.remove_stopword(x['Search'], stop_word)
        text = text.lower()
        # print(text)
        all_job.append(ViTokenizer.tokenize(text))

    vector = TfidfVectorizer()
    x = vector.fit_transform(all_job)
    search_text = search_text.lower()
    te = word_tokenize(search_text, format='text')
    te = remove_stopword.remove_stopword(te, stop_word)
    te = vector.transform([te])
    length = str(te).split("\t")

    if len(length) > 1:
        re = cosine_similarity(x, te)

        result = []

        for i in range(len(re)):
            result.append(re[i][0])

        count = 0

        for i in np.argsort(result)[-20:][::-1]:
            count += 1
            print("{}. {}".format(count, all_job[i].split('|')[0].replace("_", " ")))

    else:
        print(f'Không tìm thấy bài viết có từ khóa "{search_text}"!')


def stopword():
    string = input("Nhập nội dung cần xóa: ")

    print("Chuỗi trước khi xóa: {}".format(string))
    print("Chuỗi sau khi xóa: {}".format(remove_stopword.remove_stopword(string, stop_word)))
