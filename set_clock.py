################################################################################
# set_clock.py
# K. Szimonisz - Sept 2018
# Code built upon Professor A. Hornof's 'sample_menu.py' via CIS 443
#
# A sample program to show how to move through a list of sound objects with
# single keystrokes.
#
################################################################################
__author__ = 'szimonisz'

# Package imports
import readchar
import time         # for time.sleep()

# Local imports
import sound        # sound.py accompanies this file

################################################################################
# main()
################################################################################
def main():
    create_sound_filenames()
    
    # The sound file verification function is disabled by default, since it lags the start of the program due to the many sound files it plays.
    # Uncomment the following line if you wish to test the soundfiles used in this program. The intro audio will play regardless of your choice.
    #verify_sound_filenames()
    
    create_menu_globals()
    run_menu()

################################################################################
# Create the sound objects for the auditory menus and display.
################################################################################
def create_sound_filenames():

    # Declare global variables.
    global MENU_CHOICES_WAV, DAYS_WAV, HOURS_WAV, MINUTES_WAV, AM_AND_PM_WAV, INTRO_WAV, YOU_SELECTED_WAV, PRESS_AGAIN_TO_QUIT_WAV,\
        EXITING_PROGRAM_WAV, EXITING_PROGRAM_WAV_DURATION, TMP_FILE_WAV, HELP_WAV, ENTERING_DAY_MENU_WAV, ENTERING_HOUR_MENU_WAV, \
        ENTERING_MINUTES_MENU_WAV, ENTERING_AM_PM_MENU_WAV, CURRENT_SELECTION_IS_WAV, DAY_SET_TO_WAV, HOUR_SET_TO_WAV, MINUTES_SET_TO_WAV,\
        AM_PM_SET_TO_WAV, RETURNING_TO_START_MENU_WAV, PRESS_L_FOR_HELP_WAV, YOU_ARE_IN_THE_MENU_WAV, IT_IS_WAV, PRESS_SEMICOLON_TO_RETURN_TO_START_MENU_WAV,\
        PRESS_SEMICOLON_TO_QUIT_WAV

    # Create  sounds.
    nav_path = "custom_wav_files/misc/"
    menu_choices_path = "custom_wav_files/sub_menu_titles/"
    day_path = "custom_wav_files/days/"
    hour_path = "custom_wav_files/hours/"
    minute_path = "custom_wav_files/minutes/"
    am_pm_path = "custom_wav_files/am_pm/"
    
    INTRO_WAV = nav_path + "Intro.wav"
    HELP_WAV = nav_path + "Help.wav"
    PRESS_L_FOR_HELP_WAV = nav_path + "Press_L_key_for_assistance.wav"
    PRESS_SEMICOLON_TO_QUIT_WAV = nav_path + "Press_semicolon_to_quit.wav"
    
    MENU_CHOICES_WAV = [menu_choices_path + "Set_the_day_of_week.wav", menu_choices_path + "Set_the_hour.wav",\
        menu_choices_path + "Set_the_minutes.wav", menu_choices_path + "Set_am_pm.wav"]
    DAYS_WAV = [day_path + "Sunday.wav", day_path + "Monday.wav", day_path + "Tuesday.wav", day_path + "Wednesday.wav",\
        day_path + "Thursday.wav", day_path + "Friday.wav", day_path + "Saturday.wav"]
   
    HOURS_WAV = [hour_path + "1.wav", hour_path + "2.wav", hour_path + "3.wav", hour_path + "4.wav", hour_path + "5.wav",\
        hour_path + "6.wav", hour_path + "7.wav", hour_path + "8.wav", hour_path + "9.wav", hour_path + "10.wav",\
        hour_path + "11.wav", hour_path + "12.wav"]
    MINUTES_WAV = [minute_path + "01.wav", minute_path + "02.wav", minute_path + "03.wav", minute_path + "04.wav", minute_path + "05.wav",\
        minute_path + "06.wav", minute_path + "07.wav", minute_path + "08.wav", minute_path + "09.wav", minute_path + "10.wav", minute_path + "11.wav",\
        minute_path + "12.wav", minute_path + "13.wav", minute_path + "14.wav", minute_path + "15.wav", minute_path + "16.wav", minute_path + "17.wav",\
        minute_path + "18.wav", minute_path + "19.wav", minute_path + "20.wav", minute_path + "21.wav", minute_path + "22.wav", minute_path + "23.wav",\
        minute_path + "24.wav", minute_path + "25.wav", minute_path + "26.wav", minute_path + "27.wav", minute_path + "28.wav", minute_path + "29.wav",\
        minute_path + "30.wav", minute_path + "31.wav", minute_path + "32.wav", minute_path + "33.wav", minute_path + "34.wav", minute_path + "35.wav",\
        minute_path + "36.wav", minute_path + "37.wav", minute_path + "38.wav", minute_path + "39.wav", minute_path + "40.wav", minute_path + "41.wav",\
        minute_path + "42.wav", minute_path + "43.wav", minute_path + "44.wav", minute_path + "45.wav", minute_path + "46.wav", minute_path + "47.wav",\
        minute_path + "48.wav", minute_path + "49.wav", minute_path + "50.wav", minute_path + "51.wav", minute_path + "52.wav", minute_path + "53.wav",\
        minute_path + "54.wav", minute_path + "55.wav", minute_path + "56.wav", minute_path + "57.wav", minute_path + "58.wav", minute_path + "59.wav", minute_path + "00.wav"]
    AM_AND_PM_WAV = [am_pm_path + "AM.wav", am_pm_path + "PM.wav"]

    YOU_ARE_IN_THE_MENU_WAV = [nav_path + "You_are_in_the_set_day_menu.wav", nav_path + "You_are_in_the_set_hour_menu.wav",\
        nav_path + "You_are_in_the_set_minutes_menu.wav", nav_path + "You_are_in_the_set_am_pm_menu.wav"]
    YOU_SELECTED_WAV = nav_path + "You_selected.wav"
    
    ENTERING_DAY_MENU_WAV = nav_path + "Entering_the_set_day_menu.wav"
    ENTERING_HOUR_MENU_WAV = nav_path + "Entering_the_set_hour_menu.wav"
    ENTERING_MINUTES_MENU_WAV = nav_path + "Entering_the_set_minutes_menu.wav"
    ENTERING_AM_PM_MENU_WAV = nav_path + "Entering_the_set_am_pm_menu.wav"
    
    IT_IS_WAV = nav_path + "It_is.wav"
    DAY_SET_TO_WAV = nav_path + "Day_set_to.wav"
    HOUR_SET_TO_WAV = nav_path + "Hour_set_to.wav"
    MINUTES_SET_TO_WAV = nav_path + "Minutes_set_to.wav"
    AM_PM_SET_TO_WAV = nav_path + "AM_PM_set_to.wav"

    PRESS_SEMICOLON_TO_RETURN_TO_START_MENU_WAV = nav_path + "Press_semicolon_to_return_to_starting_menu.wav"
    RETURNING_TO_START_MENU_WAV = nav_path + "Returning_to_start_menu.wav"
    CURRENT_SELECTION_IS_WAV = nav_path + "Current_selection_is.wav"
    PRESS_AGAIN_TO_QUIT_WAV = nav_path + "Press_again_to_quit.wav"
    EXITING_PROGRAM_WAV = nav_path + "Exiting_program.wav"
    EXITING_PROGRAM_WAV_DURATION = 1.15 # in s. 1.09 is accurate but 0.45 saves time.

    TMP_FILE_WAV = "tmp_file_p782s8u.wav" # Random filename  for output

################################################################################
# Create some global constants and variables for the menu.
################################################################################
def create_menu_globals():

    # Declare global variables as such.
    global HELP_KEY, SET_KEY ,FORWARD_KEY, BACKWARD_KEY, QUIT_KEY, MINIMAL_HELP_STRING, CURRENT_DAY, CURRENT_HOUR,\
        CURRENT_MINUTES, CURRENT_AM_PM, CURRENT_MENU_CHOICE, CURRENT_SUBMENU_CHOICE

    # Constants
    # Keystrokes for the keyboard interaction.
    BACKWARD_KEY = 'j'
    FORWARD_KEY = 'k'
    HELP_KEY = 'l'
    QUIT_KEY = ';'
    SET_KEY = '\x20' #space bar
    
    # A bare minimum of text to display to guide the user.
    MINIMAL_HELP_STRING = "Welcome to set_clock."

    # Global variables
    CURRENT_DAY = 0
    CURRENT_HOUR = 0
    CURRENT_MINUTES = 0
    CURRENT_AM_PM = 0
    CURRENT_MENU_CHOICE = 0
    CURRENT_SUBMENU_CHOICE = 0

################################################################################
# Run the menu in an endless loop until the user exits.
################################################################################
def run_menu():

    global CURRENT_DAY
    global CURRENT_HOUR
    global CURRENT_MINUTES
    global CURRENT_AM_PM
    global CURRENT_MENU_CHOICE

    # Play the introduction audio
    sound.Play(INTRO_WAV)
    
    # Provide a minimal indication that the program has started.
    print(MINIMAL_HELP_STRING)

    # Get the first keystroke.
    c = readchar.readchar()

    # Endless loop responding to the user's last keystroke.
    # The loop breaks when the user hits the QUIT_MENU_KEY.
    while True:

        # Respond to the user's input.
        if c == FORWARD_KEY:

            # Advance the time, looping back around to the start.
            CURRENT_MENU_CHOICE += 1

            if CURRENT_MENU_CHOICE == len(MENU_CHOICES_WAV):
                CURRENT_MENU_CHOICE = 0

            sound.Play(MENU_CHOICES_WAV[CURRENT_MENU_CHOICE])

        if c == BACKWARD_KEY:

            # Retreat the time, looping back around to the end.
            CURRENT_MENU_CHOICE -= 1

            if CURRENT_MENU_CHOICE < 0:
                CURRENT_MENU_CHOICE = len(MENU_CHOICES_WAV) - 1;

            sound.Play(MENU_CHOICES_WAV[CURRENT_MENU_CHOICE])

        if c == SET_KEY:

            #Run the sub-menu function. run_submenu() will determine what specific submenu to run based on the value of CURRENT_MENU_CHOICE
            run_submenu()
        
        if c == HELP_KEY:
            
            # Create and play the help audio. Starting with the current day and time. 
            sound.combine_wav_files(TMP_FILE_WAV, IT_IS_WAV, DAYS_WAV[CURRENT_DAY],HOURS_WAV[CURRENT_HOUR],MINUTES_WAV[CURRENT_MINUTES],AM_AND_PM_WAV[CURRENT_AM_PM],HELP_WAV)
            sound.Play(TMP_FILE_WAV)
        
        # User quits.
        if c == QUIT_KEY:

            # Notify the user that another QUIT_MENU_KEY will quit the program.
            sound.Play(PRESS_AGAIN_TO_QUIT_WAV)

            # Get the user's next keystroke.
            c = readchar.readchar()

            # If the user pressed QUIT_MENU_KEY, quit the program.
            if c == QUIT_KEY:
                sound.Play(EXITING_PROGRAM_WAV)
                # A delay is needed so the sound gets played before quitting.
                time.sleep(EXITING_PROGRAM_WAV_DURATION)
                sound.cleanup()
                # Quit the program
                return
        # The user presses a key that will have no effect.
        else:
            # Get the user's next keystroke.
            c = readchar.readchar()

#################################################################################################################
# Run a sub-menu in an endless loop until the user exits.
# A sub-menu is selected from the starting menu by the user. 
# Sub-menus: "SET DAY MENU", "SET HOUR MENU", "SET MINUTES MENU", "SET AM/PM MENU"
# The global variable CURRENT_MENU_CHOICE represents the sub-menu selected from the starting menu. (run_menu())
# The global variable CURRENT_SUBMENU_CHOICE represents the specific sub-menu option selected from the sub-menu.
#################################################################################################################
def run_submenu():
    global CURRENT_SUBMENU_CHOICE
    global CURRENT_MENU_CHOICE
    global CURRENT_DAY
    global CURRENT_HOUR
    global CURRENT_MINUTES
    global CURRENT_AM_PM
    
    # The following three variables allow the run_submenu() function to operate in a modular fashion. 
    current_submenu_wav_collection = None
    current_entering_menu_wav = None
    current_set_to_wav = None

    # If the user selected the 'Set Day' sub-menu from the run_menu() function
    # Then set up the 'modular' sub-menu variables for 'Set Day' operation.
    if CURRENT_MENU_CHOICE == 0:
        CURRENT_SUBMENU_CHOICE = CURRENT_DAY
        current_submenu_wav_collection = DAYS_WAV
        current_entering_menu_wav = ENTERING_DAY_MENU_WAV
        current_set_to_wav = DAY_SET_TO_WAV
    
    # If the user selected the 'Set Hour' sub-menu from the run_menu() function
    # Then setup the 'modular' sub-menu variables for 'Set Hour' operation.
    elif CURRENT_MENU_CHOICE == 1:
        CURRENT_SUBMENU_CHOICE = CURRENT_HOUR
        current_submenu_wav_collection = HOURS_WAV
        current_entering_menu_wav = ENTERING_HOUR_MENU_WAV
        current_set_to_wav = HOUR_SET_TO_WAV
    
    # If the user selected the 'Set Minutes' sub-menu from the run_menu() function
    # Then setup the 'modular' sub-menu variables for 'Set Minutes' operation.
    elif CURRENT_MENU_CHOICE == 2:
        CURRENT_SUBMENU_CHOICE = CURRENT_MINUTES
        current_submenu_wav_collection = MINUTES_WAV
        current_entering_menu_wav = ENTERING_MINUTES_MENU_WAV
        current_set_to_wav = MINUTES_SET_TO_WAV

    # If the user selected the 'Set AM/PM' sub-menu from the run_menu() function
    # Then setup the 'modular' sub-menu variables for 'Set Minutes' operation.
    elif CURRENT_MENU_CHOICE == 3:
        CURRENT_SUBMENU_CHOICE = CURRENT_AM_PM
        current_submenu_wav_collection = AM_AND_PM_WAV
        current_entering_menu_wav = ENTERING_AM_PM_MENU_WAV
        current_set_to_wav = AM_PM_SET_TO_WAV

    # Create and play the Sub-menu transition introduction audio
    # "Entering <Selected Sub-menu>. Current selection is <Current Day OR Hour OR Minutes OR AM/PM>. Press the L key for assistance. Press semicolon to return to start." 
    sound.combine_wav_files(TMP_FILE_WAV, current_entering_menu_wav, CURRENT_SELECTION_IS_WAV,\
        current_submenu_wav_collection[CURRENT_SUBMENU_CHOICE], PRESS_L_FOR_HELP_WAV, PRESS_SEMICOLON_TO_RETURN_TO_START_MENU_WAV)
    sound.Play(TMP_FILE_WAV)
    
    # Get the first keystroke.
    c = readchar.readchar()
    
    while True:
        # Respond to the user's input.
        if c == FORWARD_KEY:

            # Advance the available sub-menu options, looping back around to the start.
            CURRENT_SUBMENU_CHOICE += 1
            
            if CURRENT_SUBMENU_CHOICE == len(current_submenu_wav_collection):
                CURRENT_SUBMENU_CHOICE = 0
            
            # Play the sub-menu option the user is currently pointing at. (i.e. "Sunday")
            sound.Play(current_submenu_wav_collection[CURRENT_SUBMENU_CHOICE])

        if c == BACKWARD_KEY:

            # Retreat the available sub-menu options, looping back around to the end.
            CURRENT_SUBMENU_CHOICE -= 1
            
            if CURRENT_SUBMENU_CHOICE < 0:
                CURRENT_SUBMENU_CHOICE = len(current_submenu_wav_collection)-1

            # Play the sub-menu option the user is currently pointing at. (i.e. "Sunday")
            sound.Play(current_submenu_wav_collection[CURRENT_SUBMENU_CHOICE])

        if c == SET_KEY:
            # MENU CHOICE KEY: 0 -> Set Day, 1 -> Set Hour, 2 -> Set Minutes, 3 -> Set AM/PM
           
            # If current sub-menu is: "Set Day" sub-menu
            if CURRENT_MENU_CHOICE == 0:
                # Set the current day to the sub-menu option selected by the user
                CURRENT_DAY = CURRENT_SUBMENU_CHOICE

            # If current sub-menu is: "Set Hour" sub-menu
            elif CURRENT_MENU_CHOICE == 1:
                # Set the current hour to the sub-menu option selected by the user
                CURRENT_HOUR = CURRENT_SUBMENU_CHOICE
            
            # If current sub-menu is: "Set Minutes" sub-menu
            elif CURRENT_MENU_CHOICE == 2:
                # Set the current minutes to the sub-menu option selected by the user
                CURRENT_MINUTES = CURRENT_SUBMENU_CHOICE
            
            # If current sub-menu is: "Set AM/PM" sub-menu
            elif CURRENT_MENU_CHOICE == 3:
                # Set the current AM/PM to the sub-menu option selected by the user
                CURRENT_AM_PM = CURRENT_SUBMENU_CHOICE
            
            # Create and play the Sub-menu exiting transition audio / Start-menu introduction audio:
            # "<Current sub-menu> set to <selected day / time>. It is <Current Day and Time>. Press L for help. Press semicolon to return to start."
            sound.combine_wav_files(TMP_FILE_WAV, current_set_to_wav, current_submenu_wav_collection[CURRENT_SUBMENU_CHOICE],\
                RETURNING_TO_START_MENU_WAV, IT_IS_WAV, DAYS_WAV[CURRENT_DAY],HOURS_WAV[CURRENT_HOUR],MINUTES_WAV[CURRENT_MINUTES],\
                AM_AND_PM_WAV[CURRENT_AM_PM],PRESS_L_FOR_HELP_WAV,PRESS_SEMICOLON_TO_QUIT_WAV)
            
            sound.Play(TMP_FILE_WAV)

            # Reset the start menu selection pointer to "Set Day"
            CURRENT_MENU_CHOICE = 0
            
            #return to the starting menu (give control back torun_menu() function)
            return 

        if c == HELP_KEY:
            # Create and play the Sub-menu help audio
            # "You are in the <Current sub-menu>. It is <Current Day and Time>. Use the J and K keys... etc." 
            sound.combine_wav_files(TMP_FILE_WAV, YOU_ARE_IN_THE_MENU_WAV[CURRENT_MENU_CHOICE], IT_IS_WAV,DAYS_WAV[CURRENT_DAY],\
                HOURS_WAV[CURRENT_HOUR],MINUTES_WAV[CURRENT_MINUTES],AM_AND_PM_WAV[CURRENT_AM_PM],HELP_WAV)
            
            sound.Play(TMP_FILE_WAV)
        
        if c == QUIT_KEY:
            # Create and play the Sub-menu quit audio
            # "Returning to the starting menu. It is <Current Day and time>. Press L for help. Press semicolon to quit.
            sound.combine_wav_files(TMP_FILE_WAV, RETURNING_TO_START_MENU_WAV, IT_IS_WAV, DAYS_WAV[CURRENT_DAY],HOURS_WAV[CURRENT_HOUR],\
                MINUTES_WAV[CURRENT_MINUTES],AM_AND_PM_WAV[CURRENT_AM_PM],PRESS_L_FOR_HELP_WAV,PRESS_SEMICOLON_TO_QUIT_WAV)
            
            sound.Play(TMP_FILE_WAV)
 
            #Reset the start menu selection pointer to "Set Day"
            CURRENT_MENU_CHOICE = 0
            return
        
        else:
            c = readchar.readchar()

########################################################################################################################################
# Verify all files can be loaded and played.
# Play all sound files to make sure the paths and filenames are correct and valid.
# This program is disabled by default in main()
# This function creates a very long lag time when enabled at the start of the program, due to the many sound files used in the program.
# The programmer may re-enable it, to test each sound file, by uncommenting the verify_sound_filenames() function call line in main().
#######################################################################################################################################
def verify_sound_filenames():
    sound.Play(DAYS_WAV[0])
    sound.Play(DAYS_WAV[1])
    sound.Play(DAYS_WAV[2])
    sound.Play(DAYS_WAV[3])
    sound.Play(DAYS_WAV[4])
    sound.Play(DAYS_WAV[5])
    sound.Play(DAYS_WAV[6])
    sound.Play(MENU_CHOICES_WAV[0])
    sound.Play(MENU_CHOICES_WAV[1])
    sound.Play(MENU_CHOICES_WAV[2])
    sound.Play(MENU_CHOICES_WAV[3])
    sound.Play(HOURS_WAV[0])
    sound.Play(HOURS_WAV[1])
    sound.Play(HOURS_WAV[2])
    sound.Play(HOURS_WAV[3])
    sound.Play(HOURS_WAV[4])
    sound.Play(HOURS_WAV[5])
    sound.Play(HOURS_WAV[6])
    sound.Play(HOURS_WAV[7])
    sound.Play(HOURS_WAV[8])
    sound.Play(HOURS_WAV[9])
    sound.Play(HOURS_WAV[10])
    sound.Play(HOURS_WAV[11])
    sound.Play(MINUTES_WAV[0])
    sound.Play(MINUTES_WAV[1])
    sound.Play(MINUTES_WAV[2])
    sound.Play(MINUTES_WAV[3])
    sound.Play(MINUTES_WAV[4])
    sound.Play(MINUTES_WAV[5])
    sound.Play(MINUTES_WAV[6])
    sound.Play(MINUTES_WAV[7])
    sound.Play(MINUTES_WAV[8])
    sound.Play(MINUTES_WAV[9])
    sound.Play(MINUTES_WAV[10])
    sound.Play(MINUTES_WAV[11])
    sound.Play(MINUTES_WAV[12])
    sound.Play(MINUTES_WAV[13])
    sound.Play(MINUTES_WAV[14])
    sound.Play(MINUTES_WAV[15])
    sound.Play(MINUTES_WAV[16])
    sound.Play(MINUTES_WAV[17])
    sound.Play(MINUTES_WAV[18])
    sound.Play(MINUTES_WAV[19])
    sound.Play(MINUTES_WAV[20])
    sound.Play(MINUTES_WAV[21])
    sound.Play(MINUTES_WAV[22])
    sound.Play(MINUTES_WAV[23])
    sound.Play(MINUTES_WAV[24])
    sound.Play(MINUTES_WAV[25])
    sound.Play(MINUTES_WAV[26])
    sound.Play(MINUTES_WAV[27])
    sound.Play(MINUTES_WAV[28])
    sound.Play(MINUTES_WAV[29])
    sound.Play(MINUTES_WAV[30])
    sound.Play(MINUTES_WAV[31])
    sound.Play(MINUTES_WAV[32])
    sound.Play(MINUTES_WAV[33])
    sound.Play(MINUTES_WAV[34])
    sound.Play(MINUTES_WAV[35])
    sound.Play(MINUTES_WAV[36])
    sound.Play(MINUTES_WAV[37])
    sound.Play(MINUTES_WAV[38])
    sound.Play(MINUTES_WAV[39])
    sound.Play(MINUTES_WAV[40])
    sound.Play(MINUTES_WAV[41])
    sound.Play(MINUTES_WAV[42])
    sound.Play(MINUTES_WAV[43])
    sound.Play(MINUTES_WAV[44])
    sound.Play(MINUTES_WAV[45])
    sound.Play(MINUTES_WAV[46])
    sound.Play(MINUTES_WAV[47])
    sound.Play(MINUTES_WAV[48])
    sound.Play(MINUTES_WAV[49])
    sound.Play(MINUTES_WAV[50])
    sound.Play(MINUTES_WAV[51])
    sound.Play(MINUTES_WAV[52])
    sound.Play(MINUTES_WAV[53])
    sound.Play(MINUTES_WAV[54])
    sound.Play(MINUTES_WAV[55])
    sound.Play(MINUTES_WAV[56])
    sound.Play(MINUTES_WAV[57])
    sound.Play(MINUTES_WAV[58])
    sound.Play(MINUTES_WAV[59])
    sound.Play(AM_AND_PM_WAV[0])
    sound.Play(AM_AND_PM_WAV[1])
    sound.Play(HELP_WAV)
    sound.Play(PRESS_L_FOR_HELP_WAV)
    sound.Play(PRESS_SEMICOLON_TO_QUIT_WAV)
    sound.Play(YOU_ARE_IN_THE_MENU_WAV[0])
    sound.Play(YOU_ARE_IN_THE_MENU_WAV[1])
    sound.Play(YOU_ARE_IN_THE_MENU_WAV[2])
    sound.Play(YOU_ARE_IN_THE_MENU_WAV[3])
    sound.Play(ENTERING_DAY_MENU_WAV)
    sound.Play(YOU_SELECTED_WAV)
    sound.Play(ENTERING_HOUR_MENU_WAV)
    sound.Play(ENTERING_MINUTES_MENU_WAV)
    sound.Play(ENTERING_AM_PM_MENU_WAV)
    sound.Play(IT_IS_WAV)
    sound.Play(DAY_SET_TO_WAV)
    sound.Play(HOUR_SET_TO_WAV)
    sound.Play(MINUTES_SET_TO_WAV)
    sound.Play(AM_PM_SET_TO_WAV)
    sound.Play(PRESS_SEMICOLON_TO_RETURN_TO_START_MENU_WAV)
    sound.Play(RETURNING_TO_START_MENU_WAV)
    sound.Play(CURRENT_SELECTION_IS_WAV)
    sound.Play(PRESS_AGAIN_TO_QUIT_WAV)
    sound.Play(EXITING_PROGRAM_WAV)
    sound.Play(INTRO_WAV)
    
################################################################################
main()
################################################################################
