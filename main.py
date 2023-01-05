from datetime import datetime

f = open("cardNumber.txt", 'a')


def checkLuhn (cardNum):
    nDigits = len(cardNum)
    nSum = 0
    isSecond = False

    for i in range(nDigits - 1, -1, -1):
        d = ord(cardNum[i]) - ord('0')

        if isSecond == True:
            d = d * 2

        nSum += d // 10
        nSum += d % 10

        isSecond = not isSecond

    if nSum % 10 == 0:
        return True
    else:
        return False


def title():
    print('\n')
    print("\t\t\t ====================================================================")
    print("\t\t\t ||                            LUHN ALGORITHM                      ||")
    print("\t\t\t ====================================================================")
    print('\n')


if __name__ == "__main__":

    title()

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    while True:

        print("\nPress 0: To Stop / Terminate")
        print("Press 1: To Continue")
        choice = int(input("Enter your choice : "))

        if choice == 0:
            exit()

        elif choice == 1:
            cardNo = input("Enter a credit card number to validate : ")  # 79927398713-->Valid credit card number
            f.write("\n\t\t\t =================================================================== \n")
            print("\nDate and time => ", dt_string, '\n')
            f.write(f'\nDate and time                  : {dt_string}')
            f.write("\n")
            f.write(f'credit card number             : {cardNo} ')

            if checkLuhn(cardNo):
                print("This is a valid card \n")
                f.write("\nStatus                         : Valid credit card Number\n")
                f.write("\n\t\t\t =================================================================== \n")
            else:
                print("This is not a valid card\n")
                f.write("\nStatus                         : Invalid credit card number\n")
                f.write("\n\t\t\t =================================================================== \n")
        else:
            print("\n\nInvalid Input....\n\n")
