# budget.py

def level(amt):
    if amt < 500:   return "Very Low"
    if amt < 2000:  return "Low"
    if amt < 5000:  return "Moderate"
    if amt < 10000: return "High"
    return "Very High"

def show_budget(data):
    income     = float(data["total_income"])
    loan_emi   = float(data["loan_emi"])
    insurance  = float(data["insurance"])
    goal       = data["goal"]
    dependents = int(data["dependents"])

    fixed     = loan_emi + insurance
    available = income - fixed

    if available <= 0:
        print("\nYour loan EMI and insurance exceed your income!")
        return

    if goal == "Save more":
        savings_pct = 0.25
        invest_pct  = 0.10
    elif goal == "Balanced":
        savings_pct = 0.20
        invest_pct  = 0.07
    else:
        savings_pct = 0.12
        invest_pct  = 0.05

    spend_pct = 1 - savings_pct - invest_pct

    categories = {
        "Grocery & Food"  : 0.20 + (0.02 * dependents),
        "Home & Rent"     : 0.22,
        "Transport"       : 0.08,
        "Utilities"       : 0.07,
        "Health"          : 0.07 if dependents > 0 else 0.05,
        "Education"       : 0.05 if dependents > 0 else 0.02,
        "Weekend Outings" : 0.08,
        "Personal / Self" : 0.07,
        "Clothing"        : 0.04,
        "Miscellaneous"   : 0.05,
    }

    total_cat = sum(categories.values())
    spending  = {k: round((v / total_cat) * spend_pct * available, 2) for k, v in categories.items()}

    savings_amt = round(savings_pct * available, 2)
    invest_amt  = round(invest_pct  * available, 2)

    print("\n====================")
    print("  Budget for", data["name"])
    print("====================")
    print("  Income    : Rs", income)
    if loan_emi > 0:
        print("  Loan EMI  : Rs", loan_emi, "("+data["loan_type"]+")")
    if insurance > 0:
        print("  Insurance : Rs", insurance)
    print("  Available : Rs", available)
    print("--------------------")
    print("  Category         Amount   Level")
    print("--------------------")
    print(f"  {'Savings':<16} Rs{savings_amt:>7.0f}  {level(savings_amt)}")
    print(f"  {'Investment/FD':<16} Rs{invest_amt:>7.0f}  {level(invest_amt)}")
    for cat, amt in spending.items():
        print(f"  {cat:<16} Rs{amt:>7.0f}  {level(amt)}")
    print("====================")
