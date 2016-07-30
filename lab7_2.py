def getFactorial(x):
    fac = 1
    for i in x:
        fac = fac * i
    return fac


def getSum(x):
    sum = 0
    for i in x:
        sum = sum + i
    return sum


def getAverage(x):
    avg = getSum(x) / len(x)
    return avg


def main():
    import InputBox
    InputBox.ShowDialog("Enter the maxium: ")
    max = int(InputBox.GetInput())
    x = range(1, max+1)
    s = "You entered: " + str(max) + "\n"
    s += "Range: " + str(x) + "\n"
    s += "\n----Report------\n"
    s += "Factorial: " + str(getFactorial(x)) + "\n"
    s += "Sum: " + str(getSum(x)) + "\n"
    s += "Average: " + str(getAverage(x)) + "\n"
    import MessageBox
    MessageBox.Show(s)

if __name__ == "__main__":
    main()
