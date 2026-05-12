#_______________Imports:
import pandas
from gevent.util import print_run_info
import random
#_______________Secondary Imports:
from tkinter import messagebox

from pymupdf.table import to_list

#_______________Globals:
state_keys_list = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

#=======================================================================================================================
#===================================================================================== PICKING A RANDOM KEY [Word & it's meaning]
##############################
def pick_random_state(exception_list):
    global chosen_lang_DIC
    global state_keys_list
    #======#======
    resalt_state = ""
    random_st = random.choice(state_keys_list)
    #######
    if random_st not in exception_list:
        #
        picked_state = random_st
        #
        print(f"<!>this is the word= {picked_state}\nthis is the meaning= {picked_state}")
        # return something
        ############
        resalt_state = picked_state
        ############
    else:
        pick_random_state(exception_list)

    #___________________________________
    #=====EMPTY TUPLE BUG FIX:
    if resalt_state != "" or resalt_state != None:
        return resalt_state
    else:
        pick_random_state(exception_list)


