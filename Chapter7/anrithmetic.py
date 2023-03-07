'''
จัดเก็บและเรียกใช้ฟังก์ชันในโมดูล เพื่อความสะดวกในการเรียกใช้งาน ควรจัดหมวดหมู่
ฟังก์ชันไว้ในไฟล์เดียวกันเป็นไฟล์โมดูล .py และสามารถเรียกฟังก์ชันเหล่านี้ไปใช้ในโปรแกรมต่าง ๆ 
ได้ด้วยการ import หรือ from
'''
def add(x,y):
    return x+y
def division(x,y):
    return x/y
def multiply(x,y):
    return x*y
def subtract(x,y):
    return x-y

# ดูการใช้ในไฟล์ math.py
