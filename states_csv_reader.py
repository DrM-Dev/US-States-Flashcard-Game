#_______________Imports:
import pandas
from gevent.util import print_run_info
import random
#_______________Secondary Imports:
from tkinter import messagebox

#_______________Globals:
lang_keys_list = [] #empty by default

#_______________DataBAse Globals:
current_language = "French" #french by default *spawns a baguette*
#################
chosen_lang_DF =   None # pandas.read_csv(r"data/French/fr_500.csv")
chosen_lang_DIC =  None # {row_info.Lang: row_info.English for (index, row_info) in chosen_lang_DF.iterrows()}
lang_series =      None # pandas.Series(chosen_lang_DIC)


#================================================ Lang Options
def process_db():
    global lang_keys_list
    #--
    global chosen_lang_DF
    global chosen_lang_DIC
    global lang_series
    ####
    # ========================Data-Base SETUP
    # chosen_lang_DF => the Data frame have been picked in switched_db() function, and now it will run the processing phase:
    # ====================================================================================DB to DIC
    # Turning Database into Dictionary:
    chosen_lang_DIC = {row_info.Lang: row_info.English for (index, row_info) in chosen_lang_DF.iterrows()}
    # ====================================================================================DIC to DS (Data Series) "to pick keys ONLY"
    # TARGETED DIC => chosen_lang_DIC
    lang_series = pandas.Series(chosen_lang_DIC)
    #
    lang_keys_list.clear()
    lang_keys_list = [keys[0] for keys in lang_series.items()]


#_______________Lang Switch Operation:
def switch_db():
    global current_language #French or German or Russian or Spanish or Chinese
    global chosen_lang_DF
    ####
    try:
        if current_language == "French":
            # Switching Dataframe
            chosen_lang_DF = pandas.read_csv(r"data/French/fr_500.csv")
        elif current_language == "German":
            # Switching Dataframe
            chosen_lang_DF = pandas.read_csv(r"data/German/de_500.csv")
        elif current_language == "Russian":
            # Switching Dataframe
            chosen_lang_DF = pandas.read_csv(r"data/Russian/ru_500.csv")
        elif current_language == "Spanish":
            # Switching Dataframe
            chosen_lang_DF = pandas.read_csv(r"data/Spanish/sp_500.csv")
        elif current_language == "Chinese":
            # Switching Dataframe
            chosen_lang_DF = pandas.read_csv(r"data/Chinese/zh_cn_500.csv")
        else:
            # back to default
            # Switching Dataframe
            chosen_lang_DF = pandas.read_csv(r"data/French/fr_500.csv")
    except FileNotFoundError:
        messagebox.showerror(title="NO DATA", message="the langauge folder \"data\" for this program have been moved/deleted, please reinstall this program,\ncheck my githup page!! @Dr.M-Dev")
    ####
    process_db()

#_______________Main to Here -> Lang Switch:
def lang_switch_db(chosen_language):
    global current_language
    current_language = chosen_language
    #####
    switch_db()


#=======================================================================================================================
#===================================================================================== PICKING A RANDOM KEY [Word & it's meaning]
##############################
def pick_random_word(exception_list):
    global chosen_lang_DIC
    global lang_keys_list
    #======#======
    global current_language
    lang_switch_db(current_language) #default
    #======#======
    resalt_tuple = ""
    random_key = random.choice(lang_keys_list)
    #######
    if random_key not in exception_list:
        #
        picked_word = random_key
        picked_meaning = chosen_lang_DIC[picked_word]
        #
        print(f"this is the word= {picked_word}\nthis is the meaning= {picked_meaning}")
        # return something
        ############
        resalt_tuple = (picked_word,picked_meaning)
        ############
    else:
        pick_random_word(exception_list)

    #___________________________________
    #=====EMPTY TUPLE BUG FIX:
    if resalt_tuple != "" or resalt_tuple != None:
        return resalt_tuple
    else:
        pick_random_word(exception_list)
