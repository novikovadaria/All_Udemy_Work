"""
1 - amd
2 - or
3 - not
"""

# .......................... And LO.............
from operator import truediv


hight_income = True
good_credit = True

if hight_income and good_credit:
    print("Eligible For Loan")
else:
    print("Not Eligible For Loan")

# .............................Or LO.............................
if hight_income or good_credit:
    print("Eligible For Loan")
else:
    print("Not Eligible For Loan")

# ..............................Not LO....................
hight_income = True
good_credit = True
student = True

if not student:
    print("Eligible For Loan")
else:
    print("Not Elogable For Loan")
