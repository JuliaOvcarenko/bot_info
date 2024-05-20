a = "Huh huh huH"
a = a.split()
print(" ".join([b[0].capitalize() + b[1:] for b in a]))