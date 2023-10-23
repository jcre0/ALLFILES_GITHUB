ammount_before_tax = int(input("How much is the bill withouth taxes? : "))
tax_toll = 14.975 / 100
ammount_after_tax = ammount_before_tax * tax_toll + ammount_before_tax
tax_ammount = ammount_after_tax -ammount_before_tax
percentage_tip = int(input("How much tip are you leaving (%): ")) / 100
tip_ammount = ammount_after_tax * percentage_tip
number_guests = int(input("How many guests will be paying their part of the bill? : "))
total_cost = float(ammount_after_tax + tip_ammount)
total_cost_guest = total_cost / number_guests

print(f"""
        Restaurant Creo
        Facture #149752
        ________________
ammount before tax = {ammount_before_tax}$\n
ammount after tax = {ammount_after_tax.__round__(2)}$\n
tip ammount = {tip_ammount.__round__(2)}$\n
taxes = {print({tax_ammount.__round__(2)})}$\n
number of guests paying their part = {number_guests}\n
total to pay for each guest = {total_cost_guest.__round__(2)}$


""")

