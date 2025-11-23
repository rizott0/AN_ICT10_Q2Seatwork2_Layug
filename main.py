from pyscript import document

def AverageTwo(event):
    try:
        subjects = ("science", "filipino", "math", "english", "ict", "pe")

        grades = []

        for subj in subjects:
            value = document.getElementById(subj).value
            grades.append(float(value))

    except:
        document.getElementById("r_average").innerText = "Please complete all fields."
        return

    avg = sum(grades) / len(grades)

    document.getElementById("r_average").innerText = f"General Average: {avg:.2f}"