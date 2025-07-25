import datetime

TICKET_FILE = "tickets.txt"

def submit_ticket():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    issue = input("Describe your issue: ")

    ticket_id = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    ticket = f"""
------------------------------
Ticket ID: {ticket_id}
Name: {name}
Email: {email}
Issue: {issue}
Status: Open
Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
------------------------------
"""

    with open(TICKET_FILE, "a") as f:
        f.write(ticket)

    print("\n✅ Your ticket has been submitted. Your Ticket ID is:", ticket_id)

def view_tickets():
    try:
        with open(TICKET_FILE, "r") as f:
            data = f.read()
            print("\n🎫 All Submitted Tickets:\n")
            print(data if data else "No tickets found.")
    except FileNotFoundError:
        print("No tickets have been submitted yet.")

def main():
    while True:
        print("\n=== SUPPORT TICKET SYSTEM ===")
        print("1. Submit a Support Ticket")
        print("2. View All Tickets (Admin)")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            submit_ticket()
        elif choice == '2':
            view_tickets()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()


