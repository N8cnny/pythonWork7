def main():
    x = []

    def populate():
        for i in range(0, 47):
            x.insert(i, i + 1)

    def shuffle():
        import random
        for i in range(0, 47):
            n = random.randint(0, 46)
            temp = x[n]
            x[n] = x[i]
            x[i] = temp

    def showIt():
        import random
        s = ""
        for i in range(0, 5):
            s = s + str(x[i]) + " "
        s = s + "mega: " + str(random.randint(1, 27))
        return s

    def showDialog():
        import InputBox
        InputBox.ShowDialog("How many drawings?: ")
        n = int(InputBox.GetInput())
        i = 0
        result = ""
        while i < n:
            shuffle()
            result += showIt() + "\n"
            i = i + 1

        import MessageBox
        MessageBox.Show(result)

    populate()
    showDialog()
main()

