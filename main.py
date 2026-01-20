from pyscript import Element
import random

def check_eligibility():
    registered = document.querySelector(
        'input[name="registered"]:checked'
    ).value
    medical = document.querySelector(
        'input[name="medical"]:checked'
    ).value
    grade = Element("grade").value
    section = Element("section").value

    result = Element("result")

    # Eligibility checks
    if registered != "yes":
        result.write("❌ Please register online to join the Intramurals.")
    elif medical != "yes":
        result.write("❌ Please secure a medical clearance.")
    elif grade == "" or int(grade) < 7 or int(grade) > 10:
        result.write("❌ Only students from Grades 7 to 10 are eligible.")
    elif section == "":
        result.write("❌ Please select your section.")
    else:
        teams = [
            "Blue Bears",
            "Red Bulldogs",
            "Yellow Tigers",
            "Green Hornets"
        ]
        team = random.choice(teams)

        result.write(
            "🎉 Congratulations! You are eligible to join the Intramurals.<br><br>"
            f"<strong>Grade & Section:</strong> {grade} - {section}<br>"
            f"<strong>Assigned Team:</strong> {team}"
        )
