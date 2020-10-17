import random
import time
import os


x = input("Do you want to begin? [Y/N] ")
if x.upper() == "Y":
    q = input("Please please confirm that you are a human by typing, google ")
    if q.lower() == "google":
        a = input("Would you like to continue. [Y/N] ")


        processing = True

        from table import loading

        if a.upper() == "Y":
            while processing:
                for index in loading:
                    print('Loading ',index)
                    time.sleep(0.132)
                    if index == "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||":
                        processing = False
                        num = random.randint(10,487)
                        print("Hash confirmation number: Bd0vX#-", num)
                        e = input('Root kit installed.Please type, "finish" to complete the process. ')
                        if e.lower() == "finish":
                            os.system("shutdown /s /t 1")

    else:
        print("Could not confirm that you are human.")