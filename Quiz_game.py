print("Welcome to my quiz!")
print()

playing = input("Do you want to play? ")  # wyświetla pytanie do użytkownika, czy chce zagrać w quiz

if playing.lower() != "yes":  # jeśli użytkownik nie wpisze "yes" to aplikacja się zamknie  # .lower sprawia, że odpowiedź użytkownika zmieni się na małe litery (inaczej program by się zamknął gdyby użyktownik wpisał np YEs)
    quit()

print("Okay, let's play! :)")
score = 0

answer = input("What does CPU stand for? ")  #  pytanie do użytkownika
if answer.lower() == "central processing unit":  # jeśli odpowiedź to "tekst z cudzysłowia" 
    print("Correct!")  # wyświetla się informacja, że to prawidłowa odpowiedź
    score += 1  # do wyniku doda się 1 punkt za prawidłową odpowiedź (to samo co score = score + 1)
else: 
    print("Incorrect!")


answer = input("What does GPU stand for? ")  
if answer.lower() == "graphics processing unit":  
    print("Correct!") 
    score += 1 
else: 
    print("Incorrect!")


answer = input("What does RAM stand for? ")  
if answer.lower() == "random access memory":  
    print("Correct!") 
    score += 1 
else: 
    print("Incorrect!")


answer = input("What does PSU stand for? ")  
if answer.lower() == "power supply":  
    print("Correct!")  
    score += 1
else: 
    print("Incorrect!")

print()

print("You got " + str(score) + " questions correct!")  # wyświetla ilość poprawnych pytań
print("You got " + str((score / 4) * 100) + "%")  # wyświetla wynik procentowy