from colorama import Fore, Style

class log:
    def __init__(self, outcome, subject:str, topic:str, message:str, arg:str='', error:object='', abort:bool=True):
        """ I made this log object to create standard convention through the project
            for error handling and clarification."""
        # if outcome is true it worked, and false; didn't work
        if outcome == True:
            # if it went well:
            c = f'[ {Fore.GREEN}OK{Style.RESET_ALL} ] '
        elif outcome == False:
            # if it didn't:
            c = f'[ {Fore.RED}ER{Style.RESET_ALL} ] '
        elif outcome == None:
            # if it is in progress:
            c = f'[....] '
        elif type(outcome) == str:
            c = f'[ {outcome} ]'
            
        if error != '':
            error = f'( {Fore.MAGENTA}{error}{Style.RESET_ALL} )'
        
        p1 = f"{Fore.CYAN}{subject.upper()}.{topic.lower()}{Style.RESET_ALL}\t "
        p2 = f"{message} {Fore.YELLOW}{arg}{Style.RESET_ALL} {error}"
        if outcome == None: p1 = ''
        
        self.msg = f"{c}{p1}{p2}".expandtabs(18)
        print(self.msg)
        # finally I construct and print the message!
        if abort and outcome == False:
            exit()
            
    def __str__(self):
        return self.msg
