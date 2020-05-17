import pyautogui
import time
import os

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

dir_path = os.path.dirname(os.path.realpath(__file__))
sep = os.sep
screenshots_folder = dir_path + sep + "screenshots" + sep
screen_dim = pyautogui.size()

"just a small indicator thing to show that the script is beginning"
def initiation():
    print("Starting bot")
    time.sleep(0.5)
    for i in range(1,4):
        print(4-i)
        time.sleep(1)
    print("BEGIN!")

"sensor function determining the mouse position"
def mouseposition(duration):
    for i in range(duration*5 + 1):
        print("location is: ", end="")
        print(pyautogui.position())
        time.sleep(1/5)

"clicks the image if it's there, does nothing  if it's not"
def click_image(location, con=0.9):
    spot = pyautogui.locateCenterOnScreen(location, confidence=con)
    if spot:
        pyautogui.click(spot)

"""Waits until the specified image appears on screen, throws exception
if image not found within specified duration (or time up)"""
def wait_until_appears(image, wait_duration=10, con=1, reg=None):
    if reg == None:
        reg = (0, 0) + pyautogui.size()

    been_found = False
    for i in range(wait_duration*2):
        if not pyautogui.locateOnScreen(image, confidence=con, region=reg):
            been_found = True
            break;
        time.sleep(0.5)

    if not been_found:
        raise Exception("Image not found")

def wait_until_one_appears(image_lst, wait_duration, con=1, reg= None):
    if reg == None:
        reg = (0, 0) + pyautogui.size()

    been_found = False
    for i in range(wait_duration*2):
        for image in image_lst:
            if pyautogui.locateOnScreen(image, confidence=con, region=reg):
                been_found = True
                break;
        time.sleep(0.5)

"Function checking whether and image appeared on screen within indicated duration"
def check_if_appears(image, check_duration=10, con=1, reg=None):
    if reg == None:
        reg = (0, 0) + pyautogui.size()

    been_found = False
    for i in range(check_duration):
        print("######checking######")
        if pyautogui.locateOnScreen(image, confidence=con, region=reg):
            been_found = True
            break;
        time.sleep(0.5)
    return been_found

"logs into the account"
def login(username="lamaboti", password="iamabot1"):
    "Opens up league of legends"
    click_image(screenshots_folder + "pregame" + sep + "windows_start_logo.png")
    pyautogui.write("League of Legends")
    for i in range(10):
        if check_if_appears(screenshots_folder + "pregame" + sep + "league_start_menu.PNG", con=0.7):
            break;
        print("====> finding league logo...")
        time.sleep(0.5)
    click_image(screenshots_folder + "pregame" + sep + "league_start_menu.PNG")

    "logs in"
    print("====> logging in...")
    username_loc = None
    for i in range(20):
        username_loc = pyautogui.locateCenterOnScreen(screenshots_folder + "pregame" + sep + "login_username1.PNG", confidence=0.9)
        if username_loc:
            break;
        username_loc = pyautogui.locateCenterOnScreen(screenshots_folder + "pregame" + sep + "login_username2.PNG", confidence=0.9)
        if username_loc:
            break;
        time.sleep(0.5)

    if not username_loc:
        print(username_loc)
        raise Exception("username bar not found/covered")
    pyautogui.click(username_loc)

    print("====> typing Username and password...")
    pyautogui.write(username)
    click_image(screenshots_folder + "pregame" + sep + "login_password.png")
    pyautogui.write(password)
    click_image(screenshots_folder + "pregame" + sep + "enter_league.png")


    for i in range(30):
        print("====> waiting for Play button(s)...")
        play_button = pyautogui.locateCenterOnScreen(screenshots_folder + "pregame" + sep + "loginPLAY_button.png", confidence=0.5)
        if play_button:
            print("====> found large PLAY button")
            pyautogui.click(play_button)
            break;
        play_button = pyautogui.locateCenterOnScreen(screenshots_folder + "pregame" + sep + "play_button.png", confidence=0.5)
        if play_button:
            print("====> large PLAY button omitted")
            pyautogui.click(play_button)
            break;
        time.sleep(1)

"Set ups a game from the home-screen"
def start_queue():
    print("====> setting up queue...")
    "Clicks the play/party button in the top-right"
    wait_until_appears(screenshots_folder + "pregame" + sep + "play_button.png", 40)
    start_button = pyautogui.locateCenterOnScreen(screenshots_folder + "pregame" + sep + "play_button.png")

    if not start_button:
        start_button = pyautogui.locateCenterOnScreen(screenshots_folder + "pregame" + sep + "party_play_button.png")
    pyautogui.click(start_button)

    "selects co-op vs AI and starts queue"
    co_op_v_ai_loc = pyautogui.locateCenterOnScreen(screenshots_folder + "pregame" + sep + "co_op_v_ai.PNG")
    if not co_op_v_ai_loc:
        click_image(screenshots_folder + "pregame" + sep + "co_v_ai.png")

"Finds a match and presses play"
def find_match():
    print("====> starting queue...")
    click_image(screenshots_folder + "pregame" + sep + "confirm_button.png")
    pyautogui.moveTo(960, 540)
    click_image(screenshots_folder + "pregame" + sep + "find_match_button.png", 0.5)
    wait_until_appears(screenshots_folder + "pregame" + sep + "accept_button.png", 40)
    click_image(screenshots_folder + "pregame" + sep + "accept_button.png")

"Picks a champion and sets up runes and masteries if possible"
def pick_champ():
    print("====> Selecting champion...")
    lock_in_loc = pyautogui.locateCenterOnScreen(screenshots_folder + "champ_select" + sep + "lock_in(grey).png", confidence=0.8)
    click_image(screenshots_folder + "champ_select" + sep + "adc_role.png", 0.8)
    for i in range(1, 20):
        select_champ = pyautogui.locateCenterOnScreen(screenshots_folder + "champ_select" + sep + str(i) + ".png", confidence=0.8)
        if select_champ:
            pyautogui.click(select_champ)
            pyautogui.click(lock_in_loc)
            time.sleep(0.5)
            if not pyautogui.locateCenterOnScreen(screenshots_folder + "champ_select" + sep + str(i + 1) + ".png", confidence=0.8):
                break;

"Accept games and sets up champ select"
def start_game():
    find_match()
    pick_champ()

time.sleep(1)
editloc = pyautogui.locateCenterOnScreen(screenshots_folder + "champ_select" + sep + "edit_runes.png", confidence=0.8)
pyautogui.click(editloc)
print(screen_dim[0], screen_dim[1])
pyautogui.move(-screen_dim[0]/10, -screen_dim[1]*8/15)
pyauto.click()


"===================[MAIN FUNCTION(S)]==================="
def play_game(num=1):
    start_queue()
    for i in range(num):
        start_game()

# def main():
#     "Starts my bot"
#     initiation()
#     login()
#
#     play_game()
#
#
# if __name__ == "__main__":
#     main()
#     print(">>>>>>>>>[DONE]<<<<<<<<<")
