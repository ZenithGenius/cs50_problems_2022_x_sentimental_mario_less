from cs50 import get_int

while True:
    # get the height in the range
    height = get_int("Height: ")
    if height > 0 and height < 9:
        break
# iterate through height to ptint the pyramid
for row in range(height):
    for space in range(height - row - 1, 0, -1):
        # print spaces
        print(" ", end="")
    for hash in range(row + 1):
        # print hashes
        print("#", end="")
    print("\n", end="")