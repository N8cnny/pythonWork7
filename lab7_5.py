def setDateTime():
    import datetime
    global dt # set dt in global namespace
    dt = datetime.datetime.now() # get current date/time


def getCurrentTime():
    h = dt.strftime("%H")
    m = dt.strftime("%M")
    s = dt.strftime("%S")
    localTime = h + ":" + m + ":" + s
    import MessageBox
    MessageBox.Show("You chose 1:\n\n" + localTime)


def getCurrentDate():
    m = dt.month
    d = dt.day
    y = dt.year
    s = str(m) + "/" + str(d) + "/" + str(y)
    import MessageBox
    MessageBox.Show("You chose 2 :\n\n" + s)


def countdown():
    mon = 12 - dt.month
    day = 31 - dt.day
    hr = 23 - dt.hour
    min = 60 - dt.minute
    sec = 60 - dt.second
    s = "You need to wait "
    s = s + str(mon) + " month(s) "
    s = s + str(day) + " day(s) "
    s = s + str(hr) + " hour(s) "
    s = s + str(min) + " minutue(s) "
    s = s + str(sec) + " second(s) "
    s = s + "to " + str(dt.year+1) + "\'s New Year Day!"
    import MessageBox
    MessageBox.Show("\n" + s + "\n")


def main():
    s = "--------------M E N U---------------\n"
    s += " 1. Display current time \n"
    s += " 2. Display current date \n"
    s += " 3. Count down to New Year\'s Day \n"
    s += "-----------------------------------\n\n"
    s += "Enter your choice [1/2/3]: "
    import InputBox
    InputBox.ShowDialog(s)
    i = int(InputBox.GetInput())
    if i == 1:
        setDateTime()
        getCurrentTime()
    elif i == 2:
        setDateTime()
        getCurrentDate()
    elif i == 3:
        setDateTime()
        countdown()
    else:
        print("Invalid option!!!\n")
        main()
if __name__ == "__main__":
    main()
