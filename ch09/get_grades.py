# 9.2 Exceptions as a Control Flow Mechanism

# Figure 9-1 from page 175
def get_grades(fname):
    grades = []
    try:
        with open(fname, 'r') as grades_file:
            for line in grades_file:
                try:
                    line = line.rstrip()
                    grade = float(line)
                    grades.append(grade)
                except:
                    raise ValueError(f"Failed to convert '{line}' to float")     
    except IOError:
        raise ValueError(f"get_grades failed to open file {fname}")
    return grades

if __name__ == "__main__":
    try:
        grades = get_grades('quiz1grades.txt')
        grades.sort()
        median = grades[len(grades)//2]
        print(f"Median grade is {median}")
    except ValueError as error_msg:
        print(f"Error: {error_msg}")