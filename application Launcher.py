import os
print("\t   Application Launcher\n")
print("\tBrowser\n")
print(" 1.Chrome\t2.Mozila Firefox\n")
print("\tMicrosoft Office\n")
print(" 1.Excel\t2.Powerpoint\t3.Word\n")
print("\tAccess Drive\n")
print(" 1.Drive C\t2.Drive D\t3.Explorer\n ")
print("\tEditor\n")
print(" 1.Notepad\t2.Stickynote\n")
print("\tPython Editor\n")
print(" 1.IDLE\t2.Juypter Notebook\n")
print("\tmedia player\n")
print(" 1.VLC\t2.window media player\n")

print("\t\tExit\n")
while(True):

    app=input("Enter application name which you want to run : ")
    if("Chrome"  in app) or ("CHROME" in app) or ("Google" in app):
        os.system("start Chrome")
    elif("Firefox" in app)or("FIREFOX" in app) or ("mozila" in app) or ("MOZILA" in app):
        os.system("start FireFox")
    elif("excel" in app)or ("EXCEL" in app):
        os.system("start excel.exe")
    elif("POWERPOINT"  in app)or ("powerpoint" in app)or ("powerpoint" in app):
        os.system("start powerpnt")
    elif("WORD" in app)or ("word" in app):
        os.system("start WinWord.exe")
    elif("WORD" in app)or ("word" in app):
        os.system("start WinWord.exe")
    elif("explorer" in app)or ("EXPLORER" in app)or ("Explorer" in app):
        os.system("start explorer.exe")
    elif("notepad" in app)or ("NOTEPAD" in app):
        os.system("start notepad")

    elif("stickynote" in app)or ("STICKYNOTE" in app):
        os.system("start stikynot")

    elif("IDLE" in app)or ("PYTHON" in app)or("idle" in app)or ("python" in app):
        os.system("start IDLE")

    elif("jupyter" in app)or ("jupyter notebook" in app)or("Juypter" in app)or ("JUYPTER" in app):
        os.system("start jupyter notebook")

    elif("VLC" in app)or ("vlc" in app):
        os.system("start VLC")
    elif("wmplayer" in app)or ("media" in app)or ("player" in app):
        os.system("start wmplayer")
        
    elif("D" in app)or ("d" in app):
        os.system("start D:")

    elif("c" in app)or ("C" in app):
        os.system("start C:")
        
    elif("exit" in app)or ("quit" in app):
        break
