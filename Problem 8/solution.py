def cannons_ready(gunners):
    x = True

    for g in gunners.values():
        if g != "aye":
            x = False

    if x == False:
        return "Shiver me timbers!"
    else:
       return "Fire!"
