#Tuple
gender=("Nam","Nữ","Khác")
print(gender[0])
#dictionary
student ={
    'id':1,
    'full_name': 'NguyenVanA'
}   
print(student["id"])
print(student.get('id2','Nhập ngu vcl'))
# chua ton tai la them moi, co roi thi cap nhat
student['email']='aiosima'
student['full_name']='hehe'  

student.pop('email')
del student['id']
print(student)

# duyet
for key in student.keys():
    print(key)

for value in student.values():
    print(value)

for key,value in student.items():
    print(key,value)
    
d = {'A':1, 'B':2, 'C':3}
print(len(d))# in ra cap khoa: gtri
t = (1, 2)
t[0] = 99