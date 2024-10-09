def determine_numeric_grade(transmuted_score):
    numeric_grades = [
        (96, 1.00),
        (91, 1.25),
        (86, 1.50),
        (81, 1.75),
        (76, 2.00),
        (71, 2.25),
        (66, 2.50),
        (61, 2.75),
        (56, 3.00),
        (0, 5.00),
    ]

    for boundary, grade in numeric_grades:
        if transmuted_score >= boundary:
            return grade

    return 5.00
