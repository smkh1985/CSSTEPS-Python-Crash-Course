def print_ticket(name, seat, gate="A1"):
    print(f"{name}: seat {seat}, gate {gate}")
    
passenger = {"seat": "12A", "name": "Emma"}
print_ticket(**passenger)
passenger["gate"] = "B4"
print_ticket(**passenger)
