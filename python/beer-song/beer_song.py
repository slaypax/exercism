def recite(start=99, take=1):
    song = []
    for i in range(start, start - take, -1):
        if i == 2:
            song.append("2 bottles of beer on the wall, 2 bottles of beer.")
            song.append("Take one down and pass it around, 1 bottle of beer on the wall.")
            song.append("")
        elif i == 1:
            song.append("1 bottle of beer on the wall, 1 bottle of beer.")   
            song.append("Take it down and pass it around, no more bottles of beer on the wall.") 
            song.append("")
        elif i == 0:                 
            song.append("No more bottles of beer on the wall, no more bottles of beer.")
            song.append(f"Go to the store and buy some more, {start} bottles of beer on the wall.")
        else:
            song.append(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            song.append(f"Take one down and pass it around, {i - 1} bottles of beer on the wall.")    

    print(song)
    return song
