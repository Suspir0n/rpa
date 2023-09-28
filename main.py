import pyautogui
from time import sleep
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG,
    datefmt='%d-%b-%y %H:%M:%S'
)
logger = logging.getLogger(__name__)

class RPAAutomatizeBackupInGoogleDrive:

    def __init__(self):
        logging.info('\033[1;34mInitializing the program\033[m')
        pyautogui.alert('O codigo vai começar, por favor, não toque no teclado enquanto o codigo está rodando!')
        logging.info('\033[1;34mThe program has started, thank you for choosing our service!\033[m')
        pyautogui.PAUSE = 1
        logging.info('\033[1;34mOpening google on your computer\033[m')
        self.open_google_my_computer()
        logging.info('\033[1;34mGoogle opened successfully\033[m')
        sleep(1.5)
        logging.info('\033[1;34mAccessing google drive in your browser\033[m')
        self.open_google_drive_my_browser()
        logging.info('\033[1;34mWebsite loaded successfully\033[m')
        logging.info('\033[1;34mAccessing your desktop\033[m')
        self.open_my_workspace_of_computer()
        logging.info('\033[1;34mMoving the file\033[m')
        self.click_file_for_backup_and_drag()
        logging.info('\033[1;34mOpening the browser again with the website loaded\033[m')
        self.opening_google_drive()
        logging.info('\033[1;34mDrag the file to Google Drive\033[m')
        self.let_file_at_google_drive()
        sleep(5)
        logging.info('\033[1;34mProgram ending\033[m')
        logging.info('\033[1;34mThank you for using our automated service!\033[m')
        self.finish()

    def open_google_my_computer(self) -> None:
        pyautogui.press('winleft')
        pyautogui.write('chrome')
        pyautogui.press('enter')

    def open_google_drive_my_browser(self) -> None:
        pyautogui.write('https://drive.google.com/drive/u/0/my-drive')
        pyautogui.press('enter')

    def open_my_workspace_of_computer(self) -> None:
        pyautogui.hotkey('winleft', 'd')

    def click_file_for_backup_and_drag(self) -> None:
        pyautogui.moveTo(1856, 54)
        pyautogui.mouseDown()
        pyautogui.moveTo(3726, 738)

    def opening_google_drive(self) -> None:
        pyautogui.hotkey('alt', 'tab')

    def let_file_at_google_drive(self) -> None:
        pyautogui.mouseUp()

    def finish(self) -> None:
        pyautogui.alert('O codigo acabou de rodar, pode usar seu computador de novo!')


start = RPAAutomatizeBackupInGoogleDrive()

