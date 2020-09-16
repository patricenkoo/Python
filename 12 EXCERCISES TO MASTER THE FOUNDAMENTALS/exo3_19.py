class Student:
    def __init__(self, first_name, last_name, student_id, courses):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.courses = courses

    def get_gpa():
        total_grade_points = 0
        credit_hour_count = 0
        for course in self.courses:
            if course.get_grade(): 
                total_grade_points += course.get_gpa_points()
                credit_hour_count += course.get_credit_hours()
        return total_grade_points / credit_hour_count 

class Course:
    def __init__(self, name, credit_hours, grade):
        self.name = name
        self.credit_hours = credit_hours
        self.grade = grade

    def get_gpa_points(self):
        return self.credit_hours * self.grade

    def get_credit_hours(self):
        return self.credit_hours

    def get_grade(self):
        return self.grade

def find_with_gpa(students, min_gpa):
    result_list = []
    for student in students:
        if student.get_gpa() >= min_gpa:
            result_list.append(student)
    return result_list

def create_diff_attributes(students):
    total = 0.0
    for student in students:
        total += student.get_gpa()
    average_gpa = total / len(students)

    for student in students:
        student.gpa_diff = student.get_gpa() - average_gpa

def create_diff_attributes(students):
    for this_student in students:
        total = 0.0
        for other_student in students:
            total += other_student.get_gpa()
        average_gpa = total / len(students)
        this_student.gpa_diff = this_student.get_gpa() - average_gpa
