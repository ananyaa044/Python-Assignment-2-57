# 30. Calculate electricity charges using slabs and nested if statements.

units = float(input("Enter electricity units consumed: "))

if units < 0:
    print("Units cannot be negative.")
else:
    if units <= 100:
        charge = units * 1.5
    else:
        charge = 100 * 1.5
        if units <= 200:
            charge += (units - 100) * 2.5
        else:
            charge += 100 * 2.5
            if units <= 300:
                charge += (units - 200) * 4
            else:
                charge += 100 * 4
                charge += (units - 300) * 6
    print("Electricity charge = Rs.", round(charge, 2))
