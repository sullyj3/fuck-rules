def match(command, settings):
    return ('pacin' in command.script)

def get_new_command(command, settings):
    return 'sudo {}'.format(command.script)
