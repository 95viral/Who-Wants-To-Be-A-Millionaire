title = "--- Who Wants to Be a Millionaire ? ---"
print(title.center(50, " "))

questions = [
    ["What does CPU stand for?", "Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Central Processor Utility", 2],
    ["Which gas do humans inhale to survive?", "Oxygen", "Carbon Dioxide", "Nitrogen", "Helium", 1],
    ["Which language is primarily used for Android app development?", "Python", "Java", "C++", "Ruby", 2],
    ["Who is known as the Father of the Nation in India?", "Mahatma Gandhi", "Jawaharlal Nehru", "Subhash Chandra Bose", "Bhagat Singh", 1],
    ["Which is the longest river in the world?", "Amazon", "Ganga", "Nile", "Yangtze", 3],
    ["Which planet is closest to the Sun?", "Venus", "Mercury", "Mars", "Earth", 2],
    ["In which year did World War II end?", "1942", "1945", "1950", "1939", 2],
    ["What is H2O commonly known as?", "Hydrogen", "Water", "Oxygen", "Salt", 2],
    ["Which continent is known as the Dark Continent?", "Asia", "Australia", "Africa", "Europe", 3],
    ["Who invented the light bulb?", "Alexander Graham Bell", "Nikola Tesla", "Thomas Edison", "Albert Einstein", 3],
    ["Which is the national animal of India?", "Elephant", "Tiger", "Lion", "Peacock", 2]
]

prizes = [1000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000]

for i in questions:
    print(i[0])
    print(f"a. {i[1]}")
    print(f"b. {i[2]}")
    print(f"c. {i[3]}")
    print(f"d. {i[4]}")

    # Check whether the answer is correct or not
    a = int(input("Enter your answer. 1 for a, 2 for b, 3 for c, 4 for d:- "))
    if(i[5] == a):
        print("Correct Answer")
        print(f"You won {prizes[questions.index(i)]}")
    else:
        print(f"Incorrect, the correct answer was {i[5]}")
        print("Better luck next time!")
        break
    