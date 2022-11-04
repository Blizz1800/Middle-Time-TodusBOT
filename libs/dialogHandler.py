
def generateDialog(file, *subs):
    dialog = ""
    file = open(file, 'rb')
    dialog = file.read()
    file.close()
    dialog = dialog.decode('utf-8').format(*subs)
    return dialog