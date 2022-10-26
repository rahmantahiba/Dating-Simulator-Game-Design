"""

Make sure to follow the game script on google doc.

"""

define c = Character("Creator", color="#FFD700")
define f = Character("female", image="female")
image define female normal = "side female normal.png"

label start:
    pause
    c "Hello players! Thank you for supporting my journey and I would like to emphasize that this is
    simply a personal project of mine. I hope everyone enjoys the game!"

    label gender:
    c "Anyway let's get started! What is the gender of your character?"

    menu:
        "Male":
            $ m_option = True
            jump male
        "Female":
            $ f_option = True
            jump female

    label male:

        if m_option == True:
            $ m_name = renpy.input("What is your name?")
            $ m_name = m_name.strip()

        elif m_name == "":
            $ m_name = "Zephyr"
            c "Your default name is Zephyr"

    label female:

        if f_option == True:
            $ f_name = renpy.input("What is your name?")
            $ f_name = f_name.strip() #to add space

        elif f_name == "":
            $ f_name = "Zephyrine"
            c "Your default name is Zephyrine"

    pause
return
