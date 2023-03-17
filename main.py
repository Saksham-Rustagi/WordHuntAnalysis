# This is a sample Python script.
import pickle
import random
import time
import boggle


with open('letters.pk', 'rb') as fi:
    letterDict = pickle.load(fi)
with open('boards.pk', 'rb') as fi:
    boards = pickle.load(fi)
with open('allwords.pk', 'rb') as fi:
    allwords = pickle.load(fi)
with open('count.pk', 'rb') as fi:
    simulated_boards = pickle.load(fi)

n_size = 4
best_points = 0
best_board = "aaaaaaaaaaaaaaaa"
points_dict = {
    3: 100,
    4: 400,
    5: 800,
    6: 1400,
    7: 1800,
    8: 2200,
    9: 2600,
    10: 3000,
    11: 3400,
    12: 3800,
    13: 4200,
    14: 4600,
    15: 5000,
    16: 10000
}
dictionary = boggle.get_dictionary('../pythonProject1/bogwords.txt')


def importBoardData():
    board = ""
    # load your data back to memory when you need it

    print(boards)
    print(len(letterDict))
    print(sorted(letterDict.items(), key=lambda kv: (kv[1], kv[0])))

    while board != "1":
        board = input("Input board: ")
        if board == "3":
            total = sum(letterDict.values())
            for x in sorted(letterDict.items(), key=lambda kv: (kv[1], kv[0])):
                print("Percentage of " + x[0] + " is: " + str(x[1] * 100 / total))
            break

        if len(board) != 16:
            continue

        boards.append(board)
        for x in board:
            if x in letterDict:
                letterDict[x] += 1
            else:
                letterDict[x] = 1

    with open('letters.pk', 'wb') as fi:
        pickle.dump(letterDict, fi)

    with open('boards.pk', 'wb') as fi:
        pickle.dump(boards, fi)


def word_freq(arr):
    global simulated_boards, best_points, best_board
    for b in arr:
        simulated_boards += 1
        found_words = boggle.main(b, dictionary,n_size)
        points = 0
        for x in found_words:
            points += points_dict[len(x)]
            if x in allwords[n_size]:
                allwords[n_size][x] += 1
            else:
                allwords[n_size][x] = 1
        if points > best_points:
            best_points = points
            best_board = b

#Word data
def print_word_freqs(sort_by, min_length=None):
    # "L" is length; "A" is alphabetical; "F" is frequency
    min_length = 3 if min_length is None else min_length
    if sort_by == "L":
        for x in sorted(allwords[n_size].items(), key=lambda kv: len(kv[0])):
            print(x[0] + " showed up: " + str(x[1]) + " times")

    elif sort_by == "A":
        for x in sorted(allwords[n_size].items()):
            print(x[0] + " showed up: " + str(x[1]) + " times")

    elif sort_by == "F":
        answer = input("(s)tarts, (e)nds, (c)ontains, (l)ength")
        constr = answer.split(" ")

        starts = ""
        ends = ""
        contains = ""
        for i in range(0, len(constr), 2):
            if constr[i] == "s":
                starts = constr[i+1].upper()
            if constr[i] == "e":
                ends = constr[i+1].upper()
            if constr[i] == "c":
                contains = constr[i+1].upper()
            if constr[i] == "l":
                min_length = int(constr[i+1])

        for x in sorted(allwords[n_size].items(), key=lambda kv: (kv[1], kv[0])):
            if len(x[0]) < min_length:
                continue
            if len(starts) != 0 and x[0][0:len(starts)] != starts:
                continue
            if len(ends) != 0 and x[0][len(x[0]) - len(ends):] != ends:
                continue
            if len(contains) != 0 and (not contains in x[0]):
                continue
            print(x[0] + " showed up: " + str(x[1]) + " times")


def create_boards(n):
    created = []
    for x in range(n):
        stri = "".join(random.choices(list(letterDict), weights=list(letterDict.values()), k=n_size**2))
        created.append(stri)
    return created


def solve_board(b):
    found_words = boggle.main(b, dictionary, n_size)
    found_words = sorted(found_words, key=len)
    boggle.display_words(found_words)
    points = 0
    for x in found_words:
        points += points_dict[len(x)]
    print(points)


if __name__ == '__main__':

    userin = input("What would you like to do? Solve a board(S), Simulate Random board(R), See word data(D), "
                   "Input real boards(I): ")

    if userin.upper() == "S":
        solve_board(input("Input board to Solve: "))

    elif userin.upper() == "R":
        seconds_to_run = int(input("How many seconds to run this for: "))
        start = time.time()
        bcount = 0
        while time.time() < start + seconds_to_run:
            boards_to_test = create_boards(1000)
            word_freq(boards_to_test)
            bcount += 1000
            print("Best board was " + best_board + ", with " + str(best_points) + " points.")

        print(bcount, "boards simulated.")
        print("Best board was " + best_board + ", with " + str(best_points) + " points.")
        userin = input("Do you want to save?")
        if userin.upper() == "YES":
            if best_points > allwords[n_size+5]["bestpoints"]:
                allwords[n_size+5]["bestboard"] = best_board
                allwords[n_size+5]["bestpoints"] = best_points
            with open('allwords.pk', 'wb') as fi:
                pickle.dump(allwords, fi)
            print("There have been", simulated_boards, "simulated boards so far.")
            with open('count.pk', 'wb') as fi:
                pickle.dump(simulated_boards, fi)

    elif userin.upper() == "D":
        userin = input("What would you like to sort by, (l)ength, (f)requency, or (a)lphabetical? ")
        print_word_freqs(userin.strip().upper())

    elif userin.upper() == "I":
        importBoardData()

    elif userin.upper() == "B":
        print("The best board is",allwords[n_size+5]["bestboard"],"with a point score of",allwords[n_size+5]["bestpoints"])
