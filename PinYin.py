from pypinyin import pinyin, lazy_pinyin
import pypinyin
import re
import xlrd
import xlwt

pattern_english = re.compile(r'[a-zA-Z1-9]+')
pattern_chinese = re.compile(r'[\u4e00-\u9fa5]+')

src_file = open("soccer.txt", encoding = 'utf-8')

book = xlwt.Workbook(encoding = 'utf-8')
sheet = book.add_sheet('Soccer')
sheet.write(0,0,'English')
sheet.write(0,1,'Chinese')
sheet.write(0,2,'Pin Yin')


line_number = 1
for each_line in src_file:
    english_group = pattern_english.findall(each_line)
    english = ''
    if english_group is not None:
        english = (' ').join(english_group)
    chinese_group = pattern_chinese.findall(each_line)
    chinese = ''
    if chinese_group is not None:
        chinese = (' ').join(chinese_group)
    pin_yin_group = pinyin(chinese)
    pin_yin = ''
    if pin_yin_group is not None:
        for each_pinyin in pin_yin_group:
            pin_yin =  pin_yin + ('').join(each_pinyin) + ' '
    row = sheet.row(line_number)
    row.write(0, english)
    row.write(1, chinese)
    row.write(2, pin_yin)
    line_number = line_number + 1

book.save('soccer.xls')
