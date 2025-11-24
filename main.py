from js import document

def get_grade(id):
    value = document.getElementById(id).value
    return float(value) if value.strip() else None

def calculate_gwa(event=None):
    first_name = document.getElementById("first").value.strip() or "Student"
    last_name = document.getElementById("last").value.strip()
    full_name = f"{first_name} {last_name}" if last_name else first_name

    grades = []
    for subject in ["science", "filipino", "math", "pe", "english", "ict"]:
        grade = get_grade(subject)
        if grade is None or grade < 0 or grade > 100:
            document.getElementById("result").innerText = "Please enter all valid grades (0-100)!"
            return
        grades.append(grade)

    grade_average = sum(grades) / len(grades)

    if grade_average >= 90:
        remark = "Excellent"
    elif grade_average >= 75:
        remark = "Good"
    else:
        remark = "Fail"

    result_text = (
        f"Student Name: {full_name}\n"
        f"Science: {grades[0]}\n"
        f"Filipino: {grades[1]}\n"
        f"Math: {grades[2]}\n"
        f"PE: {grades[3]}\n"
        f"English: {grades[4]}\n"
        f"ICT: {grades[5]}\n\n"
        f"General Average: {grade_average:.2f}\n"
        f"Result: {remark}"
    )

    document.getElementById("result").innerText = result_text

def reset_form(event=None):
    for subject in ["first", "last", "science", "filipino", "math", "pe", "english", "ict"]:
        document.getElementById(subject).value = ""
    document.getElementById("result").innerText = "Enter grades above to calculate GWA."
