from colorama import Fore, Style
import re

def len_no_ansi(string) -> str:
    return len(re.sub(
        r'[\u001B\u009B][\[\]()#;?]*((([a-zA-Z\d]*(;[-a-zA-Z\d\/#&.:=?%@~_]*)*)?\u0007)|((\d{1,4}(?:;\d{0,4})*)?[\dA-PR-TZcf-ntqry=><~]))', '', string))

class log:
    def __init__(self, device:str, outcome, subject:str, topic:str, message:str, arg:str='', error:object='', abort:bool=True):
        """ I made this log object to create standard convension through the project
            for error handleing and clarification"""
        # if outcome is true it worked, and false; didn't work
        if outcome == True:
            # if it went well:
            c = f'[ {Fore.GREEN}OK{Style.RESET_ALL} ]'
        elif outcome == False:
            # if it didn't:
            c = f'[ {Fore.RED}ER{Style.RESET_ALL} ]'
        elif outcome == None:
            # if it is in progress:
            c = f'[....]'
        elif outcome == "WARN":
            c = f'[{Fore.YELLOW}WARN{Style.RESET_ALL}]'
        elif type(outcome) == str:
            c = f'[{Fore.YELLOW}WARN{Style.RESET_ALL}]'
            
        if error != '':
            error = f'( {Fore.MAGENTA}{error}{Style.RESET_ALL} )'
        
        p1 = f"{device} {c} {Fore.CYAN}{subject.upper()}.{topic.lower()}{Style.RESET_ALL}"
        p2 = f"{message} {Fore.YELLOW}{arg}{Style.RESET_ALL} {error}"
        
        indent_size = 45
        len_p1 = len_no_ansi(p1)
        
        self.msg = p1 + " " * (indent_size - len_p1) + p2
        from app.mqtt.mqtt import pub
        pub().publish(f'log', self.msg)
        # send the log to the sever
        
        print(self.msg)
        # finally I construct, send and print the message!
        if abort and outcome == False:
            exit()
            
    def __str__(self):
        return self.msg