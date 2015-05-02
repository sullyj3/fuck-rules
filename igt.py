def match(command, settings):
    return ('igt' in command.script)

def get_new_command(command, settings):
    return command.script.replace("igt", "git", 1)
