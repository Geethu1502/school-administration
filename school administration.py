#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
def write_into_csv(info_list):
    with open("x.csv","a",newline=" ") as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
             writer.writerow("Name", "Age", "Contact_number", "Email_id")
        writer.writerow(info_list)

condition=True
student_num=1
while(condition):
    student_info=input("enter the student information for student {} in the following format (Name Age Contact_number Email_id):".format(student_num))
    student_info_list=student_info.split(" ")
    print(" the entered information is -\nName:{}\nAge:{}\nContact_number:{}\nEmail_id:{}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
    choice_check=input("is the entered information correct? (yes/no):")
    if choice_check=="yes":
        write_into_csv(student_info_list) 
        x=input("enter (yes/no) if you want to enter information of another student:")
        if x=="yes":
            condition = True
            student_num=student_num+1
        elif x=="no":
            condition = False  
    elif choice_check=="no":
        print("please re enter the values")
    


# In[ ]:




