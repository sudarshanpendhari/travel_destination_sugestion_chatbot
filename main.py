import json
import random

# Load destinations data
with open('destinations.json') as file:
    destinations = json.load(file)['dests']

# Initialize variables
current_step = "greet"
selected_category = None
shown_destinations = []

def greet():
    responses = [
        "Hello! Welcome to our travel suggestion chatbot.",
        "Hi there! Ready to plan your next trip?",
        "Hey! It's great to see you. Let's plan an amazing journey together."
    ]
    return random.choice(responses)

def ask_trip_planning():
    return "When are you planning your trip? Please provide the month (e.g., January, February)."

def ask_interests():
    return "What are your interests for this trip? Here are some options: Family trip, Business trip, Honeymoon trip, or something else."

def suggest_destinations(month):
    global selected_category
    global shown_destinations

    # Randomly choose a category of destinations
    if(month=="family trip"):
        selected_category ="hill station"
    elif(month=="honeymoon trip"):
        selected_category ="Beaches"
    elif(month=="business trip"):
        selected_category ="historical"
    else:
        selected_category ="Forts"
    destinations_in_category = destinations[selected_category]
    selected_destination = random.choice(destinations_in_category)
    shown_destinations.append(selected_destination['name'])
    if(selected_category!="Beaches"):
        return f"For your trip in {month}, I suggest {selected_destination['name']} in {selected_destination['Location']}. Would you like to explore more?"
    else:
        info_message = ""
        for spot in selected_destination['TouristSpots']:
            info_message += f"\n{spot['TSN']}: {spot['info']}"
    
        return f"For your trip in {month}, I suggest {selected_destination['name']} in {selected_destination['Location']}. Here are some tourist spots:{info_message}. Would you like to explore more?"
def suggest_more_destinations():
    global selected_category
    global shown_destinations

    if selected_category is None:
        return "Please select an interest first."
    
    # Show only one destination initially, if the user asks for more, show more
    other_destinations = [dest for dest in destinations[selected_category] if dest['name'] not in shown_destinations]
    if other_destinations:
        next_destination = random.choice(other_destinations)
        shown_destinations.append(next_destination['name'])
        return f"Another great option is {next_destination['name']} in {next_destination['Location']}."
    else:
        return "Sorry, I've run out of suggestions for now."

def main():
    print(greet())
    
    global current_step
    while True:
        user_input = input("You: ").strip().lower()

        if current_step == "greet":
            print(ask_trip_planning())
            current_step = "ask_trip_planning"
        
        elif current_step == "ask_trip_planning":
            print(ask_interests())
            current_step = "ask_interests"
        
        elif current_step == "ask_interests":
            print(suggest_destinations(user_input))
            current_step = "suggest_destinations"

        elif current_step == "suggest_destinations":
            if user_input in ['yes', 'sure', 'okay', 'why not', 'please']:
                print("Here are some more options:")
                print(suggest_more_destinations())
                print("Would you like to explore more options?\n type change to change your interests!!!")
            elif user_input in ['no', 'not now', 'stop']:
                print("Okay, let me know if you need further assistance.")
                break
            elif user_input in ['menu', 'change category', 'show menu']:
                print("Okay, let me know the category\nWhat are your interests for this trip? Here are some options: Family trip, Business trip, Honeymoon trip, or something else.")
                current_step = "ask_interests"
            else:
                print("Sorry, I didn't understand that. Would you like to explore more options?")
    
if __name__ == "__main__":
    main()
