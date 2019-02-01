#!/usr/bin/env python3

print("   .-^-.      llll         iiii    ttttttttttttt")
print("  /_/_\_\     llll         iiii    ttttttttttttt")
print(" ' ' | ' '    llll         iiii        tttt")
print("     J        llll         iiii        tttt")
print("              lllllllll    iiii        tttt")
print("              lllllllll    iiii        tttt")
print("")
print("LitWeather")
print("Author: LitMoose")
print("There is no copyright on this -- I'm not that fancy.")
print("Created on a cold January day, 2019")
print("")
print("")

def Fahrenheit(x):
    return ((x-32) * 5/9 + 273.15)

def Celsius(y):
    return (y + 273.15)

print("Select Country")
print("1.'Merica")
print("2.Belize")
print("3.Palau")
print("4.Bahamas")
print("5.Cayman Islands")
print("6.That one Canadian who uses Fahrenheit")
print("7.Texas")
print("8.Scotland")
print("9.Literally Everywhere Else")

#Now it's your turn

choice = input("Enter choice(1/2/3/4/5/6/7/8/9):")

degrees = eval(input("How many degrees do you THINK it is outside?: "))

if choice == '1':
    print("Actually it's", Fahrenheit(degrees) ,"Kelvins! That's grillin' weather! Pop open a cold one, grab your "
                                                "favorite red, white, and blue shorts, and meet me outside!")

elif choice == '2':
    print("Actually it's", Fahrenheit(degrees) ,"Kelvins! Great scuba weather. Say Scuba. Scuba. It's a great word.")

elif choice == '3':
    print("Actually it's", Fahrenheit(degrees) ,"Kelvins! Wait, are you REALLY in Palau, or are you just hitting "
                                                "buttons?")

elif choice == '4':
    print("Actually it's", Fahrenheit(degrees), "Kelvins! That's roughly the number of tourists who are going to barf"
                                                " after getting absolutely faced at Senor Frogs tonight.")

elif choice == '5':
    print("Actually it's", Fahrenheit(degrees) ,"Kelvins! Grab a bikini and do the stingray shuffle!")

elif choice == '6':
    print("Actually it's", Fahrenheit(degrees) ,"Kelvins! Sound lovely, eh. Good day to go ootside, enjoy a Molson,"
                                                " wave at a moose.")

elif choice == '7':
    print("YEEEEE HAW, THAT'S", Fahrenheit(degrees), "Kelvins! If'n yer not cookin' yer own, it's a great day for"
                                                     " brisket and some Shiners. See ya at DHA!")
elif choice == '8':
    print("Ach, is tha' all?! Quit yer greetin', tha's brammer weaither. Jist lest week when Ah was wearin' mah kilt, "
          "Ah go mah bawbag stuck tae a bench. Hud tae caa th' fire brigade.")

elif choice == '9':
    print("Actually it's", Celsius(degrees) ,"Kelvins! Congratulations on being part of a logical temperature"
                                             " measurement system. We'd all switch, but it's not worth the mass "
                                             "confusion. ;)")

else:
    print("Well, this is awkward. Did you use a space? Was there a typo? Are you messing with me? "
          "I'm not great at this yet. My peer reviewer was a cat.")
