start = '''
You just found out that your sister has been kidnapped and is
being held in a castle guarded by dragons!
You must now become a superhero to save her!
'''
print(start)

super_power = input("Do you want super strength or super speed? Type 'strength' or 'speed'.")
time = 45

def print_time(time):
    print("You have " + str(time) + " minutes left.")
    return time


if super_power == "speed":
    print('''You trip into a particle accelerator and it explodes.
    When you emerge from the ashes, you now have super-speed!''')

    print("Suddenly, a timer appears, giving you only 45 minutes to save your sister.")


    superhero_friend = input('''Do you want to spend 15 minutes recruiting a
    superhero friend to help you, or try to go off on your own? Type 'friend' or 'own'.''')
    if superhero_friend == "friend":
        print("You lost 15 minutes finding a friend to help, but you now have a partner!")
        print_time(30)

        print('''You arrive at the castle and easily defeat the dragon with your friend.
        Unfortunately, as the two of you enter the castle, a troll appears and stats attacking your friend.''')
        print_time(20)
        friendship = input("Do you spend 15 minutes to save your friend, or leave him to die and continue on to your sister? Type 'friend' or 'sister'.")
        if friendship == "friend":
            print_time(5)
            print('''You saved your friend, but now you have to find your sister.
            With only 5 minutes left, you and your friend use your super speed to search the castle.
            Finally, you find her in the dungeons. You and your friend rescue her, and you all ride off into the sunset!''')
        elif friendship == "sister":
            print_time(20)
            print('''You leave your friend, and his screams echo down the hallway as you try to search for your sister.
            Unfortunately, the castle is too big, even with your super speed, and there's no way you can check all of the rooms.
            The troll comes running after you, and you get devoured. Your sister is left trapped in the castle for eternity.
            You should have saved your friend.''')





    elif superhero_friend == "own":
        print("You saved 15 minutes, but you will now have to save your sister on your own.")
        print_time(45)
        print('''You arrive at the castle, but now you have to outsmart the dragon.
        Unfortunately, it's too powerful for you to take on by yourself.
        Your super speed is no help to you when the dragon burns you to a crisp.
        Your sister is now trapped in the castle forever.''')






elif super_power == "strength":
    print('''You trip into a particle accelerator and it explodes.
    When you emerge from the ashes, you now have super-strength!''')

    print("Suddenly, a giant ogre appears!")

    battle = input("Do you want to run away or try to fight the ogre? Type 'run' or 'fight'.")
    if battle == "run":
        print("You try to run, but you aren't fast enough, and the ogre steps on you and kills you.")
        print("You failed your sister and the dragons have eaten her.")
    elif battle == "fight":
        print("You decide to fight the ogre with your super strength and defeat him!")
        print('''You continue the rescue for your sister.
        You arrive at the castle, but the dragon is guarding the entrance''')

        dragon = input("Do you want to fight the dragon or try to befriend it? Type 'fight' or 'befriend'.")
        if dragon == "fight":
            print('''You use your super strength and kill the dragon.
            As you step inside the castle, a troll appears.
            He sees the broken body of his only friend and flies into a wild rage, devouring you.
            In his blind anger, he also kills your sister.
            The last anyone sees of him, he is standing on the top of the castle, laughing manically.''')
        elif dragon == "befriend":
            print('''You try to befriend the dragon, and to your surprise, he accepts your friendship!
            He and his friend the troll decide to give up your sister, and the four of you ride off happily into the sunset.)
        
