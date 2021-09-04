import os
if os.path.getsize("profile.txt") == 0:
    file = (open("profile.txt", "a+", encoding="utf-8"))
    profile_name = input("Hello! How can I contact to you?\nPlease Put Your Name: ",)
    file.write(profile_name)
    print("Hello, ", profile_name, "! Nice To Meet You!")
    file.close()
else:
    file = (open("profile.txt", "r", encoding="utf-8"))
    print(file.read(), ", Hello! Nice To Meet You! ")
    file.close()

print("We have a few program for you: ")
print("\033[31mProgram #1 -   BRICKS   - Enter 1")
print("\033[32mProgram #2 - DICTIONARY - Enter 2")
print("\033[33mProgram #3 -  SEQUENCE  - Enter 3")
print("\033[34mProgram #4 - ChangeName - Enter 4")
print("\033[35mProgram #5 -    QUIT    - Enter q")

choice = input("\033[38mMake your choice: ")

# ========= PROGRAM 1
if ord(choice) == 49:
    import WALL
    print("\033[31mProgram 1 - Answer: ")
    res = WALL.breaks_solution(WALL.wall)
    if res != 0:
        print("Наименьшее количество пересечений кирпичей:", res)
    else:
        print("Пересечений кирпичей нет")

# ========= PROGRAM 2
elif ord(choice) == 50:
    print("\033[32mProgram 2 - Answer: ")
    import SEQUENCE
    for norm_view in SEQUENCE.get_uniq(SEQUENCE.data, SEQUENCE.keys):
        print(norm_view)
# ========= PROGRAM 3
elif ord(choice) == 51:
    print("\033[32mProgram 3 - Answer: ")
    import SORT
    print(SORT.data)
# ========= PROGRAM 4
elif ord(choice) == 52:
    file = (open("profile.txt", "w", encoding="utf-8"))
    profile_name = input("Put Your New Name: ")
    file.write(profile_name)
    print("Your name has been changed to\033[31m\033[1m", profile_name)
    file.close()
# ========= PROGRAM 5
elif ord(choice) == 113:
    print("Your Program Was Ended")
else:
    print("Please, Select Correct Program")
