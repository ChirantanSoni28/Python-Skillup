def create_cast_list(filename):
    cast_list = []
    with open(filename) as x:
       for line in x:
           l = line.split(",")
           cast_list.append(l[0])
    return cast_list




print(create_cast_list('/Chirantan/flying_circus.txt'))
