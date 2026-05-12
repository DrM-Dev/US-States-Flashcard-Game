#Language Flashcards Game - ver       by      Dr.M-Dev
ver = "0.1.1"
#====================IMPORTS:
from tkinter import *
import customtkinter
from PIL import ImageTk, Image
from customtkinter import CTkImage, CTkLabel
#
from tkinter import messagebox
#
import states_csv_reader


#====================Global Constants:
BACKGROUND_COLOR = "#B1DDC6"
LANG_TITLE_FONT = "Ariel", 40, "italic"
WORD_FONT = "Courier", 50, "bold"

#====================Globals:
player_choice = None
player_SCORE = 0
score_effected = False #(false -> the score is NOT YET Effected),
                      # (true -> the score have already been effected, and shouldn't be altered any further)
#
# fetched_tuple = None
the_word = "word_null"
the_meaning = ""
#
lang_keys_list = []
guessed_keys_list = []

#====================SETUP
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
#-------------
root = customtkinter.CTk()
root.configure(fg_color=BACKGROUND_COLOR)
#
window_width = 1000
window_height = 600
#
root.minsize(window_width,window_height)
root.maxsize(window_width,window_height)
root.config(padx=20,pady=20)
#-------------
root.title(f"Language Flashcards Game {ver}")
#----bitmap
root.iconbitmap("images/LangaugeFlashGame_bitmap.ico")
#----logo:
logo = customtkinter.CTkImage(light_image=Image.open("images/LOGO_T_Black.png"),size=(90,80))
logo_label = customtkinter.CTkLabel(root ,text="", fg_color="transparent" ,image=logo, bg_color="transparent")
logo_label.place(x=0,y=200)
#--------------------------
#-------------Widgets displacement
widgets_x_place = 20
widgets_y_place = 20
#|
buttons_x_displacement = 50
buttons_y_displacement = 50

#====================LANGUAGES Globals:
#LANGAUGES
FRENCH_LANG = "French"
# FRENCH_LANG_ICON =
#x+x+x+x+x+x+x+x+x+x+x+x
chosen_lang = "French" #default
#x+x+x+x+x+x+x+x+x+x+x+x
lang_title = chosen_lang

#______________________________________________________________
print('''                                                                                                                                                  
                                                              ...::::.      ...::::::::    :.      .:.   
  5@@@@@@@@B!    &@@@@@@@&G:        ^G&@@@&P#@@@@B~          J@@@@@@@@@G.   #@@@@@@@@@@   .@@B    7@@?   
  G@@~::::J@@!   @@#     B@@.      :@@G::~&@@!::Y@@~         J@@~    ^@@B   #@@.           !@@J  .@@B    
  G@@     .@@Y   @@@    5&@#       ~@@!   B@&   :@@?         J@@:     &@#   #@@BBBBBBB      P@@: #@@.    
  7BP     .@@J   PBGGGGGB@@B       :BB^   B@&   :@@?         ~GP.     &@#   JGPYYYYYYY       &@# @@!     
  Y&&^....?@@7   #&P     J@@:  ##  ^&&~   B@&   ^@@?         ?@@7:  :7@@P   Y@& ......       ^@@@@P      
  P@@@@@@@@&?    &@B     ?@@:  ##  ~@@!   B@&   :@@?         ?@@@@@@@@#J    J&@@@@@@@@?       ?@@B  


                                                             !J!:                                                                
                                                              ^G@@&P7:                                                           
                                         .~7YGB#&&&&&&&#BG5?~:  .Y@@@@&G^                                                        
                                    :?P&@@@@@@@@@@@@@@@@@@@@@@@&G?J@@@@@&                                                        
                                .!G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P   ...                                                 
                              ~B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BG&&@@@@                                              
                            ?&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&                                             
                          7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#GYP#&J                                            
                        .B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!                                                
                       :&@@@@@@@@@@@@@@@@J7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P                                               
                      .@@@@@@@@@@@@@@@@#:  ^&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G                                              
                      #@@@@@@@@@@@@@@&7      P@@@@@@@@@@@@@B&@@@@@@@&@@#&@@@@@@@@@@J                                             
                     !@@@@@@@@@@@@@&?         ^#@@@@&&@@@@@@#PPGB##? B@5#@#@@@@@@@@@:                                            
                     B@@@@@@@@@@@G~             ^B@@@&GG#@@@@@@@#~   .&#J@Y&@@@@@@@@G                                            
                     @@@@@@@@@@~                  .?#@@@&BGPGBBJ      .#5G&J@@@@@@@@@.                                           
                   .@@@@@@@@@7      !PB##B4^        .^JG#&&P:  ^4B###P4?!~!?@@@@@@@@^                                           
                   .@@@@@@@@#      !4~.. .~4^                 ~4~....~4^    #@@@@@@@^   .~                                      
               ~BJ :@@@@@@@@BJYYYYYYJJJJYJJJJJJJ?!.     .!?JYYYJJYYYJJJYYYYY&@@@@@@@P7: .G#?.                                   
            .?BG^  &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?...5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?  .Y#5:                                 
          :5BJ.    @@@@@@@@@&PJJJJJJ????JJJJ5&@@@@@@@@@@@@@@@GYJJ??????JJJJJYB@@@@@@@@@Y     7BB~                               
        !GG~       .YGG@@@@B        ...       G@@@@@@@@@@@@@:     .::.        !@@@@&GP7        ^G#?                             
     .JB5:             &@@@Y      4P..P@G.    7@@@@@@@@@@@@&    ^:^B@@@P.      @@@@~             .J#5.                          
     J@J               &@@@5     G@@4Y&@@&    ?@@@@?::^#@@@&   ~@4^B@@@@#     .@@@@~              ^#&:                          
      .5#J.            &@@@5     ?@@@@@@@P    7@@@@.   ?@@@&   .@@@@@@@@Y     .@@@@~           .J#P:                            
        .?#P:          #@@@G      .JGBBY:     5@@@&    ^@@@@.    ?B&&#P^      :@@@@~         ^PBJ.                              
           ~BB!        7@@@@5.              :P@@@@J     #@@@&!.             .!&@@@&        7BG~                                 
             :5#J.      ?@@@@@@@@@@@@@@@@@@@@@@@@J      .#@@@@@@&&&&&&&@&&@@@@@@@B.     :5BY.                                   
               .J#!      .7G&&@@@@@@@@@@@@@@&&G7.         ^5#&@@@@@@@@@@@@@@@&BJ:       7!                                      


 ''')

print(f"**** WELCOME to Language Flashcards Game {ver}   -by-    Dr.M-Dev ****")
#====================#====================#====================#==================
#====================#====================#====================#==================
#====================#====================#====================#==================
#++++++++++++++++++++++++++++++++++++++++BUTTON-FUNCTIONS
LP_Window_Is_ON = False #Disabled by default! #that way you can "HOVER and ACTIVATE IT"
#+++++++++++++++++++#
#______________________SWITCHING FUN\\
def pick_this_language(language):
    global chosen_lang
    global lang_title
    #----
    if language == "French":
        chosen_lang = "French"
        lang_title = chosen_lang
    elif language == "German":
        chosen_lang = "German"
        lang_title = chosen_lang
    elif language == "Russian":
        chosen_lang = "Russian"
        lang_title = chosen_lang
    elif language == "Spanish":
        chosen_lang = "Spanish"
        lang_title = chosen_lang
    elif language == "Chinese":
        chosen_lang = "Chinese"
        lang_title = chosen_lang
    else:
        chosen_lang = "French"
        lang_title = chosen_lang
    #----
    states_csv_reader.lang_switch_db(chosen_lang)
    print(f"\n<!>--> Language Database Switched to {chosen_lang}")
#+++++++++++++++++++#

#__________________BUTTONS FUN\\ #French or German or Russian or Spanish or Chinese
def finalizing_language_selection(selected_lang):
    global player_SCORE
    # ----
    confirm = messagebox.askyesno(title="Language Switch Warning", message=f"Are you sure you want to switch the cards to {selected_lang}?\nyour score will be back to 0!")
    # ----
    print(confirm) #DEBUG
    # ---
    if confirm:
        if selected_lang == "French":
            pick_this_language("French")
            set_current_lang_flag("French")
            #
        elif selected_lang == "German":
            pick_this_language("German")
            set_current_lang_flag("German")
            #
        elif selected_lang == "Russian":
            pick_this_language("Russian")
            set_current_lang_flag("Russian")
            #
        elif selected_lang == "Spanish":
            pick_this_language("Spanish")
            set_current_lang_flag("Spanish")
            #
        elif selected_lang == "Chinese":
            pick_this_language("Chinese")
            set_current_lang_flag("Chinese")
        #
        player_SCORE = 0
        score_counter.configure(text=f"Score:{player_SCORE}")
    else:
        print("no language was chosen")

#-------
def select_french():
    finalizing_language_selection("French")
def select_german():
    finalizing_language_selection("German")
def select_russian():
    finalizing_language_selection("Russian")
def select_spanish():
    finalizing_language_selection("Spanish")
def select_chinese():
    finalizing_language_selection("Chinese")


#-------------------------------------------------FLAG IMAGE FILES:
###################Pick Language Window Options: #French or German or Russian or Spanish or Chinese
#Language Image files:
french_lang_flag_img = customtkinter.CTkImage(light_image=Image.open("images/Flags/fr_flag.png"),size=(100,50))
german_lang_flag_img = customtkinter.CTkImage(light_image=Image.open("images/Flags/de_flag.png"), size=(100, 50))
russian_lang_flag_img = customtkinter.CTkImage(light_image=Image.open("images/Flags/ru_flag.png"), size=(100, 50))
spanish_lang_flag_img = customtkinter.CTkImage(light_image=Image.open("images/Flags/es_sp_flag.png"), size=(100, 50))
chinese_lang_flag_img = customtkinter.CTkImage(light_image=Image.open("images/Flags/zh_ch_flag.png"), size=(100, 50))

#__________________MAIN FUN\\
def pick_language():
    ##################FLAGS IMAGES:
    global french_lang_flag_img
    global german_lang_flag_img
    global russian_lang_flag_img
    global spanish_lang_flag_img
    global chinese_lang_flag_img
    ##################STARTUP
    global chosen_lang
    #---
    global LP_Window_Is_ON
    LP_Window_Is_ON = True #-->#IMPORTANT SWITCH (to disable click-able & hover images)\\
    # {-} #
    print("DEBUG: pick-language window activated")
    print(f"LANG PICK WINDOW STATE->>{LP_Window_Is_ON}")
    switchL_mark_button.configure(image=switchL_b__disabled_image)
    switchL_mark_button.configure(state="disabled")

    ##################SETUP:
    # ================
    # ================
    pick_lang_window = customtkinter.CTkToplevel(root)
    pick_lang_window.iconbitmap("images/LangaugeFlashGame_bitmap.ico")
    pick_lang_window.attributes("-topmost", True)
    #
    pick_lang_window.configure(fg_color=BACKGROUND_COLOR)
    #
    pick_lang_window.minsize(500, 400)
    pick_lang_window.maxsize(500, 400)
    pick_lang_window.config(padx=20, pady=20)
    # -------------
    pick_lang_window.title(f"Select A Language :)")
    # ----
    # #NOW switching this window to TOP LEVEL so it can respond to commands
    # print("<!> WINDOW-2 is top level now <!>")
    # customtkinter.CTkToplevel(master=pick_lang_window)
    # ================
    # ================

    ###################
    french_lang_flag_b = customtkinter.CTkButton(pick_lang_window, image=french_lang_flag_img, text="", height=50,
                                               width=100,
                                               command=select_french, fg_color="transparent",
                                               bg_color="transparent", border_width=0, hover_color="white")
# ----
    german_lang_flag_b = customtkinter.CTkButton(pick_lang_window, image=german_lang_flag_img, text="", height=50,
                                               width=100,
                                               command=select_german, fg_color="transparent",
                                               bg_color="transparent", border_width=0, hover_color="white")
#----
    russian_lang_flag_b = customtkinter.CTkButton(pick_lang_window, image=russian_lang_flag_img, text="", height=50,
                                               width=100,
                                               command=select_russian, fg_color="transparent",
                                               bg_color="transparent", border_width=0, hover_color="white")
#----
    spanish_lang_flag_b = customtkinter.CTkButton(pick_lang_window, image=spanish_lang_flag_img, text="", height=50,
                                               width=100,
                                               command=select_spanish, fg_color="transparent",
                                               bg_color="transparent", border_width=0, hover_color="white")
#----
    chinese_lang_flag_b = customtkinter.CTkButton(pick_lang_window, image=chinese_lang_flag_img, text="", height=50,
                                               width=100,
                                               command=select_chinese, fg_color="transparent",
                                               bg_color="transparent", border_width=0, hover_color="white")
#------------------------------------
    flags_x_place = 50
    flags_y_place = -60
    flags_displacement = 60
    #--
    french_lang_flag_b.place(x=flags_x_place,y=flags_y_place+flags_displacement*1)
    german_lang_flag_b.place(x=flags_x_place,y=flags_y_place+flags_displacement*2)
    russian_lang_flag_b.place(x=flags_x_place,y=flags_y_place+flags_displacement*3)
    spanish_lang_flag_b.place(x=flags_x_place,y=flags_y_place+flags_displacement*4)
    chinese_lang_flag_b.place(x=flags_x_place,y=flags_y_place+flags_displacement*5)

#------------------------------------ [More Labels:] ------------------------------------
    # Language Labels
    language_label_fonts = ("Courier", 40, "bold")
    # French or German or Russian or Spanish or Chinese
    french_lang_label = customtkinter.CTkLabel(pick_lang_window ,text="French",text_color="black" ,font=language_label_fonts,fg_color="transparent", bg_color="transparent")
    french_lang_label.place(x=flags_x_place + 150,y=flags_y_place+flags_displacement * 1 + 8)
    #
    german_lang_label = customtkinter.CTkLabel(pick_lang_window, text="German", text_color="black",font=language_label_fonts, fg_color="transparent", bg_color="transparent")
    german_lang_label.place(x=flags_x_place + 150, y=flags_y_place + flags_displacement * 2 + 8)
    #
    russian_lang_label = customtkinter.CTkLabel(pick_lang_window, text="Russian", text_color="black",font=language_label_fonts, fg_color="transparent", bg_color="transparent")
    russian_lang_label.place(x=flags_x_place + 150, y=flags_y_place + flags_displacement * 3 + 8)
    #
    spanish_lang_label = customtkinter.CTkLabel(pick_lang_window, text="Spanish", text_color="black",font=language_label_fonts, fg_color="transparent", bg_color="transparent")
    spanish_lang_label.place(x=flags_x_place + 150, y=flags_y_place + flags_displacement * 4 + 8)
    #
    chinese_lang_label = customtkinter.CTkLabel(pick_lang_window, text="Chinese", text_color="black",font=language_label_fonts, fg_color="transparent", bg_color="transparent")
    chinese_lang_label.place(x=flags_x_place + 150, y=flags_y_place + flags_displacement * 5 + 8)

#__________________________________________________
    # Current Lang Indicator:
    win2_current_language_indicator = customtkinter.CTkLabel(pick_lang_window, text=f"You Selected:",
                                                             text_color="black",
                                                             font=("Courier", 25, "bold"),
                                                             fg_color="transparent", width=50,
                                                             height=50)
    win2_current_language_indicator.place(x=flags_x_place, y=flags_y_place + flags_displacement * 5 + 60)
    #
    ################## LANGUAGE-INDICATOR:
    def change_lang_indicator(selected_lang):
        win2_current_language_indicator.configure(text=f"You Selected: {selected_lang}")

    ################## #----HOVER-Indicator
    def fr_b_hover_in(event):
        change_lang_indicator("French-🇫🇷")
    def de_b_hover_in(event):
        change_lang_indicator("German-🇩🇪")
    def ru_b_hover_in(event):
        change_lang_indicator("Russian-🇷🇺")
    def es_b_hover_in(event):
        change_lang_indicator("Spanish-🇪🇸")
    def zh_ch_b_hover_in(event):
        change_lang_indicator("Chinese-🇨🇳")
    # bind events:
    french_lang_flag_b.bind("<Enter>", fr_b_hover_in)
    german_lang_flag_b.bind("<Enter>", de_b_hover_in)
    russian_lang_flag_b.bind("<Enter>", ru_b_hover_in)
    spanish_lang_flag_b.bind("<Enter>", es_b_hover_in)
    chinese_lang_flag_b.bind("<Enter>", zh_ch_b_hover_in)


#__________________________________________________
    ################## LANGUAGE-WINDOW-OPTIONS END:
    def on_closing():
        #----
        global chosen_lang
        #----
        global LP_Window_Is_ON
        LP_Window_Is_ON = False #-->#IMPORTANT SWITCH (to enable click-able & hover images)\\
        # {-} #
        print("DEBUG: pick-language window IS OFF")
        print(f"LANG PICK WINDOW STATE->>{LP_Window_Is_ON}")
        switchL_mark_button.configure(image=switchL_b__normal_state_image)
        switchL_mark_button.configure(state="normal")
        #
        #
        # print("<!> switching back to the main window! <!>") #--->NO NEED, only .destroy() :)
        # customtkinter.CTkToplevel(master=root)
        #
        #
        picking_word() #<--- pick a new card right away to switch to the new language!
        set_current_lang_flag(chosen_lang)
        #
        pick_lang_window.destroy()  # Explicitly close the window

    pick_lang_window.protocol("WM_DELETE_WINDOW", on_closing)
    ################END_mainloop:
    pick_lang_window.mainloop()





#====================================================================================================Flash Cards System
#################################################################CHECKING PLAYER GUESS / WORD-CARD SWITCH MECHANIC
def check_player_answer():
    global player_choice
    global player_SCORE
    #
    global score_effected
    # -------------------
    # global fetched_tuple
    global the_word
    global the_meaning
    # ++++
    global guessed_keys_list
    # -------------------
    # -------------------
    answer_state = False
    #~~~~~~~~~~~~~~~~~~~~~~~~
    #~~~~~~~~~~~~~~~~~~~~~~~~fixing playing mechanic (also no need for score system, yet I will keep it) <!>
    if player_choice: #and fetched_tuple[1] == the_meaning:
        answer_state = True
    # if not player_choice and the_word != the_meaning:
    #     answer_state = True
    #-----
    # if player_choice and the_word != the_meaning:
    #     answer_state = False
    if not player_choice: #and fetched_tuple[1] == the_meaning:
        answer_state = False
    # ~~~~~~~~~~~~~~~~~~~~~~~~
    # ~~~~~~~~~~~~~~~~~~~~~~~~
    if answer_state:
        guessed_keys_list.append(the_word)
        #-----------
        if not score_effected:
            player_SCORE += 1
            score_counter.configure(text=f"Score:{player_SCORE}")
            ##
            score_effected = True
        #
        # switch_card_back() -> IF YOU KNOW THE MEANING...THEN TIME TO PULL ANOTHER CARD:
        picking_word()
        #>activate the (pick another card) -> picking_word() ---> it will do the switch_card_front() AUTOMATICALLY
        # ------------------------------
        print("DEBUG ->>>>> CORRECT ANSWER :D")
        print(f"SCORE-> {player_SCORE}")
        print(f"\nGUESSED LIST:\n{guessed_keys_list}")
        # ------

        ####
    elif not answer_state:
        if not score_effected:
            if player_SCORE != 0:
                player_SCORE -= 1
            #---
            score_counter.configure(text=f"Score:{player_SCORE}")
            ##
            score_effected = True
        #
        switch_card_back()
        #----------------
        # picking_word() #FLIP A NEW CARD!
        # ------------------------------
        print("DEBUG ->>>>> WRONG ANSWER :(")
        print(f"SCORE-> {player_SCORE}")
        print(f"\nGUESSED LIST:\n{guessed_keys_list}")
        # ------


#_________________________________________________________PICKING RANDOM WORD:
list_obtained = False
def match_lang_keys_lists():
    global lang_keys_list
    #global guessed_keys_list
    #=================
    #=================
    lang_keys_list = states_csv_reader.lang_keys_list
    # DEBUG:
    # print(f"list fetched ->{lang_keys_list}")
    # print(f"{guessed_keys_list}")

#++++++++++++++++++++++++++++++
def picking_word():
    # global fetched_tuple
    global the_word
    global the_meaning
    #++++
    global guessed_keys_list
    #=================
    #=================NEW:
    if not list_obtained:
        match_lang_keys_lists()
    #----------------
    global score_effected
    score_effected = False
    #=================
    #=================
    random_word_tuple = states_csv_reader.pick_random_word(guessed_keys_list)
    #
    # fetched_tuple = random_word_tuple
    try:
        the_word = random_word_tuple[0]
        the_meaning = random_word_tuple[1]
        print(f"\nTHE TUPLE +++++++++++++++++[+]+++++++++++++++++++. {random_word_tuple}")
    except IndexError:
        print(f"\nTHE TUPLE ---------------[X]---------------------. {random_word_tuple}")
        picking_word()
    #=================
    #=================
    switch_card_front()
    # DEBUG:
    # print(f"THE WORD{the_word}\nAND IT'S MEANING IS {the_meaning}")

#--------------
#GET A CARD BUTTON - Terminal / Primordial-Button xD
# flip_front_button = customtkinter.CTkButton(root, text="GET A NEW CARD", height=50, width=50,command=picking_word, bg_color="white", text_color="White", font=("Courier", 15, "bold"))
# flip_front_button.place(x=300,y=500)
# [edit: I decided to make it into a new feature "a fully functional button with CTk]




#====================================================================================================UIs + More
card_facing = "front" #only 2 states, #front/#back
def check_state():
    global card_facing
    global lang_title
    ####
    global the_word
    global the_meaning
    ####
    if card_facing == "front":
        main_canvas.configure(bg="white")
        #
        main_canvas.itemconfig(lang_title_text, text=f"{lang_title}") #ASKING ABOUT THE WORD
        main_canvas.itemconfig(random_word_text, text=f"{the_word}")
        #
        card_widget.configure(image=card_FRONT_img)
        #==========================================
    elif card_facing == "back":
        main_canvas.configure(bg="#86C1B0")
        #
        main_canvas.itemconfig(lang_title_text, text="Meaning:") #SHOWING THE MEANING
        main_canvas.itemconfig(random_word_text, text=f"{the_meaning}")
        #
        card_widget.configure(image=card_BACK_img)
#------------------------------------------
def switch_card_front():
    global card_facing
    card_facing = "front"
    print("debug: switch front")
    #
    check_state()
#----
def switch_card_back():
    global card_facing
    card_facing = "back"
    print("debug: switch back")
    #
    check_state()


#_____________________________________________________________Labels + more
#0000-Card
# FRONT_card_body_img = CTkImage(light_image=Image.open("images/card_front.png"), size=(800,500))
card_FRONT_img = customtkinter.CTkImage(light_image=Image.open("images/card_front.png"),size=(700,400))
card_BACK_img = customtkinter.CTkImage(light_image=Image.open("images/card_back.png"),size=(700,400))

#_________________LABEL-TEXT (for player score)
score_counter = customtkinter.CTkLabel(root, text=f"Score:{player_SCORE}", font=("Courier", 30, "bold"), text_color="black")
score_counter.place(x=widgets_x_place+390,y=widgets_y_place-35)

#_________________LABEL-IMAGE
card_widget = customtkinter.CTkLabel(root, image=card_FRONT_img, text="")
card_widget.place(x=window_width/2-360, y=window_height/4-120)

#_________________Canvas
# highlightthickness=0 keeps it looking modern without a clunky border
main_canvas = Canvas(root, width=700, height=400, highlightthickness=0, bg="white")
main_canvas.place(x=window_width/2-260, y=window_height/4-90)
####
#Canva-Text:
# the_word = "word_null" (a global variable)
lang_title_text = main_canvas.create_text(700/2,100, text=f"{lang_title}", font=LANG_TITLE_FONT)
random_word_text = main_canvas.create_text(700/2,280, text=f"{the_word}", font=WORD_FONT)





#_____________________________________________________________BUTTONS
#_____________________________________________________________
#0000-PICK A NEW CARD Button
####-------------------------Button Text Labels
correct_b__label = customtkinter.CTkLabel(root, text=f"Get Another Card", font=("Courier", 14, "bold"), text_color="Black")
correct_b__label.place(x=150+210+buttons_x_displacement,y=400+buttons_y_displacement+100)

####-------------------------BUTTON-ART / IMAGES
new_card_b__normal_state_image = customtkinter.CTkImage(light_image=Image.open("images/cards_norm.png"),size=(150, 100))
new_card_b__hover_in_image = customtkinter.CTkImage(light_image=Image.open("images/cards_hover.png"),size=(150, 100))
new_card_b__clicked_image = customtkinter.CTkImage(light_image=Image.open("images/cards_clicked.png"),size=(150, 100))

####-------------------------BUTTON-MAIN-FUNCTIONS
# def new_card_button_event():
#----------------------------->THE MAIN FUNCTION OF THIS BUTTON ISS GETTING A NEW CARD ->  picking_word()

####-------------------------BUTTON-CONSTRUCTION Widget
new_card_mark_button = customtkinter.CTkButton(root, image=new_card_b__normal_state_image , text="", height=50, width=150,command=picking_word, fg_color="transparent",border_width=0, hover=False)
new_card_mark_button.place(x=150+210+buttons_x_displacement,y=400+buttons_y_displacement)

####-------------------------BUTTON-Aesthetic-functions
#----HOVER
def new_card_b_hover_in(event):
    new_card_mark_button.configure(image=new_card_b__hover_in_image)
def new_card_b_hover_out(event):
    new_card_mark_button.configure(image=new_card_b__normal_state_image)
#bind events:
new_card_mark_button.bind("<Enter>", new_card_b_hover_in)
new_card_mark_button.bind("<Leave>", new_card_b_hover_out)

#----CLICK-STATE
def new_card_b_clicked(event):
    new_card_mark_button.configure(image=new_card_b__clicked_image)
def new_card_b_unclicked(event):
    new_card_mark_button.configure(image=new_card_b__normal_state_image)
#bind events:
new_card_mark_button.bind("<ButtonPress-1>", new_card_b_clicked)
new_card_mark_button.bind("<ButtonRelease-1>", new_card_b_unclicked)





#_____________________________________________________________
#0000-CHECK-MARK Button
####-------------------------Button Text Labels
correct_b__label = customtkinter.CTkLabel(root, text=f"I know this word", font=("Courier", 14, "bold"), text_color="Black")
correct_b__label.place(x=130+buttons_x_displacement,y=400+buttons_y_displacement+100)

####-------------------------BUTTON-ART / IMAGES
correct_b__normal_state_image = customtkinter.CTkImage(light_image=Image.open("images/right_norm.png"),size=(100, 100))
correct_b__hover_in_image = customtkinter.CTkImage(light_image=Image.open("images/right_hover.png"),size=(100, 100))
correct_b__clicked_image = customtkinter.CTkImage(light_image=Image.open("images/right_clicked.png"),size=(100, 100))

####-------------------------BUTTON-MAIN-FUNCTIONS
def check_button_event():
    global player_choice
    global guessed_keys_list
    #
    player_choice = True
    #-------------------
    #debug
    print("CORRECT pressed")
    #-------------------
    check_player_answer()

####-------------------------BUTTON-CONSTRUCTION Widget
check_mark_button = customtkinter.CTkButton(root, image=correct_b__normal_state_image , text="", height=50, width=50,command=check_button_event, fg_color="transparent",border_width=0, hover=False)
check_mark_button.place(x=150+buttons_x_displacement,y=400+buttons_y_displacement)

####-------------------------BUTTON-Aesthetic-functions
#----HOVER
def check_b_hover_in(event):
    check_mark_button.configure(image=correct_b__hover_in_image)
def check_b_hover_out(event):
    check_mark_button.configure(image=correct_b__normal_state_image)
#bind events:
check_mark_button.bind("<Enter>", check_b_hover_in)
check_mark_button.bind("<Leave>", check_b_hover_out)

#----CLICK-STATE
def check_b_clicked(event):
    check_mark_button.configure(image=correct_b__clicked_image)
def check_b_unclicked(event):
    check_mark_button.configure(image=correct_b__normal_state_image)
#bind events:
check_mark_button.bind("<ButtonPress-1>", check_b_clicked)
check_mark_button.bind("<ButtonRelease-1>", check_b_unclicked)





#_____________________________________________________________
#0000-WRONG-CLICK Button
####-------------------------Button Text Labels
wrong_b__label = customtkinter.CTkLabel(root, text=f"I don't know this word", font=("Courier", 14, "bold"), text_color="Black")
wrong_b__label.place(x=600-40+buttons_x_displacement,y=400+buttons_y_displacement+100)

####-------------------------BUTTON-ART / IMAGES
wrong_b__normal_state_image = customtkinter.CTkImage(light_image=Image.open("images/wrong_norm.png"),size=(100, 100))
wrong_b__hover_in_image = customtkinter.CTkImage(light_image=Image.open("images/wrong_hover.png"),size=(100, 100))
wrong_b__clicked_image = customtkinter.CTkImage(light_image=Image.open("images/wrong_clicked.png"),size=(100, 100))

####-------------------------BUTTON-MAIN-FUNCTIONS
def wrong_button_event():
    global player_choice
    player_choice = False
    # -------------------
    # debug
    print("WRONG pressed")
    # -------------------
    check_player_answer()

####-------------------------BUTTON-CONSTRUCTION Widget
wrong_button = customtkinter.CTkButton(root, image=wrong_b__normal_state_image , text="", height=50, width=50,command=wrong_button_event, fg_color="transparent",border_width=0, hover=False)
wrong_button.place(x=600+buttons_x_displacement,y=400+buttons_y_displacement)

####-------------------------BUTTON-Aesthetic-functions
#----HOVER
def wrong_b_hover_in(event):
    wrong_button.configure(image=wrong_b__hover_in_image)
def wrong_b_hover_out(event):
    wrong_button.configure(image=wrong_b__normal_state_image)
#bind events:
wrong_button.bind("<Enter>", wrong_b_hover_in)
wrong_button.bind("<Leave>", wrong_b_hover_out)

#----CLICK-STATE
def wrong_b_clicked(event):
    wrong_button.configure(image=wrong_b__clicked_image)
def wrong_b_unclicked(event):
    wrong_button.configure(image=wrong_b__normal_state_image)
#bind events:
wrong_button.bind("<ButtonPress-1>", wrong_b_clicked)
wrong_button.bind("<ButtonRelease-1>", wrong_b_unclicked)


#_____________________________________________________________SWITCHING LANGUAGE Button/Label/Current Language Indicator
#Current Lang Indicator:
current_language_indicator = customtkinter.CTkLabel(root ,text="", fg_color="transparent" ,image=french_lang_flag_img, bg_color="transparent", width=80, height=80)
current_language_indicator.place(x=150+665+buttons_x_displacement,y=200+buttons_y_displacement+40)

def set_current_lang_flag(current_lang):
    ##################FLAGS IMAGES:
    global french_lang_flag_img
    global german_lang_flag_img
    global russian_lang_flag_img
    global spanish_lang_flag_img
    global chinese_lang_flag_img
    #----
    language = current_lang
    #----
    if language == "French":
        current_language_indicator.configure(image=french_lang_flag_img)
    elif language == "German":
        current_language_indicator.configure(image=german_lang_flag_img)
    elif language == "Russian":
        current_language_indicator.configure(image=russian_lang_flag_img)
    elif language == "Spanish":
        current_language_indicator.configure(image=spanish_lang_flag_img)
    elif language == "Chinese":
        current_language_indicator.configure(image=chinese_lang_flag_img)
    else:
        current_language_indicator.configure(image=french_lang_flag_img)#back to default
    # ----



#0000-Switch-Lang Button
####-------------------------Button Text Labels
switchL_b__label = customtkinter.CTkLabel(root, text=f"Change Language\n\n\nCurrent Language:", font=("Courier", 12, "bold"), text_color="Black")
switchL_b__label.place(x=150+655+buttons_x_displacement,y=200+buttons_y_displacement-10)

####-------------------------BUTTON-ART / IMAGES
switchL_b__normal_state_image = customtkinter.CTkImage(light_image=Image.open("images/lang_folder_norm.png"),size=(100, 75))
switchL_b__hover_in_image = customtkinter.CTkImage(light_image=Image.open("images/lang_folder_hover.png"),size=(100, 75))
switchL_b__clicked_image = customtkinter.CTkImage(light_image=Image.open("images/lang_folder_hover.png"),size=(100, 75))
switchL_b__disabled_image = customtkinter.CTkImage(light_image=Image.open("images/lang_folder_disabled.png"),size=(100,75))

####-------------------------BUTTON-MAIN-FUNCTIONS
# def switchL_button_event():
#----------------------------->THE MAIN FUNCTION OF THIS BUTTON ISS GETTING A NEW CARD ->  pick_language()

####-------------------------BUTTON-CONSTRUCTION Widget
switchL_mark_button = customtkinter.CTkButton(root, image=switchL_b__normal_state_image , text="", height=50, width=150,command=pick_language, fg_color="transparent",border_width=0, hover=False)
switchL_mark_button.place(x=150+640+buttons_x_displacement,y=200+buttons_y_displacement-100)

####-------------------------BUTTON-Aesthetic-functions
#----HOVER
def switchL_b_hover_in(event):
    global LP_Window_Is_ON
    if not LP_Window_Is_ON:
        switchL_mark_button.configure(image=switchL_b__hover_in_image)
def switchL_b_hover_out(event):
    global LP_Window_Is_ON
    if not LP_Window_Is_ON:
        switchL_mark_button.configure(image=switchL_b__normal_state_image)
#bind events: ------------------------------------------------------------>AND BOUND TO "LP_Window_State" only allowed when it's FALSE "off"
switchL_mark_button.bind("<Enter>", switchL_b_hover_in)
switchL_mark_button.bind("<Leave>", switchL_b_hover_out)

#----CLICK-STATE
def switchL_b_clicked(event):
    global LP_Window_Is_ON
    if not LP_Window_Is_ON:
        switchL_mark_button.configure(image=switchL_b__clicked_image)
def switchL_b_unclicked(event):
    global LP_Window_Is_ON
    if not LP_Window_Is_ON:
        switchL_mark_button.configure(image=switchL_b__normal_state_image)
#bind events: ------------------------------------------------------------>AND BOUND TO "LP_Window_State" only allowed when it's FALSE "off"
switchL_mark_button.bind("<ButtonPress-1>", switchL_b_clicked)
switchL_mark_button.bind("<ButtonRelease-1>", switchL_b_unclicked)



#_____________________________________________________________Starting the code with:
picking_word()


#==============END
root.mainloop()
