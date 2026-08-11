has_enough_income = False
has_good_credit_score = True
has_criminal_record = True


if (has_enough_income or has_good_credit_score and not has_criminal_record):
    print("The loan is approved.")
elif (has_enough_income or has_good_credit_score and has_criminal_record):
    print("The loan is denied because client has crimainal record")
else:
    print("Loan not applied")
