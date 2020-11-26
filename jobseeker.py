import requests
import re
from bs4 import BeautifulSoup


def RemoveSpace(text):
    text = re.sub('[!@#$+*-]', '', text)
    return ' '.join(text.split())


def GetSoup(url):
    # Get response
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html5lib')

    return soup


def GetLink(url):
    soup = GetSoup(url)
    fullLink = []
    links = soup.find_all('header', class_='job')

    for i in links:
        fullLink.append('http://vieclam.laodong.com.vn' + i.h3.a['href'])

    return fullLink


URL = 'http://vieclam.laodong.com.vn/nguoi-lao-dong/tran-luong-ngoc-tram-12880.html'


def Infomation(soup):
    fullName = soup.find('span', id='cphMainContent_lblFullName').text
    birthday = soup.find('span', id='cphMainContent_lblDOB').text
    gender = soup.find('span', id='cphMainContent_lblGender').text
    phone = soup.find('span', id='cphMainContent_lblPhone').text
    email = soup.find('span', id='cphMainContent_lblEmail').text
    address = soup.find('span', id='cphMainContent_lblAddress').text

    dictionary = {
        'fullName': fullName,
        'birthday': birthday,
        'gender': gender,
        'phone': phone != '' and phone or 'Không có',
        'email': email,
        'address': RemoveSpace(address)
    }

    return dictionary


def Experience(soup):
    educationLevel = soup.find('span', id='cphMainContent_lblEducationLevelID').text
    qualification = soup.find('span', id='cphMainContent_lblQualificationID').text
    languageProficiency = soup.find('span', id='cphMainContent_lblLanguageProficiency').text
    itProficiency = soup.find('span', id='cphMainContent_lblITProficiency').text
    specialized = soup.find('span', id='cphMainContent_lblSpecialized').text
    experiences = soup.find('span', id='cphMainContent_lblExperiences').text

    dictionary = {
        'educationLevel': educationLevel,
        'qualification': qualification != '' and qualification or 'Không rõ',
        'languageProficiency': languageProficiency != '' and languageProficiency or 'Không rõ',
        'itProficiency': itProficiency != '' and itProficiency or 'Không rõ',
        'specialized': specialized != '' and specialized or 'Không rõ',
        'experiences': educationLevel != '' and RemoveSpace(experiences) or 'Không rõ'
    }

    return dictionary


def CareerAspirations(soup):
    expectedPosition = soup.find('span', id='cphMainContent_lblExpectedPosition').text
    expectedJobLevel = soup.find('span', id='cphMainContent_lblExpectedJobLevelID').text
    expectedJobCategory = soup.find('span', id='cphMainContent_lblExpectedJobCategoryID').text
    expectedSalaryRange = soup.find('span', id='cphMainContent_lblExpectedSalaryRangeID').text
    expectedCompanyType = soup.find('span', id='cphMainContent_lblExpectedCompanyTypeID').text
    expectedWorkLocation = soup.find('span', id='cphMainContent_lblExpectedWorkLocationID').text
    availableFrom = soup.find('span', id='cphMainContent_lblAvailableFrom').text
    moreInfo = soup.find('span', id='cphMainContent_lblMoreInfo').text

    dictionary = {
        'expectedPosition': expectedCompanyType != '' and RemoveSpace(expectedPosition) or 'Không có',
        'expectedJobLevel': expectedJobLevel,
        'expectedJobCategory': RemoveSpace(expectedJobCategory),
        'expectedSalaryRange': expectedSalaryRange,
        'expectedCompanyType': expectedCompanyType != '' and RemoveSpace(expectedCompanyType) or 'Không có',
        'expectedWorkLocation': expectedWorkLocation,
        'availableFrom': availableFrom,
        'moreInfo': moreInfo != '' and RemoveSpace(moreInfo) or 'Không có'
    }

    return dictionary


def GetID(url):
    return url.replace(".html", "").split("-")[-1]


def AllInformation(url):
    soup = GetSoup(url)
    dictionary = {
        'Infomation': Infomation(soup),
        'Experience': Experience(soup),
        'CareerAspirations': CareerAspirations(soup)
    }

    return dictionary
