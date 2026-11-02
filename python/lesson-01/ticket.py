ticket_id = "INC002"
description = "User cannot connect to Wi-Fi"
Priority = "Low"
Status = "Open"
Action = "Process normally"
Assigned_to = "Anthony"

print("=== IT SUPPORT TICKET ===")
print(f"Ticket: {ticket_id}")
print(f"Problem: {description}")
print(f"Priority: {Priority}")
print(f"Status: {Status}")
print(f"Assigned to: {Assigned_to}")

if Priority == "High":
    print("Action: Escalation may be required")
elif Priority == "Medium":
    print("Action: Investigate soon")
else:
    print("Action: Process normally")


