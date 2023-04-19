import itertools, random
# product() function, performs the Cartesian product of the two sequences.
# The two sequences are numbers from 1 to 13 and the four suits. So, altogether we have 13 * 4 = 52 items in the deck with each card as a tuple
deck = list(itertools.product(range(1,14),["Spade", "Heart", "Diamond", "Club"]))
random.shuffle(deck)
print("You have got :")
for i in range(5):
    print(deck[i][0], "of", deck[i][1])