group = []

ticket_catalog = {
    "Kids": {"t_price": 0, "cat_age": 3},
    "Junior": {"t_price": 14, "cat_age": 13},
    "Regular": {"t_price": 23, "cat_age": 65},
    "Senior": {"t_price": 18, "cat_age": float('inf')}
}

ticket = {
    "Kids": 0,
    "Junior": 0,
    "Regular": 0,
    "Senior": 0
}

def ticket_price(age:int):
    for category in ticket_catalog:
        if age < ticket_catalog[category]["cat_age"]:
            price = ticket_catalog[category]["t_price"]
            break
    return price, category

def valid_data(data: str):
    valid: bool = False
    try:
        int(data)
        valid = True
    except ValueError:
        valid = False
    return valid

def age_entry():
    while True:
        age_input = input("Enter your age: ")
        if age_input == "":
            break
        elif valid_data(age_input):
            age = age_input
            group.append(ticket_price(int(age)))
        else:
            age_input = input("Invalid data entry, try again: ")
            age = age_input
            group.append(ticket_price(int(age)))
    return group

def final_ticket(group):  
    total_price = 0
    for price, category in group:
        total_price += price
        ticket[category] += 1

    print(f"Enjoy yor visit!\nTotal tickets: {len(group)}\n")

    for cat in ticket:
        if ticket[cat] != 0:
            print(f"{ticket[cat]} {cat} x {ticket_catalog[cat]["t_price"]:5.2f} $ = {ticket_catalog[cat]["t_price"] * ticket[cat]:4.2f} $\n")
                    
    print(f"TOTAL PRICE: {total_price:4.2f} $")

final_ticket(age_entry())                  