age_list=[24,25,26,27,28]
print(age_list)
name_list=["Anu","Rahul","Meena","Arun","Vijay"]
print(name_list)
name_list.append("Yazhini")
print(name_list)
age_list.insert(2,30)
print(age_list)
name_list.remove("Yazhini")
print(name_list)
age_list.pop()
print(age_list)
age_list.extend([29,30,26])
print(age_list)
age_list.sort(reverse=True)
print(age_list)
print("Maximum age:",max(age_list))
print("minimum age:",min(age_list))
print("sum of all ages:",sum(age_list))
print(name_list[0])
print(name_list[-1])
print(name_list[2:5])
print(name_list[::-1])
student_marks={
    "Anu":75,
    "Rahul":88,
    "Meena":92,
    "Arun":68,
    "Vijay":85

    }
print(student_marks)
print("Meena's mark:",
      student_marks["Meena"])

student_marks["Janani"]=80
print(student_marks)
student_marks["Arun"]=82
print(student_marks)

print(student_marks.keys())
print(student_marks.values())
print(student_marks.items())

my_set={'a','e','i','o','u','a','a','i'}
print(my_set)


my_set.add('s')
print(my_set)

set1={1,3,5,7,9}
set2={2,3,5,8,10}

print("set1:",set1)
print("set2:",set2)
print("Union:",set1.union(set2))
print("Intersection:",set1.intersection(set2))

score=float(input("Enter your score(0-10):"))
if score<0 or score>10:
    print("invalid score.please enter a score between 0 and 10.")

elif score>7:
    print("Above Average")
    print("Great performance! Keep it up.")

elif score>=4:
    print("Average")
    print("Good performance! Keep practicing.")

else:
    print("Below Average")
    print("Need to improve your performance. Consistent practice will lead to better results.")
    
      
