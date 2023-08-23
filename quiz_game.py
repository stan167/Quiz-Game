import random

# Questions
sport = {
    "Which country won the 2018 FIFA World Cup?": "france",
    "Who holds the record for the most Olympic gold medals?": "michael phelps",
    "In which sport would you perform a slam dunk?": "basketball",
    "Which tennis player has won the most Grand Slam titles?": "serena williams",
    "What is the maximum score achievable in a single frame of snooker?": "147"
}
literature = {
    "Who wrote the play 'Romeo and Juliet'?": "william shakespeare",
    "What novel is set in the fictional Maycomb County and deals with racial injustice?": "to kill a mockingbird",
    "Which Russian novelist wrote 'War and Peace'?": "leo tolstoy",
    "Who is the author of '1984'?": "george orwell",
    "What epic poem tells the story of the hero Odysseus' journey home?": "the odyssey"
}
history = {
    "In which year did Christopher Columbus reach the Americas?": "1492",
    "Who was the first President of the United States?": "george washington",
    "What event marked the start of World War I?": "assassination of archduke franz ferdinand",
    "Which ancient civilization built the pyramids?": "ancient egyptians",
    "What was the name of the ship that carried the Pilgrims to America in 1620?": "mayflower"
}
science = {

    "What is the smallest unit of matter?": "atom",
    "Which planet is known as the 'Red Planet'?": "mars",
    "What process allows plants to convert light energy into chemical energy?": "photosynthesis",
    "What is the force that pulls objects towards the center of the Earth?": "gravity",
    "Which scientist formulated the theory of relativity?": "albert einstein"
}

def main_menu():
    topics = {"sport" : sport, "history": history, "literature": literature, "science": science}
    print("Welcome to my Quiz Game!\n")
    while True:
        print("Please select a topic:\nSport ⚽\nHistory 🕰️\nLiterature 📖\nScience 🔬\n")
        topic = input("Choice: ")
        if topic not in topics:
            print("\n")
            print("Please enter a valid topic!")
            print("\n")
        else:
            generate_question(topics[topic])
            break
            

def generate_question(topic):
    question = (random.choice(list(topic.keys())))
    answer = topic[question]
    print("\n")
    print(f"{question}\n")
    user_answer = input("Answer: ").lower().strip()
    print("\n")
    if user_answer == answer:
        print("Correct Answer!")
        question = []
    else:
        print("Wrong!")
        question = []





main_menu()