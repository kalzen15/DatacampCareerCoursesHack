import os
files_list=[]
file_names=os.listdir('./Courses')

for filename in file_names:
    file=open('./Courses/'+filename,'r')
    files_list.append([line for line in file.readlines()])

for index1 in range(len(files_list)-1):
    for index in range(len(files_list)-1-index1):
        if len(files_list[index]) <len(files_list[index+1]):
            temp=files_list[index+1]
            temp2=file_names[index+1]
            files_list[index+1]=files_list[index]
            file_names[index+1]=file_names[index]
            files_list[index]=temp
            file_names[index]=temp2



for index in range(len(files_list)-1):
    for item in files_list[index]:
        for sub_index in range(index+1,len(files_list)):
            if item in files_list[sub_index]:
                files_list[sub_index].remove(item)

for index1 in range(len(files_list)-1):
    for index in range(len(files_list)-1-index1):
        if len(files_list[index]) <len(files_list[index+1]):
            temp=files_list[index+1]
            temp2=file_names[index+1]
            files_list[index+1]=files_list[index]
            file_names[index+1]=file_names[index]
            files_list[index]=temp
            file_names[index]=temp2


print(file_names)
print(files_list)

for i in files_list:
    print(len(i))
if not os.path.exists('./Edited'):
    os.mkdir('./Edited')
index=0
order_file=open('./Edited/order_of_courses.txt','w')
for filename in file_names:
    file=open('./Edited/'+filename,'w')
    for item in files_list[index]:
        file.write(item)
    index+=1
    order_file.write(filename+'\n')
