with open("input.txt", "r") as f:
    inputs = f.read()

def startOfMessage(length):
    for i in range(0, len(inputs)):
        if len(set(inputs[i:i+length])) == length:
            return i + length

print("Start of the message #1: {}".format(startOfMessage(4)))
print("Start of the message #1: {}".format(startOfMessage(14)))
