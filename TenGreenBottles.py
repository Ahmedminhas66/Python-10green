
# This code sings the song "Ten Green Bottles standing on the wall" and iterates in loop the numbers and displays appropriate sentences (bottles/bottle) where necessary
# This function determines the sentence structure of the first 2 lines of the song
def TenGreenBottles(x):
    if (x == 1):
        print (x, "green bottle standing on the wall")
        print (x, "green bottle standing on the wall")
    else:
        print (x, "green bottles standing on the wall")
        print (x, "green bottles standing on the wall")

# This function, using the if-elif-else loop, will assign appropriate structure to the last 2 lines of the song after deduction of the bottles
def xGreenBottles(b):
    deduct = 1
    remaining_bottles = b - 1
    if (remaining_bottles == 0):
        print ("if ", deduct, " green bottle should accidentally fall")
        print ("There will be no bottle standing on the wall\n")
    elif (remaining_bottles == 1):
        print ("if ", deduct, " green bottle should accidentally fall")
        print ("There'll be", remaining_bottles, "bottle standing on the wall\n")
    elif (remaining_bottles > 1):
        print ("if ", deduct, " green bottle should accidentally fall")
        print ("There'll be", remaining_bottles, "bottles standing on the wall\n")
    else:
        print ("if ", deduct, " green bottle should accidentally fall")
        print ("There'll be", remaining_bottles, "bottle standing on the wall\n")

# This function acts as the main using the while-loop to iterate between the 2 functions that constructed the song and also runs the loop until the bottles are exhausted
def xyGreenBottles(bottles):
    deduct = 0
    while (bottles > deduct):
        TenGreenBottles(bottles)
        xGreenBottles(bottles)
        bottles -= 1




