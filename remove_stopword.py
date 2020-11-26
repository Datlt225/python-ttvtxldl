# -*- coding: utf-8 -*-
from underthesea import word_tokenize  # ghép những chữ có nghĩa lại với nhau
import string  # lấy những kí tự đặc biệt


# lấy stop word
def get_stopword():
    stop_word = []

    # lấy tất cả stop word trong file
    with open("vietnamese-stopwords.txt", encoding="utf-8") as file:
        text = file.read()

        for word in text.split():
            stop_word.append(word)

        file.close()

    # trả về stop word lấy từ file và những kí tự đặc biệt từ string.punctuation
    return stop_word + list(string.punctuation)


# xóa stop word
def remove_stopword(text, stop_word):
    text = word_tokenize(text)  # ghép những từ có nghĩa lại với nhau
    result = ""

    for word in text:
        if word not in stop_word:
            result += word + " "

    return result


# my_string = "Dân trí Theo kết luận thanh tra tài chính, hiệu trưởng trường tiểu học Trần Văn Ơn, Q. Tân Bình, TPHCM-nơi phụ huynh cầm băng rôn đòi minh bạch tài chính- đã để ngoài sổ sách trên 735 triệu đồng... Ngày 11/11, Phòng GD&ĐT quận Tân Bình, TPHCM cùng các cơ quan thẩm quyền công bố kết luận thanh tra tài chính tại Trường tiểu học Trần Văn Ơn - nơi xảy ra sự việc phụ huynh cầm băng rôn đến yêu cầu minh bạch tài chính vào tháng 6 vừa rồi. Phụ huynh Trường tiểu học Trần Văn Ơn, Quận Tân Bình, TPHCM cầm băng rôn yêu cầu Hiệu trưởng công khai minh bạch tài chính Theo kết luận, bà Nguyễn Thị Hồng Yến, hiệu trưởng nhà trường có hành vi vi phạm nghiêm trọng trong công tác quản lý điều hành hoạt động tài chính tại trường, khi bỏ ngoài sổ sách kế toán hơn 735 triệu đồng. Cụ thể, nhà trường để ngoài sổ sách các khoản như: Bảo hiểm y tế, Bảo hiểm tai nạn của học sinh, sổ liên lạc điện tử, Anh văn tự chọn, các nguồn thu theo thỏa thuận... Trường tiểu học Trần Văn Ơn còn có rất nhiều sai phạm trong công tác hạch toán kế toán như: Hạch toán không đầy đủ hay sai số liệu theo nghiệp vụ tài chính phát sinh, không thực hiện báo cáo quyết toán ngân sách năm 2019 và 6 tháng đầu năm 2020, báo cáo lao động tiền lương quý 1,2/2020… Hiệu trưởng không tổ chức họp viên chức, nhân viên để thống nhất nội dung thảo luận chi tiêu nội bộ năm 2019, để làm cơ sở ban hành Quy chế; không công khai Quy chế chi tiêu nội bộ năm 2020 đến tập thể giáo viên, nhân viên của trường là sai quy định... Ngoài ra, trường còn thanh lý một số tài sản nhưng kế toán không nhập vào nguồn thu; nhà trường vẫn giữ tiền thừa và để ngoài sổ sách kế toán từ những khoản thu: về thu hộ, chi hộ; thu tiền học tiếng Anh với giáo viên nước ngoài; tiền kỹ năng sống, trong đó có những khoản tiền thừa từ năm học 2015-2016 chưa trả lại phụ huynh… UBND quân Tân Bình đề nghị thanh tra tham mưu cho quận chuyển đơn tố cáo của công dân đối với hiệu trưởng Nguyễn Thị Hồng Yến sang Công an quận xử lý Về hướng xử lý, hiệu trưởng cùng nguyên kế toán và thủ quỹ của trường cũng phải nộp lại cho trường khoản tiền theo hành vi sai phạm. Từ bản kết luận thanh tra, Chủ tịch UBND Q. Tân Bình đề nghị trưởng đoàn thanh tra tiếp tục làm rõ các sai phạm của hiệu trưởng và những người liên quan để áp dụng hình thức kỷ luật. Ngoài ra, đề nghị trưởng đoàn thanh tra tham mưu cho quận chuyển đơn tố cáo của công dân đối với bà Yến sang Công an quận xử lý đơn theo thẩm quyền. Trường hợp đủ cơ sở sẽ chuyển sang cơ quan điều tra xử lý để kiến nghị khởi tố. Trước đó, vào ngày 30/6 vừa qua, một số phụ huynh Trường tiểu học Trần Văn Ơn, Q.Tân Bình đến trường, cầm băng rôn đề nghị nhà trường phải minh bạch về tài chính , trả lại những khoản tiền dư. Từ sự việc này, các cơ quan thẩm quyền đã vào cuộc, tháng 9/2020, bà Nguyễn Thị Hồng Yến đã bị t ạm đình chỉ công tác trong vòng 90 ngày , để đoàn Thanh tra Nhà nước quận làm công tác thanh tra từ đơn phản ánh của phụ huynh. Lê Đăng Đạt Tin liên quan Vụ phụ huynh đòi minh bạch tài chính: Đình chỉ hiệu trưởng 90 ngày Phụ huynh kéo đến trường, cầm băng rôn yêu cầu minh bạch tài chính Từ khóa: hiệu trưởng sai phạm tài chính phản đối"
# print(my_string)
# print(word_tokenize(my_string))
# print(remove_stopword(my_string, get_stopword()))
