import rich
from rich.panel import Panel
from rich.text import Text

from pypass.helpers import *

def print_credential(user_auth, credential, show_pw=False, verbose=False):
    credential = decrypt_row(credential, user_auth, decrypt_pw=True, to_dict=True)
    text = Text()
    text.append("NAME: ", style="bold")
    text.append(credential["name"])
    text.append("\nID  : ", style="bold")
    text.append(credential['user_id'])
    text.append("\nPW  : ", style="bold")
    if show_pw:
        text.append(credential['user_pw'])
    else:
        text.append("****")
    text.append("\nURL : ", style="bold")
    text.append(credential["url"])
    if verbose:
        text.append("\nDate Created: ", style="bold")
        text.append(format_date_from_ts(credential["date_created"]))
        text.append("\nDate Modified: ", style="bold")
        text.append(format_date_from_ts(credential["date_modified"]))
    
    panel = Panel(text, title=credential["name"])
    rich.print(panel)