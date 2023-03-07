import math #import ฟังก์ชัน math ทางคณิตศาสตร์
from math import cos,tan,log,sqrt #รูปแบบที่สอง
import statistics #import ฟังก์ชัน statistics ฟังก์ชันาถิติ
ls=[2,7,13,3,8,20,4,9] #สร้างลิสต์และเก็บค่าเริ่มต้น
print(math.log10(100)) #เรียกฟังก์ชัน log10 หาค่าลอการทึมฐาน 10 ของค่า 100
print(math.sin(0.5)) #เรียกฟังก์ชัน sin() หาค่าไซน์ของค่า 0.5
print(math.exp(3)) #เรียกฟังก์ชัน exp() หาเอ็กซ์โพเนนเชียลของค่า 3
print(statistics.mean(ls)) #เรียงฟังก์ชัน mean() หาค่าเฉลี่ยของตัวเลขภายในตัวแปร ls 

print("from math import cos,tan,log,sqrt รูปแบบที่สอง")
print(cos(2))
print(tan(0.9))
print(sqrt(100))
print(log(10))
#รูปแบบที่ 2 
# from moduleName import func_name1,[func_name2]
''' moduleName ชื่อโมดูลในไลบรารีหรือไฟล์โมดูลภายนอกที่ต้องการเรียกใช้งาน
    func_name1 ฟังก์ชันในโมดูลที่ต้องการเรียกใช้งานซึ่งมีมากว่า 1 ฟังก์ชัน 
    ถ้าเราต้องการเรียกใข้ทุกฟังก์ชันในโมดูล ในการใช่คีย์เวิร์ด from ฟังก์ชัน impotr * แทนชื่อฟังก์ชัน โดยมีรูปแบบคำสั่ง'''
