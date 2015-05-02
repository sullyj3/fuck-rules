def match(command, settings):
    return (command.script == ":q")

def get_new_command(command, settings):
    return "exit"
