def noPermissionMessage():
    return "You have no permission to see this."

def notSharedLevel():
    return "This level is private. You can only see the public levels and the ones created by " \
        + "other users only if they share them with you."


""" Strings used in the scoreboard. """


def noPermissionTitle():
    return "No permission "


def noPermissionScoreboard():
    return "Scoreboard is only visible to students and teachers. Log in if you think you " + \
        "should be able to see it. "

def noDataToShow():
    return "There is no data to show. Please contact your administrator if this is unexpected. "

""" String messages used on the settings page. """


def shareTitle():
    return "Level Share"


def shareSuccessfulPerson(name, surname):
    return "You shared your level with {0} {1} successfully! ".format(name, surname)


def shareSuccessfulClass(className):
    return "You shared your level with class {0} successfully! ".format(className)


def shareUnsuccessfulPerson(name, surname):
    return "We were unable to find {0} {1}. Are you sure you got their name right?".format(name, surname)


def shareUnsuccessfulClass(className):
    return "We were unable to find class {0}. Are you sure you got it right?".format(className)


def chooseAvatar():
    return "Choose your avatar "


def uploadAvatar():
    return "...Or upload your own "


def noLevelsToShow():
    return "It seems that you have not created any levels. How about creating one now? "


def levelsMessage():
    return "All the levels you have created so far. Click on them to play them or share them " \
        + "with your friends. "


def sharedLevelsMessage():
    return "All the levels created by others that were shared with you. Click on them to " \
        + "play them"


def noSharedLevels():
    return "No one shared a level with you yet. "


""" Strings used in the class view. """


def chooseClass():
    return "Choose a class you want to see. "


def noPermission():
    return "You don't have permissions to see this. "


""" String messages used as level tips in the game view. """


def description_level_default():
    return "Write something. "  # TODO: Come up with something.


def description_overall():
    return "<i>Help the van deliver the order to the customers in the house.</i><br><br>"


def title_level1():
    return "Can you help the van get to the house? "


def description_level1():
    message = "Choose the right blocks to tell the van where to go. <br> Drag the blocks under " \
        + " the 'Start' block to attach them. <br> Are you happy with your sequence? Then click " \
        + "'go'! "  # TODO: not direct control?
    return "<b>" + title_level1() + "</b><br><br>" + message


def title_level2():
    return "This time the house is further away. "


def description_level2():
    message = "Can you help the van get there? <br> Like last time, drag the right blocks and " \
        + "attach them under the 'Start' block. <br> To remove a block, drag it back to the " \
        + "left of the screen. "  # TODO: or the bin.
    return "<b>" + title_level2() + "</b><br><br>" + message


def title_level3():
    return "Can you make the van turn right? "


def description_level3():
    message = "This time, the van has to turn right to reach the house. Make sure you use the " \
        + "'turn right' block in your sequence. <br> Drag the blocks and attach them under the " \
        + "'Start' block like before. To remove a block, drag it back to the left of the screen. "
    return "<b>" + title_level3() + "</b><br><br>" + message


def title_level4():
    return "You are getting good at this! Let's try turning left. "


def description_level4():
    message = "This time the van has to go left as well as right. Make sure you use the 'Turn " \
        + "left' block in your sequence. <br> Drag and attach the blocks like before."
    return "<b>" + title_level4() + "</b><br><br>" + message


def title_level5():
    return "Good work! You are ready for something harder. "


def description_level5():
    message = "You already know how to make the van turn left or right. This time the van has to " \
        + "make lots of turns to reach the house. <br> Drag and attach the blocks to make your " \
        + "sequence. "
    return "<b>" + title_level5() + "</b><br><br>" + message


#
#
# MISSING
#
#

def title_level6():
    return "The CFC is not always in the same place. "


def description_level6():
    message = "The driver does not always start the journey by going to the right of the screen. "
    return "<b>" + title_level6() + "</b><br><br>" + message


def title_level7():
    return "Can you go from right to left? "


def description_level7():
    message = "Practise your newly aquired skills on this road by helping the driver to arrive " \
        + "at the house. "
    return "<b>" + title_level7() + "</b><br><br>" + message


def title_level8():
    return "More complicated maze. "


def description_level8():
    message = "Congratulations, you should be now able to solve quite complex levels. Here's one " \
        + "you can have a go at. "
    return "<b>" + title_level8() + "</b><br><br>" + message


def title_level9():
    return "Snail maze! "


def description_level9():
    message = "Look at this snail maze! Can you navigate the driver through it? "
    return "<b>" + title_level9() + "</b><br><br>" + message


def title_level10():
    return "Very long and very bendy. "


def description_level10():
    message = "Wow! Look at that! It won't get more complicated than this, we promise!"
    return "<b>" + title_level5() + "</b><br><br>" + message

#
# End of Paulina's substitutes
#


def title_level11():
    return "Repeating yourself is boring."


def description_level11():
    message = "Attach a block inside the 'Repeat' block to make the van repeat it. <br> This " \
        + "means you can use one block instead of lots of blocks to do the same thing. <br> " \
        + "How many times do you want the block repeated? Type the number into the 'Repeat' " \
        + "block. "
    return "<b>" + title_level11() + "</b><br><br>" + message


def title_level12():
    return "Use the 'Repeat' block to make your sequence simpler. "


def description_level12():
    message = "You drove the van down this road on Level 7. This time, use the 'Repeat' block to " \
        + "get the van to the house. This will make your sequence simpler than last time."
    return "<b>" + title_level12() + "</b><br><br>" + message


def title_level13():
    return "No need for numbers. "


def description_level13():
    message = "Attach a block inside a 'Repeat until' block, and the van will keep repeating it. " \
        + "The van will not stop until it has reached the point you want it to stop. <br> " \
        + "You do not have to work out how many times the van should repeat your block. Instead, " \
        + "just tell the van to stop when it reaches the house. "
    return "<b>" + title_level13() + "</b><br><br>" + message


def title_level14():
    return "Can you do that again? "


def description_level14():
    message = "Well done, you did it! Now haave a go at using the 'Repeat until' block on a road " \
        + "with lots of turns. "
    return "<b>" + title_level14() + "</b><br><br>" + message


def title_level15():
    return "This time use 'Repeat While'. "


def description_level15():
    message = "Last time you told the van to repeat a block until it reached the house. This " \
        + "time, tell the van to repeat the block while not at the house. This means it will " \
        + "stop when it does reach the house. <br> This is called a While Loop. The block is " \
        + "repeated while it is true that the van is not at the house. "
    return "<b>" + title_level15() + "</b><br><br>" + message


def title_level16():
    return "Put the 'while loop' to the test. "


def description_level16():
    message = "The van is back at the bendy road. Can you use the 'Repeat while' block to make a " \
        + "While Loop? <br> Make the van repeat your While Loop while it is not at the house. " \
        + "This means you will have a short, simple sequence to make it reach the house. "
    return "<b>" + title_level16() + "</b><br><br>" + message


def title_level17():
    return "Now it's time to try the 'if' block. "


def description_level17():
    message = "Another way of telling the van what to do is to use the 'If' block . For example, " \
        + "you can tell the van to go forward if the road goes forward, or to turn left if the " \
        + "road goes forward, or to turn left if it goes left. <br> Try using the 'If block' and " \
        + "the 'Repeat' block together. <br> The 'Repeat' block will stretch if you attach the " \
        + "'If' block inside it. "
    return "<b>" + title_level17() + "</b><br><br>" + message


def title_level18():
    return "Good work! What else can you do? "


def description_level18():
    message = "You can also use the 'If' block to create choices. Add 'else' to the 'If' block " \
        + "so the van knows what to do if the first choice can't be done. <br> For example, " \
        + "tell the van to 'turn left if the road turns left. Add 'else turn right' and the van " \
        + "turns right if the road does not turn left. "
    return "<b>" + title_level18() + "</b><br><br>" + message


def title_level19():
    return "What if you cannot see the road? "


def description_level19():
    message = "If you cannot see the road, you cannot see the choices to make. No problem! " \
        + "This is where 'If' and 'else' are useful. <br> You can tell the van to go one way if " \
        + "the road goes that way. If the road does not go that way, the van will do nothing. " \
        + "<br> Keep adding choice using 'else if' and the van will move when the program finds " \
        + "the right choice. <br> You can add as many 'else if' choices as you like. Add 'else' " \
        + "as your last choice so that the van knows what to do when the choices run out."
    return "<b>" + title_level19() + "</b><br><br>" + message


def title_level20():
    return "Fantastic! Can you do it again? "


def description_level20():
    message = "Here is another road. It is even bendier than before, but you know lots of ways " \
        + "to get the van to the house. <br> Get the van to the house using what you have learnt. "
    return "<b>" + title_level20() + "</b><br><br>" + message


#
# Paulina's happy creations
#
#
def title_level21():
    return "Junction time!"


def description_level21():
    message = "Have you noticed something different? Now you can solve mazes with junctions. " \
        + "This means you have more than one way to reach the destination. Do you accept the" \
        + "challenge? "
    return "<b>" + title_level21() + "</b><br><br>" + message


def title_level22():
    return "Snail roundabout. "


def description_level22():
    message = "This maze does look like a snail a bit, doesn't it? Can you navigate the van " \
        + "to the destination having a knot on your way? Remember - the shorter the path, the " \
        + "better. "
    return "<b>" + title_level22() + "</b><br><br>" + message


def title_level23():
    return "Great! Another try? "


def description_level23():
    message = "You've done fantastic job so far! Can you find the way to the house this time? " \
        + "There is more than one solution! "
    return "<b>" + title_level23() + "</b><br><br>" + message


def title_level24():
    return "That's tangled up! "


def description_level24():
    message = "This sure is one complicated maze. Can you spot the shortest path? "
    return "<b>" + title_level24() + "</b><br><br>" + message


def title_level25():
    return "Find the pattern in this chaos."


def description_level25():
    message = "This maze surely can be solved with the general algorithm. But watch out - the " \
        + "order in which you check for the instructions will matter in this case! "
    return "<b>" + title_level25() + "</b><br><br>" + message


def title_level26():
    return "Congratulations! You've made it so far!"


def description_level26():
    message = "Let's now practise what you've learnt so far. Create a program which lets the " \
        + "driver reach the house in the shortest way. "
    return "<b>" + title_level26() + "</b><br><br>" + message


def title_level27():
    return "Traffic lights!"


def description_level27():
    message = "Don't ignore the law. Don't let the van driver drive through the red lights. "
    return "<b>" + title_level27() + "</b><br><br>" + message


def title_level28():
    return "Following procedure"


def description_level28():
    message = "Use procedures to find the destination."
    return "<b>" + title_level28() + "</b><br><br>" + message


def title_level29():
    return "Threading your way"


def description_level29():
    message = "Try using multiple threads to get both vans to their destination"
    return "<b>" + title_level29() + "</b><br><br>" + message


def title_level30():
    return "Title level 30"


def description_level30():
    message = ""
    return "<b>" + title_level30() + "</b><br><br>" + message


def title_level31():
    return "Title level 31"


def description_level31():
    message = ""
    return "<b>" + title_level31() + "</b><br><br>" + message


def title_level32():
    return "Title level 32"


def description_level32():
    message = ""
    return "<b>" + title_level32() + "</b><br><br>" + message


def title_level33():
    return "Title level 33"


def description_level33():
    message = ""
    return "<b>" + title_level33() + "</b><br><br>" + message

def title_level34():
    return "Title level 33"


def description_level34():
    message = ""
    return "<b>" + title_level33() + "</b><br><br>" + message

def title_level35():
    return "Title level 33"


def description_level35():
    message = ""
    return "<b>" + title_level33() + "</b><br><br>" + message

def title_level36():
    return "Title level 33"


def description_level36():
    message = ""
    return "<b>" + title_level33() + "</b><br><br>" + message

def title_level37():
    return "Title level 33"


def description_level37():
    message = ""
    return "<b>" + title_level33() + "</b><br><br>" + message

def title_level38():
    return "Title level 33"


def description_level38():
    message = ""
    return "<b>" + title_level33() + "</b><br><br>" + message

def title_level39():
    return "Title level 33"


def description_level39():
    message = ""
    return "<b>" + title_level33() + "</b><br><br>" + message


def title_level40():
    return "Title level 33"


def description_level40():
    message = ""
    return "<b>" + title_level33() + "</b><br><br>" + message

def title_level41():
    return "Title level 33"


def description_level41():
    message = ""
    return "<b>" + title_level33() + "</b><br><br>" + message

def title_level42():
    return "Title level 33"


def description_level42():
    message = ""
    return "<b>" + title_level33() + "</b><br><br>" + message

def title_level43():
    return "Title level 33"


def description_level43():
    message = ""
    return "<b>" + title_level33() + "</b><br><br>" + message

def title_level44():
    return "Title level 33"


def description_level44():
    message = ""
    return "<b>" + title_level33() + "</b><br><br>" + message

def title_level45():
    return "Title level 33"


def description_level45():
    message = ""
    return "<b>" + title_level33() + "</b><br><br>" + message

def title_level46():
    return "Title level 33"


def description_level46():
    message = ""
    return "<b>" + title_level33() + "</b><br><br>" + message

def title_level47():
    return "Title level 33"


def description_level47():
    message = ""
    return "<b>" + title_level33() + "</b><br><br>" + message

def title_level48():
    return "Title level 33"


def description_level48():
    message = ""
    return "<b>" + title_level33() + "</b><br><br>" + message

def title_level49():
    return "Title level 33"


def description_level49():
    message = ""
    return "<b>" + title_level33() + "</b><br><br>" + message

#
# The end of Paulina's Happy Creation.
#
#


def hint_level_default():
    message = "There is no specific information I can give for this level.<br>Do your best to " \
        + "remember some of the things you have learnt in the previous levels. "
    return message


def hint_level1():
    message = "Drag and drop the <b>move forwards</b> block so that it is under the <b>start</b> " \
        + "block - close enough to be touching. "
    return message


def hint_level2():
    message = "A block can be placed next to another if the jigsaw pieces fit. A second <b>move " \
        + "forwards</b> block can be placed under the first <b>move forwards</b> block. "
    return message


def hint_level3():
    message = "A block can be placed next to another if the jigsaw pieces fit. A <b>turn " \
        + "right</b> block can be placed under the first <b>move forwards</b> block. "
    return message


def hint_level4():
    message = "This road starts by curving to the <b>left</b>. Then it curves to the <b>right</b>. "
    return message


def hint_level5():
    message = "Follow the road round. Doing this with the arrows next to the <b>GO</b> button " \
        + "will produce the instructions for you! "
    return message


def hint_level6():
    message = "A <b>move forwards</b> block can be placed inside of the <b>repeat</b> block (to " \
        + "the right of the word 'do'). <br>Don't forget to change the number of times you need " \
        + "to repeat. "
    return message


def hint_level7():
    message = "This level can be broken down into 3 sets of: 'turn left, then turn right'. "
    return message


def hint_level8():
    message = "The blocks should read like a sentence: <b>Repeat</b> (the following) <b>until at " \
        + "destination</b>: <b>move forwards</b>. "
    return message


def hint_level9():
    message = "The blocks should read like a sentence: <b>Repeat</b> (the following) <b>until at " \
        + "destination</b>: <b>turn left</b>, (then) <b>turn right</b>. "
    return message


def hint_level10():
    message = "<b>while not</b> is the same as <b>until</b>. <br>The blocks should read like a " \
        + "sentence: <b>Repeat</b> (the following) <b>while not at destination</b>: <b>move " \
        + "forwards</b>. "
    return message


def hint_level11():
    message = "<b>while not</b> is the same as <b>until</b>. <br>The blocks should read like a " \
        + "sentence: <b>Repeat</b> (the following) <b>while not at destination</b>: <b>turn " \
        + "left</b>, (then) <b>turn right</b>. "
    return message


def hint_level12():
    message = "<b>if</b> a <b>road exists forwards</b> then <b>move forwards</b>. This "\
        + "instruction will need to be repeated to get to the destination. "
    return message


def hint_level13():
    message = "We need to check where the road is using an <b>if-else</b> block. <br>You can " \
        + "create an <b>if-else</b> block by clicking the star on the <b>if</b> block, and " \
        + "adding the <b>else</b> clause. <br>If the condition block is true, the blocks after " \
        + "<b>if</b> are executed, otherwise the blocks after <b>else</b> are. <br><b>if</b> a " \
        + "<b>road exists left</b>, <b>turn left</b>. <b>else</b> (otherwise) <b>turn right</b>. "
    return message


def hint_level14():
    message = "We need to check where the road is using an <b>if-else if</b> block. <br>You can " \
        + "create an <b>if-else if</b> block by clicking the star on the <b>if</b> block, and " \
        + "adding the <b>else if</b> clause. <br>If the first condition block is true, the " \
        + "blocks after <b>if</b> are executed, otherwise if the second condition block is true, " \
        + "the blocks after <b>else if</b> are executed. <br><b>if</b> a <b>road exists " \
        + "left</b>, <b>turn left</b>. <b>else if a road exists right</b>, <b>turn right</b>. " \
        + "<b>else move forwards</b>. "
    return message


def hint_level15():
    message = hint_level_default()
    return message


def hint_level16():
    message = "<b>If</b> the road <b>is a dead end</b>, you will need to <b>turn around</b>. "
    return message


def hint_level17():
    message = hint_level_default()
    return message


def hint_level18():
    message = hint_level_default()
    return message


def hint_level19():
    message = hint_level_default()
    return message


def hint_level20():
    message = hint_level_default()
    return message


def hint_level21():
    message = hint_level_default()
    return message


def hint_level22():
    message = hint_level_default()
    return message


def hint_level23():
    message = hint_level_default()
    return message


def hint_level24():
    message = hint_level_default()
    return message


def hint_level25():
    message = hint_level_default()
    return message


def hint_level26():
    message = hint_level_default()
    return message


def hint_level27():
    message = hint_level_default()
    return message


def hint_level28():
    message = hint_level_default()
    return message

def hint_level29():
    message = hint_level_default()
    return message

def hint_level30():
    message = hint_level_default()
    return message

def hint_level31():
    message = hint_level_default()
    return message

def hint_level32():
    message = hint_level_default()
    return message

def hint_level33():
    message = hint_level_default()
    return message

def hint_level34():
    message = hint_level_default()
    return message

def hint_level35():
    message = hint_level_default()
    return message

def hint_level36():
    message = hint_level_default()
    return message

def hint_level37():
    message = hint_level_default()
    return message

def hint_level38():
    message = hint_level_default()
    return message

def hint_level39():
    message = hint_level_default()
    return message

def hint_level40():
    message = hint_level_default()
    return message

def hint_level41():
    message = hint_level_default()
    return message

def hint_level42():
    message = hint_level_default()
    return message

def hint_level43():
    message = hint_level_default()
    return message

def hint_level44():
    message = hint_level_default()
    return message

def hint_level45():
    message = hint_level_default()
    return message

def hint_level46():
    message = hint_level_default()
    return message

def hint_level47():
    message = hint_level_default()
    return message

def hint_level48():
    message = hint_level_default()
    return message

def hint_level49():
    message = hint_level_default()
    return message

def hint_level50():
    message = hint_level_default()
    return message
