import nlpcloud

 
class NLPApp:
    def __init__(self):
        self.__database = {}
        self.__first_menu()
    
    def __first_menu(self):
        first_input = input("""Hi! How would you like to proceed?
1. Not a member? Register
2. Already a member? Login
3. Exit
""")
        if first_input == '1':
            self.__register()
        elif first_input == '2':
            self.__login()
        else:
            exit()

    def __second_menu(self):
        second_input = input("""Hi! How would you like to proceed?
1. NER
2. Language detection
3. Sentiment Analysis
4. Logout
""")
        if second_input == "1":
            self.__ner()
        elif second_input == "2":
            self.__language_detection()
        elif second_input == "3":
            self.__sentiment_analysis()
        else:
            exit()


            

    def __register(self):
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        password = input("Enter Password: ")

        if email in self.__database:
            print("Email already exists.\nPlease try another email.")
        else: 
            self.__database[email] = [name,password]
            print("Registration successfull.Now login")
            print(self.__database)
            self.__first_menu()

            
    def __login(self):
        email = input("Enter Email: ")
        password = input("Enter password: ")
        if email in self.__database:
            if self.__database[email][1] == password:
                print("Login successfull")
                self.__second_menu()
            else:
                print("Wrong Password. Try again!")
                self.__login()
        else:
            print("This email is not registered")
            self.__first_menu()

    def __ner(self):
        para = input("Enter the para: ")
        search_term = input("What you would like to search")
        client = nlpcloud.Client("finetuned-llama-3-70b", "0791956b6c6fdedc4a81739bef5c09834474488b", gpu=True)
        response = client.entities(para,searched_entity=search_term)
        print(response)
           
        


obj = NLPApp()    