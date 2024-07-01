import appointment as ap
import csv
appt_list = []
#asks the user to choose the day and time for their appointment

def create_weekly_calendar():
    day = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    for day_name in day:
        for time in range(9,17):
            appt_list.append(ap.Appointment(day_name,time))
    print(f'Weekly calendar created')
    #user can access the scheduled appointments
def load_scheduled_appointments():
    filename = input("Enter the filename: ")
    while True:
        try:
            with open(filename, 'r') as file:
                pass  
        except FileNotFoundError:
            filename = input("File not found. Re-enter the file name: ")
            continue
        else:
            scheduled_appointments = 0
            reader = open(filename,'r')
            for row in reader:
                client_name, client_phone, appt_type, day_of_week, start_time = row.strip().split(',')

                appt_type = int(appt_type)
                start_time = int(start_time)
                appt = find_appointment_by_time(day_of_week, start_time)

                if appt:
                    appt.schedule(client_name, client_phone, appt_type)
                    scheduled_appointments += 1

        print(f'{scheduled_appointments} previously saved appointments have been loaded')
        break
def print_menu():
    print(f"Jojo's Hair Salon Appointment Manager")
    print(f'-------------------------------------')
    print(f'-------------------------------------')
    print(f'1) Schedule an appointment')
    print(f'2) Find appointment by name')
    print(f'3) Print calendar for a specific day')
    print(f'4) Cancel an appointment')
    print(f'9) Exit the system')
    
def schedule_appointment():
    print("** Schedule an appointment **")
    day_name = input("What day: ")
    start_time = int(input("Enter start hour(24 hour clock): "))
    name = input("Client Name: ")
    phone = input("Client Phone: ")
    print("Appointment types\n1: Mens Cut $50, 2: Ladies Cut $80, 3: Mens Colouring $50, 4: Ladies Colouring $120")
    type = int(input("Type of Appointment: "))
    for appt in appt_list:
        if day_name == appt.get_day_of_week() and start_time == appt.get_start_time_hour():
            appt.schedule(name,phone,type)
    print(f"OK, {name}'s appointment is scheduled")
def find_appointment_by_time(day_of_week,start_time):
    for appt in appt_list:
        if day_of_week == appt.get_day_of_week() and start_time == appt.get_start_time_hour():
            return appt
def show_appointments_by_name():
    client_name = input("Enter Client Name: ")
    client_name = client_name.lower()
    for appt in appt_list:
        if client_name in (appt.get_name()).lower():
                print(appt.__str__())
        
        
def show_appointments_by_day():
    print("** Print calendar for a specific day **")
    day_of_week = input("Enter day of week: ")
    print(f'{"Client Name":<15} {"Phone":<12} {"Day": ^12} {"Start":^13}  {"End":<2} {"Type":^15}')
    for appt in appt_list:
        if day_of_week in appt.get_day_of_week():
            print(appt.__str__())
            if len(appt.__str__()) == 0:
                print("No appointments found")
def save_scheduled_appointments():
    print("** Exit the system **")
    while True:
        filename = input("Enter filename:")
        try:
            file = open(filename,'r')
            file.close()
        except FileNotFoundError:
            with open(filename,'w') as file:
                scheduled_appointments = 0
                for appt in appt_list:
                    if appt.get_appt_type() != 0:
                        file.write(f"{appt.format_record()}\n")
                        scheduled_appointments += 1
                print(f'{scheduled_appointments} appointments saved to the file {filename}')
                break
        else:
            proc = input("File already exists. Do you want to overwrite it?(Y/N): ")
            proc = proc.upper()
            if proc == "Y":
                scheduled_appointments = 0
                with open(filename,'w') as file:
                    for appt in appt_list:
                        if appt.get_appt_type() != 0:
                            file.write(f"{appt.format_record()}\n")
                            scheduled_appointments += 1
                print(f'{scheduled_appointments} appointments saved to the {filename} file')
                break
            elif proc == "N":
                continue
            else:
                print("Invalid Input. Please try again")
def cancel_appointment():
    day_name = input("What day: ")
    start_time = int(input("Enter start hour(24 hour clock): "))

    for appt in appt_list:
           
        if day_name in appt.get_day_of_week()  and start_time == appt.get_start_time_hour():
            if appt.get_appt_type() != 0:
                appt.cancel()
            else:
                print("Time slot isn't booked and doesn't need to be cancelled")
                

def main():           
    print("Starting the Appointment Manager System")
    create_weekly_calendar()
    load_app = input("Would you like to load previously scheduled appointments from a file (Y/N)?: ")
    load_app = load_app.upper()
    if load_app == "Y":
        load_scheduled_appointments()
    while True:
        print_menu() 
        choice = int(input("Enter your selection: "))
        while choice != 9:
            match choice:
                case 1:
                    schedule_appointment()
                    break
                case 2:
                    print("** Find appointment by name **")
                    show_appointments_by_name()
                    break
                case 3:
                    show_appointments_by_day()
                    break
                case 4: 
                    cancel_appointment()
                    break
                case _:
                    print("Invalid Choice. Please try again!")
                    break
        else:
            save_app = input("Would you like to save all scheduled appointments to a file (Y/N)? ")
            save_app = save_app.lower()
            if save_app == "y":
                save_scheduled_appointments()
                print("Good Bye!")
                break
if __name__ == "__main__":
    main()