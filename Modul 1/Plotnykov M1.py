# import os
# if os.path.getsize("profile.txt") == 0:
#     file = (open("profile.txt", "a+", encoding="utf-8"))
#     profile_name = input("Hello! How can I contact to you?\nPlease Put Your Name: ",)
#     file.write(profile_name)
#     print("Hello, ", profile_name, "! Nice To Meet You!")
#     file.close()
# else:
#     file = (open("profile.txt", "r", encoding="utf-8"))
#     print(file.read(), ", Hello! Nice To Meet You! ")
#     file.close()

from pathlib import Path
file = Path("profile.txt")
if file.exists():
    with open(file, "r") as profile:
        content = profile.readline()
else:
    user_input = input("Hello! How can I contact to you?\nPlease Put Your Name: ",)
    with open(file, "w") as profile:
        profile.write(user_input)

program = ["1", "2", "3", "4", "q", "Q"]
with open(file, "r") as profile:
    user_name = profile.readline()
    print(user_name, "Hello! We have a few program for you: ")
while True:
    print("\033[37m=================================")
    print("\033[31mProgram #1 -   BRICKS   - Enter 1")
    print("\033[32mProgram #2 - DICTIONARY - Enter 2")
    print("\033[33mProgram #3 -  SEQUENCE  - Enter 3")
    print("\033[34mProgram #4 - ChangeName - Enter 4")
    print("\033[35mProgram #5 -    QUIT    - Enter q")
    print("\033[37m=================================")
    x = input("\033[38mMake your choice: ")
    choice = x.lower()

    # ========= PROGRAM 1
    if choice not in program:
        print("--> Please enter correct number")

    if choice == "1":
        import WALL
        print("\033[31mProgram 1 - Answer: ")
        res = WALL.breaks_solution(WALL.wall)
        if res != 0:
            print("Наименьшее количество пересечений кирпичей:", res)
        else:
            print("Пересечений кирпичей нет")

    # ========= PROGRAM 2
    if choice == "2":
        print("\033[32mProgram 2 - Answer: ")
        import SEQUENCE
        for norm_view in SEQUENCE.get_uniq(SEQUENCE.data, SEQUENCE.keys):
            print(norm_view)

    # ========= PROGRAM 3
    if choice == "3":
        print("\033[32mProgram 3 - Answer: ")
        import SORT
        print(SORT.data)

    # ========= PROGRAM 4
    if choice == "4":
        file = (open("profile.txt", "w", encoding="utf-8"))
        profile_name = input("Put Your New Name: ")
        file.write(profile_name)
        print("Your name has been changed to\033[31m\033[1m", profile_name)
        file.close()

    # ========= PROGRAM 5
    if choice == "q":
        print("Your Program Was Ended")
        break
