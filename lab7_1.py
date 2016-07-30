def showCPU():
    import platform
    return str(platform.processor())


def showOS():
    import os
    return str(os.name)


def getSysInfo():  # function declaration
    import platform  # function body
    result = "System Info: \n"
    result += "system: " + platform.system() + "\n"
    result += "machine: " + platform.machine() + "\n"
    result += "platform: " + platform.platform() + "\n"
    result += "uname: " + str(platform.uname()) + "\n"
    result += "version: " + platform.version() + "\n" # end of function
    return result


def getEV():
    import os
    return str(os.environ['USERNAME'])


def main():
    s = "--------------------------\n"
    s += " A. Show CPU info \n"
    s += " B. Show OS info \n"
    s += " C. Show System info \n"
    s += " D. Show User name \n"
    s += "--------------------------\n"
    s += "Enter your choice [A/B/C/D]:"
    import InputBox
    InputBox.ShowDialog(s)
    s = InputBox.GetInput()
    s = s.upper()
    msg = ""
    if s == 'A': msg = showCPU()
    elif s == 'B': msg = showOS()
    elif s == 'C': msg = getSysInfo()
    elif s == 'D': msg = getEV()
    else: msg = "Invalid option!"

    import MessageBox
    MessageBox.Show(msg)

if __name__ == "__main__":
    main()

