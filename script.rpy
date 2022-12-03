"""

Make sure to follow the game script on google doc.

"""

define c = Character("Creator", color="#FFD700")
define f = Character("[female]", image="female")
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

        if m_option:
            $ m_name = renpy.input("What is your name? Press enter to set a default name")
            $ m_name = m_name.strip()
            m_name "So you have selected my route. Thank you for following my journey"

        if m_name == "":
            $ m_name = renpy.input("What is your name? Press enter to set a default name", default = "Lucas")
            $ m_name = m_name.strip()
            $ m_name = "Lucas"
            m_name "So you have selected me. Thank you for following my journey player."

    label female:

        if f_option:
            $ f_name = renpy.input("What is your name? Press enter to set a default name")
            $ f_name = f_name.strip()
            f_name "So you have selcted my route. Thank you for following my journey"
            jump fscene1

        if f_name == "":
            $ f_name = renpy.input("What is your name? Press enter to set a default name", default = "Lisette")
            $ f_name = f_name.strip()
            $ f_name = "Lisette"
            f_name "So you have selected my route. Thank you for following my journey"
            jump fscene1

    label fscene1:

        c "Let the journey begin!"

        "Chapter 1: An Interesting Turn of Events"

    pause
return
