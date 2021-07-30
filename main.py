import stdiomask


def checkUsername(name):
    with open("user.txt") as myfile:
        while myfile:
            line = myfile.readline()
            if line.strip() == name:
                return True
            if line == "":
                return False
                break



def getIndex(name):
    count = 0
    with open("user.txt") as fp:
        for line in fp:
            if line.strip() == name:
                return count

            count += 1

def checkPass(name, psw):
    index = getIndex(name)
    with open("pass.txt") as f:
        data = f.readlines()

        if str(psw) == data[index]:
            return True
        return False

def writeInfo(name, psw):
    with open("user.txt", "a") as f:
        f.write("\n")
        f.write(name)

    with open("pass.txt", "a") as p:
        p.write("\n")
        p.write(str(psw))

def hide():
    passw = stdiomask.getpass()


