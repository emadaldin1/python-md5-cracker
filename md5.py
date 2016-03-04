import hashlib
def md5hash(data):
    a = ""
    m = hashlib.md5()
    m.update(data)
    a = m.hexdigest()
    return a
try:
    with open('worldlist.txt') as file:
        pass
except IOError as e:
    print "Unable to find file worldlist.txt"
    exit()
link = raw_input("enter hash name :" )
with open("worldlist.txt") as f:
    for line in f:
        text = line.rstrip()
        md5hash(text)
        if link == md5hash(text):
            print("pass: {}, hash: {}".format(text, link))
            break
        else:
            print md5hash(text)
            print("Does not match.")


