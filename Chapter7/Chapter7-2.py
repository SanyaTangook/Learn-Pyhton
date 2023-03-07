#การกำหนดฟังก์ชันขึ้นเอง
'''รูปแบบ
def fnuction_name([parmeter lise]):
    statements
    [return Exception]
'''

def Hello():
    print("My name is python")

#วิธีเรียกใช้ฟังก์ชัน
Hello()

 #return คือ
''' return คือ การส่งค่ากลับไปยังตัวแปรในฟังช์ชั่น '''
def randomnumber(x):
    if len(x)<3:
        return
    if x == "100":
        print(True)
        return 1000
    else :
        return False

'''
n=randomnumber("100")
print("ผลที่ได้ " , n)
'''

def showlist():
    ls=[1,2,3,4,5,6,7,"A","B"]
    for i in ls:
        print(i,end=' ')

showlist()

#ขอบเขตของตัวแปรในฟังช์ชันและโปรแกรมหลัก
"""
ตัวแปรงที่เราประกาศขึ้นในโปรแกรมหลักและฟังช์ชัน จะมีขอบเขตในการเข้าถึงเพื่อใช้งานต่างกัน หากการเรียกใข้อยู่นอกเหนือขอบเขตตัวแปรง
ก็ไม่สามารถใช้งานได้ ขอบเขตของตัวแปร (Variable scope) ซึ่งแบ่งออกได้เป็น 3 ประเภท คือ โลคอล โกลบอล และนอนโลตอล
"""