import os 


if __name__ == "__main__":
    print("This is a robo speaker which is make by Sukhdeep singh :")
    while True:
        typing = input("Type anything you want to say : ")
        if typing =="q":
            os.system("""spd-say 'untill we meet again, see you soon'""")
            break
        command = f"spd-say '{typing}'"
        os.system(command)