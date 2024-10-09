def transmute_raw_score(raw_score_percentage):
    if raw_score_percentage >= 96:
        return 100
    elif raw_score_percentage >= 91:
        return 95
    elif raw_score_percentage >= 86:
        return 90
    elif raw_score_percentage >= 81:
        return 85
    elif raw_score_percentage >= 76:
        return 80
    elif raw_score_percentage >= 71:
        return 75
    elif raw_score_percentage >= 66:
        return 70
    elif raw_score_percentage >= 61:
        return 65
    elif raw_score_percentage >= 56:
        return 60
    else:
        return 50  # Or whatever the minimum failing grade is
