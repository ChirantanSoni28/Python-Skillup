def most_prolific(dict):
    year = []
    occurences = {}
    maxnumber = 0
    for items in dict.values():
        year.append(items)
    # print(year)
    for y in year:
        if y in occurences:
            occurences[y] = occurences[y] + 1
        else:
            occurences[y] = 1
    for o in occurences:
        if occurences[o] > maxnumber:
            maxyears = []
            maxyears.append(o)
            maxnumber = occurences[o]
        # print(maxnumber)
        # print(maxyears)
        elif occurences[o] == maxnumber and not (o in maxyears):
            maxyears.append(o)
    if (len(maxyears) == 1):
        return maxyears[0]
    else:
        return maxyears

Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963,
                       "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,"Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
                       "Sgt. Pepper's Lonely Hearts Club Band": 1967,
                       "Magical Mystery Tour": 1967, "The Beatles": 1968,
                       "Yellow Submarine": 1969, 'Abbey Road': 1969,
                       "Let It Be": 1970}

print(most_prolific(Beatles_Discography))
