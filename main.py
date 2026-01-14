from pyscript import document

def compute_average(event):
    try:
        score1 = float(document.getElementById("score1").value)
        score2 = float(document.getElementById("score2").value)
    except:
        document.getElementById("average").innerText = "—"
        document.getElementById("result").innerText = "Invalid input"
        return

    final_average = (score1 + score2) / 2

    if final_average >= 90:
        status = "Outstanding"
    elif final_average >= 80:
        status = "Satisfactory"
    elif final_average >= 75:
        status = "Needs Improvement"
    else:
        status = "Did Not Pass"

    document.getElementById("average").innerText = str(round(final_average, 2))
    document.getElementById("result").innerText = status