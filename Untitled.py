#!/usr/bin/env python
# coding: utf-8

# In[62]:


print('Hello from Jupyter')
my_str = 'Hello'
my_int = 16

print(my_str)
print(my_int)
my_str
my_str
my_int
number_of_apples = 5
if number_of_apples < 1:
    print('You have no apples')
elif number_of_apples == 1:
    print('You have one apple')
elif number_of_apples < 4:
    print('You have a few apples')
else:
    print('You have many apples!')
student_names = ['Alice', 'Bob', 'Carol', 'Dave']
student_names[1]
student_names[0]
student_names[-1]
student_names[0:2]
student_names[1:3]
student_names[:2]
student_names[2:]
student_names.append('Esther')
student_names
student_names.insert(2, 'Xavier')
student_names
del student_names[2]
student_names
student_names.append('Esther')
student_names.append('Esther')
student_names
student_names = ['Alice', 'Bob', 'Carol', 'Dave']

for student_name in student_names:
    print('Hello ' + student_name + '!')
long_names = []
for student_name in student_names:
    # This is our criterion
    if len(student_name) > 4:
        long_names.append(student_name)

long_names
student_names = ['Alice', 'Bob', 'Carol', 'Dave']

student_pairs = []
for student_name_0 in student_names:
    for student_name_1 in student_names:
        student_pairs.append(
            (student_name_0, student_name_1)
        )

student_pairs
student_pairs[0]
student_names = ['Alice', 'Bob', 'Carol', 'Dave']

student_pairs = []
for student_name_0 in student_names:
    for student_name_1 in student_names:
        # This is the criterion we added
        if student_name_0 != student_name_1:
            student_pairs.append(
                (student_name_0, student_name_1)
            )

student_pairs
student_grade = ('Alice', 'Spanish', 'A-')
student_grade
student_grade[0]
# student_grade.append('IU Bloomington')
# del student_grade[2]
# student_grade[2] = 'C'
student_grade = ('Alice', 'Spanish', 'A-')
student_name, subject, grade = student_grade

print(student_name)
print(subject)
print(grade)
student_grades = [
    ('Alice', 'Spanish', 'A'),
    ('Bob', 'French', 'C'),
    ('Carol', 'Italian', 'B+'),
    ('Dave', 'Italian', 'A-'),
]

for student_name, subject, grade in student_grades:
    if grade.startswith('A'):
        print('Congratulations', student_name,
              'on getting an', grade,
              'in', subject)
for student_grade in student_grades:
    if student_grade[2].startswith('A'):
        print('Congratulations', student_grade[0],
              'on getting an', student_grade[2],
              'in', student_grade[1])
foreign_languages = {
    'Alice': 'Spanish',
    'Bob': 'French',
    'Carol': 'Italian',
    'Dave': 'Italian',
}
foreign_languages['Carol']
# foreign_languages['Zeke']
'Zeke' in foreign_languages
'Alice' in foreign_languages
'alice' in foreign_languages
foreign_languages['Esther'] = 'French'
foreign_languages
del foreign_languages['Bob']
foreign_languages
foreign_languages['Esther'] = 'Italian'
foreign_languages
for key in foreign_languages:
    value = foreign_languages[key]
    print(key, 'is taking', value)
for key, value in foreign_languages.items():
    print(key, 'is taking', value)
student_grade = ('Alice', 'Spanish', 'A')
student_name, subject, grade = student_grades[0]
print(student_name, 'got a grade of', grade, 'in', subject)
record = {
    'name': 'Alice',
    'subject': 'Spanish',
    'grade': 'A',
}
print(record['name'],
      'got a grade of', record['grade'],
      'in', record['subject'])
student_grades = [
    ('Alice', 'Spanish', 'A'),
    ('Bob', 'French', 'C'),
    ('Carol', 'Italian', 'B+'),
    ('Dave', 'Italian', 'A-'),
]
student_grades[1]
student_grades[1][2]
student_grade_records = []
for student_name, subject, grade in student_grades:
    record = {
        'name': student_name,
        'subject': subject,
        'grade': grade,
    }
    student_grade_records.append(record)
    
student_grade_records
student_grade_records[1]
student_grade_records[1]['grade']
for record in student_grade_records:
    if record['grade'].startswith('A'):
        print('Congratulations', record['name'], 
              'on getting an', record['grade'], 
              'in', record['subject'])
foreign_language_grades = {}
for student_name, subject, grade in student_grades:
    record = {
        'subject': subject,
        'grade': grade,
    }
    foreign_language_grades[student_name] = record
    
foreign_language_grades
foreign_language_grades['Alice']
foreign_language_grades['Alice']['grade']
student_course_grades = {}
for student_name, subject, grade in student_grades:
    student_course_grades[student_name, subject] = grade
    
student_course_grades
student_course_grades['Alice', 'Math'] = 'A'
student_course_grades['Alice', 'History'] = 'B'
student_course_grades
student_report_cards = {}
for student_name, subject, grade in student_grades:
    # If there is no report card for a student,
    # we need to create a blank one
    if student_name not in student_report_cards:
        student_report_cards[student_name] = {}
    student_report_cards[student_name][subject] = grade
student_report_cards
student_report_cards['Alice']['Math'] = 'A'
student_report_cards['Alice']['History'] = 'B'
student_report_cards
student_report_cards['Alice']


# In[ ]:





# In[ ]:





# In[ ]:




