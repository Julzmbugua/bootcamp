student = {
    'name': 'An Other',
    'langs': ['Python', 'JavaScript', 'PHP'],
    'age': 23
}

student2 = {
    'name': 'No Name',
    'langs': ['Python', 'Java', 'PHP'],
    'age': 24
}
# Task 1:

# Create a function add_student that takes a student dictionary as a parameter,
# and adds the student in a list of students.

students = []
def add_student(stud):
  students.append(stud)
  print(len(students))

add_student(student)
add_student(student2)

print(students)

# Task 2:

# Write a function oldest_student that finds the oldest student.

# def oldest_student:
#     if student.{3} > {}:
#     	pass

def oldest_student(students):

	oldest = 0


	for student in students:
		if student['age'] > oldest:
			oldest = student['age']
	return oldest
	# Print(oldest_student(students))

print(oldest_student(students))

# Write a function student_lang that takes in a parameter lang and returns a list containing names of students who know that language.

# def student_lang(lang):
#     pass

def student_lang(lang):
	name_list = []

	for student in students:
		if lang in student['langs']:
			name_list.append(student['name'])

	return name_list

print(student_lang("JavaScript"))
print(student_lang("PHP"))