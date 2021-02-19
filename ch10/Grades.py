# 10.3 Encapsulation and Information Hiding

from Student import UG, Grad

# Figure 10-6 from page 198
class Grades(object):

    def __init__(self):
        """Create empty grade book"""
        self._students = []
        self._grades = {}
        self._is_sorted = True

    def add_student(self, student):
        """Assumes: student is of type Student
           Add student to the grade book"""
        if student in self._students:
            raise ValueError('Duplicate student')
        self._students.append(student)
        self._grades[student.get_id_num()] = []
        self._is_sorted = False

    def add_grade(self, student, grade):
        """Assumes: grade is a float
           Add grade to the list of grades for student"""
        try:
            self._grades[student.get_id_num()].append(grade)
        except:
            raise ValueError('Student not in mapping')

    def get_grades(self, student):
        """Return a list of grades for student"""
        try:
            return self._grades[student.get_id_num()][:]
        except:
            raise ValueError('Student not in mapping')

    # original version: returns sorted copy of list
    # def get_students(self):
    #     """Return a sorted list of the students in the grade book"""
    #     if not self._is_sorted:
    #         self._students.sort()
    #         self._is_sorted = True
    #     return self._students[:]
    
    # new version from later in chapter
    def get_students(self): 
        """Return the students in the grade book one at a time
            in alphabetical order"""
        if not self._is_sorted:
            self._students.sort()
            self._is_sorted = True
        for s in self._students:
            yield s
            
    # Finger exercise
    def get_students_above(self, min_average):
        """
        Return the students with an average grade > min_average
            one at a time
        """
        for student in self._students:
            average = 0.0
            tot = 0.0
            num_grades = 0
            for grade in self._grades[student.get_id_num()][:]:
                tot += grade
                num_grades += 1
                
            try:
                average = tot / num_grades
            except ZeroDivisionError:
                pass
            
            if average > min_average:
                yield student


def test_add_student():
    # Code from page 197
    course = Grades()
    course.add_student(Grad('Bernie Sanders'))
    course.add_student(Grad('Adam Grant'))
    
    # Iterate each element
    for s in course.get_students():
        print(s)
        
    print()
    
    # Store in generator and iterate
    students = course.get_students()
    for s in students:
        print(s)
    
    
# Figure 10-7 Generating a grade report
# Concatenates each report entry into one string (inefficent)
def grade_report(course):
    """Assumes course is of type Grades"""
    report = ''
    for s in course.get_students():
        tot = 0.0
        num_grades = 0
        for grade in course.get_grades(s):
            tot += grade
            num_grades += 1
        try:
            average = tot / num_grades
            report = f"{report}\n{s}'s mean grade is {average}"
        except ZeroDivisionError:
            report = f"{report}\n{s} has no grades"
    return report


# Appends each report entry into a list
def grade_report_list(course):
    """Assumes course is of type Grades"""
    report = []
    
    for s in course.get_students():
        tot = 0.0
        num_grades = 0
        for grade in course.get_grades(s):
            tot += grade
            num_grades += 1
            
        try:
            average = tot / num_grades
            entry = f"{s}'s mean grade is {average}"
        except ZeroDivisionError:
            entry = f"{s} has no grades"
        report.append(entry)
        
    return report


def test_grade_report():
    ug1 = UG('Jane Doe', 2021)
    ug2 = UG('Pierce Addison', 2041)
    ug3 = UG('David Henry', 2003)
    g1 = Grad('Billy Buckner')
    g2 = Grad('Bucky F. Dent')
    
    six_hundred = Grades()
    six_hundred.add_student(ug1)
    six_hundred.add_student(ug2)
    six_hundred.add_student(g1)
    six_hundred.add_student(g2)
    
    for s in six_hundred.get_students():
        six_hundred.add_grade(s, 75)
    six_hundred.add_grade(g1, 25)
    six_hundred.add_grade(g2, 100)
    six_hundred.add_student(ug3) # No grades
    
    print(grade_report(six_hundred))
    
    print()
    
    grades_list = grade_report_list(six_hundred)
    for entry in grades_list:
        print(entry)
    
    print()
        
    
def test_get_students_above():
    ug1 = UG('Jane Doe', 2021)
    ug2 = UG('Pierce Addison', 2041)
    ug3 = UG('David Henry', 2003)
    g1 = Grad('Billy Buckner')
    g2 = Grad('Bucky F. Dent')
    
    six_hundred = Grades()
    six_hundred.add_student(ug1)
    six_hundred.add_student(ug2)
    six_hundred.add_student(g1)
    six_hundred.add_student(g2)
    
    for s in six_hundred.get_students():
        six_hundred.add_grade(s, 75)
    six_hundred.add_grade(g1, 25)
    six_hundred.add_grade(g2, 100)
    six_hundred.add_student(ug3) # No grades
    
    for s in six_hundred.get_students_above(70.0):
        print(s)
    
        
if __name__ == "__main__":
    test_add_student()
    test_grade_report()
    test_get_students_above()
