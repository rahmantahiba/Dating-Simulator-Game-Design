"""

Make sure to follow the game script on google doc.

"""

define c = Character("Creator", color="#FFD700")
define f = Character("[female]", image="female", color="#FF69B4")
define m = Character("[male]", image="male", color="#30D5C8")
image define female normal = "female happy.png"

define f_option = None
define f_name = None
define m_option = None
define m_name = None

label start:

    c "Hello players! Thank you for supporting my project. I hope you enjoy the game!"

    label gender:

        c "Let's get started! What is your gender?"

        menu:
            "Male":
                $ m_option = True
                jump male
            "Female":
                $ f_option = True
                jump female

    label male:

        if m_option is not None:
            $ m_name = renpy.input("What is your name? Type Lucas if you wish to use the default name.")
            $ m_name = m_name.strip()
            jump chapter1

    label female:

        if f_option is not None:
            $ f_name = renpy.input("What is your name? Type Lisette if you wish to use the default name.")
            $ f_name = f_name.strip()
            jump chapter1

    label chapter1:

        if f_name:
            f_name "Thank you for following my journey, [f_name]"
        else:
            m_name "Thank you for following my journey, [m_name]"


        c "Let the journey begin!"


        "Chapter 1: An Interesting Turn of Events"

    pause
return
