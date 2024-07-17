import shutil
with open('file1.txt','w') as file_1:
    file_1.write("this is my file 1 and it has the conteny written in for my first file.")

with open('file2.txt','w') as file_2:
    file_2.write("this is my file 2 and it has the conteny written in for my second file.")
    
file1_path = 'file1.txt'
file2_path = 'file2.txt'

with open(file1_path,'r') as file1, open(file2_path, 'r') as file2:
    file1_content = file1.read()
    file2_content = file2.read()
    


 
with open ('file3.txt', 'w') as fp:
    fp.write(file1_content + "\n-\n" + file2_content)    
    
shutil.copy('file3.txt','user')

with open ('file3.txt') as f1:
    content_of_file1, partition1, content_of_file2 = f1.read().partition("-")
with open('file4.txt','w') as f2:
    f2.write(content_of_file1)
with open('file5.txt','w') as f3:
    f3.write(content_of_file2)

