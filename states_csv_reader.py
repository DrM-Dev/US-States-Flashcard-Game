#_______________Imports:
import pandas
from gevent.util import print_run_info
import random
#_______________Secondary Imports:
from tkinter import messagebox

#_______________Globals:
state_keys_list = [] #empty by default

#_______________DataBAse Globals:
#################
states_DF =   None # pandas.read_csv(r"data/French/fr_500.csv")
chosen_lang_DIC =  None # {row_info.Lang: row_info.English for (index, row_info) in chosen_lang_DF.iterrows()}
lang_series =      None # pandas.Series(chosen_lang_DIC)


states_DF = pandas.read_csv(r"states data/50States.txt", index_col=False)
print(states_DF)
#================================================ Lang Options
def process_db():
    global state_keys_list
    #--
    global states_DF
    global chosen_lang_DIC
    global lang_series
    ####
    # ========================Data-Base SETUP
    states_DF = pandas.read_csv(r"states data/50States.txt")
    print(states_DF)
    # ====================================================================================DB to DIC
    # Turning Database into Dictionary:
    chosen_lang_DIC = {row_info.Lang: row_info.English for (index, row_info) in states_DF.iterrows()}
    # ====================================================================================DIC to DS (Data Series) "to pick keys ONLY"
    # TARGETED DIC => chosen_lang_DIC
    lang_series = pandas.Series(chosen_lang_DIC)
    #
    state_keys_list.clear()
    state_keys_list = [keys[0] for keys in lang_series.items()]




#=======================================================================================================================
#===================================================================================== PICKING A RANDOM KEY [Word & it's meaning]
##############################
def pick_random_state(exception_list):
    global chosen_lang_DIC
    global state_keys_list
    #======#======
    resalt_tuple = ""
    random_key = random.choice(state_keys_list)
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
        pick_random_state(exception_list)

    #___________________________________
    #=====EMPTY TUPLE BUG FIX:
    if resalt_tuple != "" or resalt_tuple != None:
        return resalt_tuple
    else:
        pick_random_state(exception_list)
