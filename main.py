print("=== Server Maintenance Log===")
print("Maintenance Register")
print()
technician_name= input("Enter technician name: ")
print (f"Welcome, {technician_name}!")
print("This program records server maintenance activities.")

maintenance_records =[]
while True:
    print()
    print("==== MENU ====" )
    print("1 - Register maintenance")
    print("2 - View maintenance records")
    print("=" * 25)
    print("3 - Exit")
    
    option = input ("Choose an option: ")
    if option == "1":
            print("Register maintenance selected.")
            server_name = input("Enter server name (e.g., WEB-01):")
            problem = input("Describe the problem: ")
            solution = input("Describe the solution: ")
            maintenance_record = {
                "Server": server_name,
                "Problem": problem,
                "Solution": solution
            }
            maintenance_records.append(maintenance_record)
            print("Maintenance record added successfully.")
        
    elif option == "2":
        print("Maintenance Records")
        print("Total records:", len(maintenance_records))
        print("=" * 30)
        if not maintenance_records:
                print("No maintenance records found.")
        else:
            for index, record in enumerate(maintenance_records, start=1):
                print (f"Record {index}")
                print ("Server:", record["Server"])
                print ("Problem:", record["Problem"])
                print ("Solution:", record["Solution"])
                print("--------")
    elif option == "3":
        print("Goodbye!")
        break
    else:
         print("Invalid option.")
         print("Please choose 1, 2, or 3.")
  

  
