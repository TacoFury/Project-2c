print("Please enter an amount in cents less than a dollar.")
change = float(87)
print("Your change will be:")
print("Q:", change // 25)
change = change % 25
print("D:", change // 10)
change = change % 10
print("N:", change // 5)
change = change % 5
print("P:", change // 1)
change = change % 1
