
def print_about(print_to_console: bool=True, return_text: bool=False)->str:
    text = """
Cloud Console
=============

This is a terminal based user interface that will allow you to view public cloud resources and issue some basic commands to your cloud environment.

The aim is not to replace a Web Based console, but to allow at least some similar functionality from the command line in a guided way that will hide some of the complexities with performing similar tasks using the vendor's own CLI tool.

    """
    if print_to_console is True:
        print(text)
    if return_text is True:
        return text


def start_ui(exit_on_done: bool=True, return_done: bool=False):
    print('Starting UI...')
    if exit_on_done is True:
        exit(0)
    if return_done is True:
        return True


if __name__ == '__main__':
    print_about()

