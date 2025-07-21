from colorama import Fore, Style
from app.config.config import device_name
from datetime import datetime
import re

def len_no_ansi(string) -> str:
    return len(re.sub(
        r'[\u001B\u009B][\[\]()#;?]*((([a-zA-Z\d]*(;[-a-zA-Z\d\/#&.:=?%@~_]*)*)?\u0007)|((\d{1,4}(?:;\d{0,4})*)?[\dA-PR-TZcf-ntqry=><~]))', '', string))

class log:
    def __init__(self, outcome, subject:str, topic:str, message:str, arg:str='', error:object='', abort:bool=True) -> None:
        """ Log object to create standard convension through the project
            for error handleing and clarification """
            
        if error != '':
            error = f'( {Fore.MAGENTA}{error}{Style.RESET_ALL} )'
            
        c = self.classify(outcome)
        
        p1 = f"{device_name} {Fore.CYAN}{subject.upper()}.{topic.lower()}{Style.RESET_ALL}"
        p2 = f"{message} {Fore.YELLOW}{arg}{Style.RESET_ALL} {error}"
        
        indent_size = 45
        len_p1 = len_no_ansi(p1)
        
        date = Fore.CYAN + datetime.now().strftime('%a %b %d %X ') + Style.RESET_ALL
        
        self.msg = f"{date} {c} {p1} {' ' * (indent_size - len_p1)} {p2}"
        # contrust the log
        
        from app.mqtt.mqtt import pub
        pub().publish(f'log', self.msg)
        # publish the log
        
        print(self.msg)
        # print the log
        
        if abort and outcome == False:
            # check if the error requires a restart
            exit() # stop the app
            
    def classify(self, outcome: str) -> str:
        match outcome:
            case 'OK':
                # if it went well:
                return f'[ {Fore.GREEN}OK{Style.RESET_ALL} ]'
            
            case 'ER':
                # if it didn't:
                return f'[ {Fore.RED}ER{Style.RESET_ALL} ]'
            
            case 'FATAL':
                # if it went so badly the greenhouse needs to be restarted (ran into error)
                return f'[ {Fore.RED}FATAL{Style.RESET_ALL} ]'
            
            case 'WAIT':
                # if it is in progress:
                return f'[....]'
            
            case "WARN":
                return f'[{Fore.YELLOW}WARN{Style.RESET_ALL}]'
                
        if type(outcome) == str:
            return f'[{Fore.YELLOW}WARN{Style.RESET_ALL}]'
            
    def __str__(self) -> str:
        #                 ↑ duuuuh...
        return self.msg