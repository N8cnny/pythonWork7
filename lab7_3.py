def month_payment(p, r, n):
    import math
    r = (r/12)/100
    return (r + (r / (((1+r)**n) - 1))) * p


def total_payment(mp, n):
    return mp * n


def total_paid_interest(tp, p):
    return tp - p


def FV(p, r, n):
    n = n/12
    r = r/100
    return p * ((1+r)**n)


def main():
    import InputBox
    InputBox.ShowDialog("Enter the principal: ")
    p = float(InputBox.GetInput())

    InputBox.ShowDialog("Enter the annual interest rate: ")
    r = float(InputBox.GetInput())

    InputBox.ShowDialog("Enter the total number of payments: ")
    n = int(InputBox.GetInput())

    mp = month_payment(p, r, n)

    tp = total_payment(mp, n)

    ti = total_paid_interest(tp, p)

    fv = FV(p, r, n)

    s = "--------REPORT---------\n"
    s += "Total payment: " + '${:,.2f}'.format(tp) + "\n"
    s += "Monthly payment: " + '${:,.2f}'.format(mp) + "\n"
    s += "Total paid interest: " + '${:,.2f}'.format(ti) + "\n"
    s += "Future value: " + '${:,.2f}'.format(fv) + "\n"

    import MessageBox
    MessageBox.Show(s)

if __name__ == "__main__":
    main()
