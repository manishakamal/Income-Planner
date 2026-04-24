# profile.py

from utils import get_number
from file_handler import save_data

def enter_profile():
    print("\n--- Personal Details ---")
    name = input("Your name: ")
    age  = input("Your age: ")
    job  = input("Your job: ")

    print("\n--- Income Details ---")
    total_income = get_number("Your total monthly income (Rs): ")

    print("\n--- Family Details ---")
    family     = input("Number of family members (including you): ")
    dependents = int(get_number("Number of dependents (kids/elderly): "))

    print("\n--- Loan Details ---")
    has_loan  = input("Do you have a loan? (yes/no): ").lower()
    loan_emi  = 0
    loan_type = "None"
    if has_loan == "yes":
        loan_type = input("Loan type (Home/Car/Personal/Education): ")
        loan_emi  = get_number("Monthly EMI amount (Rs): ")

    print("\n--- Insurance Details ---")
    has_insurance = input("Do you have insurance? (yes/no): ").lower()
    insurance = 0
    if has_insurance == "yes":
        insurance = get_number("Monthly premium (Rs): ")

    print("\n--- Your Goal ---")
    print("1. Save more")
    print("2. Balanced")
    print("3. Spend more")
    choice = input("Choose (1/2/3): ")
    goals  = {"1": "Save more", "2": "Balanced", "3": "Spend more"}
    goal   = goals.get(choice, "Balanced")

    data = {
        "name"        : name,
        "age"         : age,
        "job"         : job,
        "total_income": total_income,
        "family"      : family,
        "dependents"  : dependents,
        "loan_type"   : loan_type,
        "loan_emi"    : loan_emi,
        "insurance"   : insurance,
        "goal"        : goal
    }

    save_data(data)
    print("\nProfile saved!")
    return data

def show_profile(data):
    print("\n--- Your Saved Profile ---")
    print("Name      :", data["name"])
    print("Age       :", data["age"])
    print("Job       :", data["job"])
    print("Family    :", data["family"], "members,", data["dependents"], "dependents")
    print("Income    : Rs", data["total_income"])
    print("Loan      :", data["loan_type"], "- EMI Rs", data["loan_emi"])
    print("Insurance : Rs", data["insurance"], "/mo")
    print("Goal      :", data["goal"])
