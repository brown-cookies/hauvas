def calculate_raw_score(request, context):
    student = request.user.student

    total_student_score = 0
    total_possible_score = 0

    for activity in context["activities"]:
        student_activity = activity.list.get(student=student)

        total_student_score += student_activity.score
        total_possible_score += activity.score

    for exam in context["exams"]:
        student_exam = exam.list.get(student=student)

        total_student_score += student_exam.score
        total_possible_score += exam.score

    if total_possible_score > 0:
        raw_score_percentage = (total_student_score / total_possible_score) * 100
    else:
        raw_score_percentage = 0

    return round(raw_score_percentage, 2)
