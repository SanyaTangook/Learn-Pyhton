import anrithmetic
# อินพอร์ตโมดูลที่ต้องการเรียกใช้ฟังก์ชัน
print('10 + 8 =',anrithmetic.add(10,8))
print('8 - 5 = ',anrithmetic.subtract(8,5))
print('3 / 7 =',anrithmetic.division(3,7))
print('12 * 6 =',anrithmetic.multiply(12,6))
'''
จากตัวอย่างถ้าใช้คำสั่ง from anrithmetic import * แทน ในการเรียกใช้
ฟังก์ชัน anrithmetic จะไม่ต้องใช้ขื่อโมดูล anrithmetic นำหน้าฟังก์ชัน ซึ่งสามารถใช้ฟังก์ชันโดยตรง
เช่า add(10,8) หรือ multiply(12,6)
'''
