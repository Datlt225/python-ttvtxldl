import requests
from bs4 import BeautifulSoup
import re
import module.deletestopword as deletestopword


URL = 'http://vieclam.laodong.com.vn/ky-tuyen-dung/tuyen-dung-nhan-vien-spa-lam-viec-tai-diva-ben-cat-76752.html'


def RemoveSpace(text):
    text = re.sub('[!@#$+*-]', '', text)
    return ' '.join(text.split())


def GetSoup(url):
    # Get response
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html5lib')

    return soup


def GetLinkJob(url):
    linkJob = []
    soup = GetSoup(url)

    # Get job
    allJob = soup.find_all('header', class_='job')

    for job in allJob:
        linkJob.append('http://vieclam.laodong.com.vn' + job.h3.a['href'])

    return linkJob


def JobDesciption(soup):
    title = soup.find('meta', property="og:description")['content']
    career = soup.find('span', id='cphMainContent_lblJobCategoryID').text
    level = soup.find('span', id='cphMainContent_lblJobLevelID').text
    description = soup.find('span', id='cphMainContent_lblDescription').text
    requirements = soup.find('span', id='cphMainContent_lblRequirements').text
    location = soup.find('span', id='cphMainContent_lblWorkLocationID').text
    try:
        salary = f"{soup.find('span', id='cphMainContent_lblMinSalary').text} - {soup.find('span', id='cphMainContent_lblMaxSalary').text} triệu đồng"
    except:
        salary = 'Thỏa thuận'
    otherAdvanced = soup.find('span', id='cphMainContent_lblOtherAdvanced').text

    dictionary = {
        "title": title,
        "career": career,
        "level": level,
        "description": RemoveSpace(description),
        "requirements": RemoveSpace(requirements),
        "salary": salary,
        "otherAdvanced": otherAdvanced != '' and RemoveSpace(otherAdvanced) or 'Không có',
        "location": location
    }

    return dictionary


def ContactInformation(soup):
    address = soup.find("span", id="cphMainContent_lblContactAddress").text
    person = soup.find("span", id="cphMainContent_lblContactPerson").text
    phone = soup.find("span", id="cphMainContent_lblContactPhone").text
    email = soup.find("span", id="cphMainContent_lblContactEmail").text
    expiryDate = soup.find("span", id="cphMainContent_lblExpiryDate").text
    workLocation = soup.find("span", id="cphMainContent_Label8").text

    dictionary = {
        "address": address,
        "person": person,
        "phone": phone,
        "email": email,
        "expiryDate": expiryDate,
        "workLocation": workLocation != '' and workLocation or 'Không rõ'
    }

    return dictionary


def ProfileRequirements(soup):
    minAge = soup.find("span", id="cphMainContent_lblMinAge").text
    maxAge = soup.find("span", id="cphMainContent_lblMaxAge").text
    gender = soup.find("span", id="cphMainContent_lblGenderRequired").text
    educationLevel = soup.find("span", id="cphMainContent_lblEducationLevelIDRequired").text
    experience = soup.find("span", id="cphMainContent_lblExperienceRequired").text
    orther = soup.find("span", id="cphMainContent_lblOtherInfoRequired").text

    dictionary = {
        "minAge": minAge,
        "maxAge": maxAge != '' and maxAge or 'Không giới hạn',
        "gender": gender != '' and gender or 'Nam/ Nữ',
        "educationLevel": educationLevel,
        "experience": experience != '' and RemoveSpace(experience) or 'Không yêu cầu kinh nghiệm',
        "orther": orther != '' and RemoveSpace(orther) or 'Không có'
    }

    return dictionary


def AllInformation(url):
    soup = GetSoup(url)

    dictionary = {
        "JobDesciption": JobDesciption(soup),
        "ContactInformation": ContactInformation(soup),
        "ProfileRequirements": ProfileRequirements(soup),
        "Seach": deletestopword.RemoveStopWord(JobDesciption(soup)['description'])
    }

    return dictionary


def GetID(url):
    return url.replace(".html", "").split("-")[-1]
