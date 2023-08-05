height = 100
bounce = 0

while bounce < 10:
    bounce += 1
    height *= 0.6
    print(bounce, round(height, 4))
