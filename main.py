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
    dt_string = now.strftime("%d/%m/%Y  | \t\t %H:%M:%S")

    while True:

        print("\n\t\t\t ====================================================================\n")
        print("\nPress 0: To Stop / Terminate")
        print("Press 1: To Continue")
        choice = int(input("Enter your choice : "))
        print("\n\t\t\t ====================================================================\n")
        if choice == 0:
            exit()

        elif choice == 1:
            cardNo = input("Enter a credit card number to validate : ")  # 79927398713-->Valid credit card number
            f.write("\n\t\t\t =================================================================== \n")
            print("\n\t\t\t\t\t Date \t\t | \t\t time  \n",'\t\t\t\t\t' , dt_string, '\n')
            f.write(f'\n\t\t\t\t\t\t\t\t Date \t\t | \t\t time  \n \t\t\t\t\t\t\t\t {dt_string}')
            f.write('\t\t\t ')
            f.write("\n\t\t\t ___________________________________________________________________  ")
            f.write(f'\n\t\t\t\t\tCredit card number       |       {cardNo} ')
            if checkLuhn(cardNo):
                print("This is a valid card \n")
                f.write("\n\t\t\t\t\t     Status              |       Valid\n")
                f.write("\t\t\t ___________________________________________________________________  \n")
                f.write("\n\t\t\t =================================================================== \n")
            else:
                print("This is not a valid card\n")
                f.write("\n\t\t\t\t\t     Status              |       Invalid\n")
                f.write("\t\t\t ___________________________________________________________________  \n")
                f.write("\n\t\t\t =================================================================== \n")
        else:
            print("\n\nInvalid Input....\n\n")
