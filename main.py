from menu_main import MenuMain
from data_base import Db

class Main:
    def __init__(self) -> None:
        print("Program starting.")
        # 1. Initialize
        main_menu= MenuMain()
        # 2. Operate
        main_menu.start()
        # 3. Cleanup
        Db.close()
        print("Program ending.")
        return None

    

if __name__=="__main__":
    app = Main()