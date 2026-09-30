import json



def main_menu():
    print("1. Trainer")
    print("2. Runner")
    print("3. Exit")



def trainer_menu():
    print("1. View Your Profile")
    print("2. Create New Event")
    print("3. View Your Events")
    print("4. Cancel Event")
    print("5. Exit")    



def runner_menu():
    print("1. View Your Profile")
    print("2. View Events") 
    print("3. View Trainers")
    print("4. Join an Event")
    print("5. Cancel Participation")
    print("6. Exit")



    
def trainer_login():

    username_trainer = input("Please enter your username: ")    
    password_trainer = input("Please enter your password: ")

    for trainer in trainers:

        if trainer["username"] == username_trainer:

            if trainer["password"] == password_trainer:
                print("Login successful!")

                return trainer 

            else:
                print("Please check your password and try again.")
                return None

    print("Please check your username and try again.")         
    return None 



def runner_login():

    username_runner = input("Please enter your username: ")
    password_runner = input("Please enter your password: ")

    for runner in runners:

        if runner["username"] == username_runner:

            if runner["password"] == password_runner:
                print("Login successful!")

                return runner

            else:
                print("Please check your password and try again.")
                return None

    print("Please check your username and try again.")  
    return None       



with open("data.json", "r") as file:
    data = json.load(file)


trainers = data["trainers"]
events = data["events"]
runners = data["runners"]





print("Running Buddies")
print("Find Your Club. Find Your Buddies.")



while True:

    main_menu()
    main_start = input("Please enter your choice: ")


    if main_start == "1" or main_start.lower() == "trainer":

        logged_in_trainer = None

        while True:

            print("Welcome Trainer!")
            print("1. Register")
            print("2. Login")
            print("3. Back")

            trainer_start = input("Please enter your choice: ")

            if trainer_start == "1" or trainer_start.lower() == "register":
            
                trainer_info = {
            
                    "username" : input("Please choose a username: "),
                    "password" : input("Please create a password: "),
                    "first_name" : input("What is your first name: "),
                    "last_name" : input("What is your last name: "),
                    "languages" : input("Which languages do you speak: "),
                    "location" : input("What is your location: "),
                    "education" : input("What is your highest level of education: "),
                    "certifications" : input("What are your certifications: "),
                    "experience_years" : input("How many years of experience do you have: "),
                    "professional_experience" : input("What professional experience do you have: "),
                    "trainer_events" : []          
                }

                trainers.append(trainer_info)

                data["trainers"] = trainers

                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)

                    print("Registration successful!")


                logged_in_trainer = trainer_login()
                                    
                if logged_in_trainer:
                    
                    print("Welcome", logged_in_trainer["first_name"], "!")
                    break


            
            elif trainer_start == "2" or trainer_start.lower() == "login":
            
                logged_in_trainer = trainer_login()
                           
                if logged_in_trainer:
                    
                    print("Welcome", logged_in_trainer["first_name"], "!") 
                    break


            
            elif trainer_start == "3" or trainer_start.lower() == "back":

                break



            else: 
                print("Please enter a valid choice.")    




        if logged_in_trainer:
        
        
            while True:
        
                trainer_menu()
                trainer_choice = input("Please enter your choice: ")

        
                if trainer_choice == "1" or trainer_choice.lower() == "view your profile":
        
                    for key, value in logged_in_trainer.items():
                                 
                        if key != "trainer_events":
        
                            print(key.replace("_"," ").title(), ":", value)
                


                elif trainer_choice == "2" or trainer_choice.lower() == "create new event":
                                           
                    event= {
                        "event_name": input("What is your event name: "),
                        "location": input("Where is the event: "),
                        "date": input("When is the event: "),
                        "time": input("What time is the event: "),
                        "level": input("What is the running level: "),
                        "distance": input("What is the distance: "),
                        "max_participants": input("What is the maximum number of participants: "),  
                        "trainer_username": logged_in_trainer["username"],
                        "participants" : []
                    }   
                                        
                
                    logged_in_trainer["trainer_events"].append(event)
                    events.append(event)  

                    data["events"] = events

                    with open("data.json", "w") as file:
                        json.dump(data, file, indent=4)                     
                
                    print("Event created successfully!")



                elif trainer_choice == "3" or trainer_choice.lower() == "view your events": 
                                   
                    for event in logged_in_trainer["trainer_events"]:
                                       
                        for key,value in event.items():
           
                            if key != "participants":
                                           
                                print(key.replace("_"," ").title(), ":", value)



                elif trainer_choice == "4" or trainer_choice.lower() == "cancel event":   
                 
                    trainer_event_cancel = input("Do you want to cancel an event? (YES/NO): ")

                                    
                    if trainer_event_cancel.lower() == "no":
                        continue

                
                    elif trainer_event_cancel.lower() == "yes":
                
                        for number, event in enumerate(logged_in_trainer["trainer_events"], start=1):
                
                            print(number, event["event_name"].title())
                
                
                    trainer_event_cancel_choice = int(input("Which event would you like to cancel? Please enter the number: "))                


                    event = logged_in_trainer["trainer_events"].pop(trainer_event_cancel_choice - 1)
                    events.remove(event)


                    data["events"] = events

                    with open("data.json", "w") as file:
                        json.dump(data, file, indent=4)
                    
                    
                    print("Event cancelled successfully!")



                    
                elif trainer_choice == "5" or trainer_choice.lower() == "exit":
                     
                    print("Goodbye!", logged_in_trainer["first_name"].title(), "See you again!")    
                    exit()  



    elif main_start == "2" or main_start.lower() == "runner":

        logged_in_runner = None

        while True:

            print("Welcome, Runner!")
            print("1. Register")
            print("2. Login")
            print("3. Back")    

            runner_start = input("Please enter your choice: ")     

            if runner_start == "1" or runner_start.lower() == "register":   

                runner_info = {

                    "username": input("Please choose a username :"),
                    "password": input("Please create a password :"),
                    "first_name": input("What is your first name? :"),
                    "last_name": input("What is your last name :"),
                    "location": input("What is your location? :"),
                    "languages": input("Which languages do you speak? :"),
                    "running_level": input("What is your running level?  Beginner/Intermediate/Advanced :")
                }             
            
                runners.append(runner_info)


                data["runners"] = runners

                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
                
                print("Registration successful!")


                logged_in_runner = runner_login()

                if logged_in_runner:
                
                    print("Welcome", logged_in_runner["first_name"],"!")   
                    break   



            elif runner_start == "2" or runner_start.lower() == "login":
            
                logged_in_runner = runner_login()
            
                if logged_in_runner:
            
                    print("Welcome", logged_in_runner["first_name"],"!")
                    break
            
            
            
            elif runner_start == "3" or runner_start.lower() == "back": 
            
                break
            
            
            else:
                print("Please enter a valid choice.")         



        if logged_in_runner:

            while True:

                runner_menu()
                runner_choice = input("Please enter your choice: ")

                if runner_choice == "1" or runner_choice.lower() == "view your profile":

                    for key, value in logged_in_runner.items():

                        print(key.replace("_"," ").title(), ":", value)
  


                elif runner_choice == "2" or runner_choice.lower() == "view events":
        
                    for event in events:
        
                        for key, value in event.items():
        
                            print(key.replace("_"," ").title(), ":", value)
        
        
        
                elif runner_choice == "3" or runner_choice.lower() == "view trainers":
        
                    for trainer in trainers:
                
                        for key, value in trainer.items():
        
                            if key not in ("username","password","trainer_events"):
        
                                print(key.replace("_"," ").title(), ":", value)



                elif runner_choice == "4" or runner_choice.lower() == "join an event": 
                
                    for number, event in enumerate(events, start=1):
            
                        print(number,event["event_name"])
                
                
                    join_choice = input("Which event would you like to join? Please enter the number: ")   
                
                    if join_choice.isdigit():
                
                        event_number = int(join_choice)
                
                        if 1 <= event_number <= len(events):
                
                            selected_event = events[event_number - 1] 
                            selected_event["participants"].append(logged_in_runner["username"])


                            data["events"] = events

                            with open("data.json", "w") as file:
                                json.dump(data, file, indent=4)


                            print("You have successfully joined") 
                
                
                        else:
                            print("Invalid event number")
                
                
                    else:
                        print("Please enter a valid number.")



                
                elif runner_choice == "5" or runner_choice.lower() == "cancel participation":
                
                    runner_event_cancel = input("Do you want cancel your event participation? (YES/NO): ")
                
                
                    if runner_event_cancel.lower() == "yes":
                
                        for number, event in enumerate(events, start=1):
                
                            print(number,event["event_name"])
                
                
                
                    runner_event_cancel_choice = input("Which event do you want to cancel your participation in? Please enter the event number: ") 
                
                
                    if runner_event_cancel_choice.isdigit():
                
                        event_number = int(runner_event_cancel_choice)

                
                        if 1<= event_number <= len(events):
                
                            selected_event = events[event_number - 1]
                
                
                            if logged_in_runner["username"] in selected_event["participants"]:
                
                                selected_event["participants"].remove(logged_in_runner["username"])


                                data["events"] = events

                                with open("data.json", "w") as file:
                                    json.dump(data, file, indent=4)

                                print("You have canceled your participation.")
                
                
                            else:
                                print("You are not participating in this event.")
                
                
                        else:
                            print("Please enter a valid number.")
                

                
                    elif runner_event_cancel.lower() == "no":
                
                        continue    



                elif runner_choice == "6" or runner_choice.lower() == "exit":   
                    
                    exit() 
                    
                    
                    
                    
    elif main_start == "3" or main_start.lower() == "exit":
                    
        exit()
                    
                    
                    
    else:
        print("Invalid choice. Please try again.") 
                
                
                                
        
        