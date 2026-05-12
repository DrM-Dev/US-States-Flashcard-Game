#Language Flashcards Game - ver       by      Dr.M-Dev
from starlette.requests import empty_send

ver = "0.1.1"
#====================IMPORTS:
from tkinter import *
import customtkinter
from PIL import ImageTk, Image
from customtkinter import CTkImage, CTkLabel
#
from tkinter import messagebox
#
import random
#
state_keys_list = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]


#====================Global Constants:
BACKGROUND_COLOR = "#4f97fb"
# GUESS_TITLE_FONT = "Ariel", 15, "italic"
# STATE_NAME_FONT = "Courier", 50, "bold"

#====================Globals:
player_choice = None
player_SCORE = 0
score_effected = False #(false -> the score is NOT YET Effected),
                      # (true -> the score have already been effected, and shouldn't be altered any further)
#
# fetched_tuple = None
the_state = "word_null"
the_name = ""
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
root.iconbitmap("images/StatesFlashGame_bitmap.ico")
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

#====================Globals:
#x+x+x+x+x+x+x+x+x+x+x+x
chosen_state_title = ""

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


#====================================================================================================Flash Cards System
#################################################################CHECKING PLAYER GUESS / WORD-CARD SWITCH MECHANIC
def check_player_answer():
    global player_choice
    global player_SCORE
    #
    global score_effected
    # -------------------
    # global fetched_tuple
    global the_state
    global the_name
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
        guessed_keys_list.append(the_state)
        #-----------
        if not score_effected:
            player_SCORE += 1
            score_counter.configure(text=f"Score:{player_SCORE}")
            ##
            score_effected = True
        #
        # switch_card_back() -> IF YOU KNOW THE MEANING...THEN TIME TO PULL ANOTHER CARD:
        picking_state()
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


#_________________________________________________________PICKING RANDOM STATE:
#+++++++++++++++++++++++++++++
def picking_state():
    global the_state
    global the_name
    global chosen_state_title
    #++++
    global guessed_keys_list
    #=================
    global score_effected
    score_effected = False
    #=================
    try:
        random_state = random.choice(state_keys_list)
        if random_state not in guessed_keys_list:
            print(f"\nTHE STATE +++++++++++++++++[+]+++++++++++++++++++. {random_state}")
            the_state = random_state
            the_name = random_state
            chosen_state_title = "Guess The State"
        else:
            picking_state()
    except IndexError:
        print(f"ERROR IN {random_state}")
        picking_state()
    #=================
    #=================
    switch_card_front()





#====================================================================================================UIs + More
##################################################
# every state image file:

card_FRONT_img = customtkinter.CTkImage(light_image=Image.open("images/card_front.png"),size=(700,400))
#_________________LABEL-IMAGE
card_widget = customtkinter.CTkLabel(root, image=card_FRONT_img, text="")
card_widget.place(x=window_width/2-360, y=window_height/4-120)

##################################################
##################################################
##################################################
##################################################
card_facing = "front" #only 2 states, #front/#back
def check_state():
    global card_facing
    global chosen_state_title
    ####
    global the_state
    global the_name
    ####
    if card_facing == "front":
        main_canvas.configure(bg="white")
        #
        main_canvas.itemconfig(state_title_text, text=f"{chosen_state_title}") #ASKING ABOUT THE WORD
        main_canvas.itemconfig(state_name_for_images, text=f"{the_state}")
        #
        card_widget.configure(image=card_FRONT_img)
        #==========================================
    elif card_facing == "back":
        main_canvas.configure(bg="#3d71cf")
        #
        main_canvas.itemconfig(state_title_text, text="State Name:") #SHOWING THE MEANING
        main_canvas.itemconfig(state_name_for_images, text=f"{the_name}")
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
main_canvas = Canvas(root, width=700, height=20, highlightthickness=0, bg="white")
main_canvas.place(x=window_width/2-260, y=window_height/4-90)
####
#Canva-Text:
# the_word = "word_null" (a global variable)
state_title_text = main_canvas.create_text(700 / 2, 10, text=f"{chosen_state_title}", font=("Ariel", 15, "italic"))
state_name_for_images = main_canvas.create_text(700 / 2, 220, text=f"{the_state}", font=("Courier", 50, "bold"))





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
new_card_mark_button = customtkinter.CTkButton(root, image=new_card_b__normal_state_image , text="", height=50, width=150,command=picking_state, fg_color="transparent",border_width=0, hover=False)
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






#_____________________________________________________________Starting the code with:
picking_state()


#==============END
root.mainloop()
