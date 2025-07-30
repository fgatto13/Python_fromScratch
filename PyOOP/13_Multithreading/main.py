import threading
# to emulate the amount of time needed to perform an action,
# let's use the time module
import time

def walk_dog(name):
    time.sleep(8) # we'll wait 8 secs and then finish walking the dog
    print(f"you finish walking {name}")

def take_out_thrash():
    time.sleep(2) # it'll take 2 secs to take out the trash
    print('you take out the thrash')

def get_mail():
    time.sleep(3) # it'll take 3 secs to get the mail
    print('you get a mail')

def main():
    print("Starting activities")
    # when using threads, we need to create a threading object
    # and in the constructor, we need to provide a targeted function to perform
    chore1 = threading.Thread(target=walk_dog, args=("Barney",))
    # if a targeted function expects parameters, we pass a tuple (1, 2, ...) of args in the constructor of the thread.
    # then we need to start the thread
    chore1.start()

    chore2 = threading.Thread(target=take_out_thrash)
    chore2.start()

    chore3 = threading.Thread(target=get_mail)
    chore3.start()

    # these threads are running concurrently,
    # therefore, the display of completed tasks will be in order of finishing time

    # to wait for the completion of the chores, we use the join method
    chore1.join()
    chore2.join()
    chore3.join()

    print("All chores are complete!")

if __name__ == "__main__":
    main()