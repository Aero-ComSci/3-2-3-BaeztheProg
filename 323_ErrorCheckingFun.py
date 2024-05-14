# Function for input validation
def get_valid_input(prompt, options):
    while True:
        user_input = input(prompt).lower()
        if user_input in options:
            return user_input
        else:
            print("Invalid input. Please enter one of the provided options.")

sandwich_type = get_valid_input("What type of sandwich would you like? (chicken, beef, tofu): ", ["chicken", "beef", "tofu"])
get_valid_input("what size of drink",["small","medium","large"])
