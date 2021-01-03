def gradingStudents(grades):
    grade_list = []
    for grade in grades:
        if grade < 38:
            grade_list.append(grade)
        else:
            if grade % 5 == 3:
                    grade_list.append(grade + 2)
            elif grade % 5 == 4:
                    grade_list.append(grade + 1)
            else:
                grade_list.append(grade)
    return grade_list