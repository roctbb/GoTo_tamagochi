def get_name():
    file = open("names.txt")
    data = file.read()
    print(data)

get_name()