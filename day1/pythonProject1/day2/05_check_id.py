import checkIsraelID

if __name__ == "__main__":
    try:
        valid = checkIsraelID.checkID("abcdefg")
        print(valid)
    except checkIsraelID.IDExseption:
        print("ID length must be between 7 and 9 characters")
    except ValueError:
        print("ID should include only digits")



