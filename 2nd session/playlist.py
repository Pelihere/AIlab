
playlist = ["Shape of You", "Blinding Lights", "Believer", "Perfect"]

print("Number of songs:", len(playlist))


print("First song:", playlist[0])
print("Last song:", playlist[-1])

playlist.append("Dynamite")

playlist.remove("Believer")

playlist.sort()
print("Sorted playlist:", playlist)

for number, song in enumerate(playlist, start=1):
    print(f"{number}. {song}")