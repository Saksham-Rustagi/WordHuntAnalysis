from string import ascii_uppercase
from random import choice


def make_grid(width, height):
    """ Create a grid of width * height of uppercase ascii characters"""
    temp = {(row, col): choice(ascii_uppercase) for row in range(height)
            for col in range(width)}
    return temp

def make_grid_from_string(str, n):
    temp = {(row, col): str[n*row+col].upper() for row in range(n)
            for col in range(n)}
    return temp


def neighbours_of_a_position(row, col):
    """ Returns all the neighbouring positions of (row,col)"""
    return [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
            (row, col - 1),                     (row, col + 1),
            (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]


def all_grid_neighbours(grid):
    """Returns a dictionary of all the neighbours of position (row,col) only if
    they exist within the grid
    """
    neighbours = {}
    for position in grid:
        row, col = position
        position_neighbours = neighbours_of_a_position(row, col)
        neighbours[position] = [p for p in position_neighbours if p in grid]
    return neighbours


def path_to_word(grid, path):
    """Returns a list of grid coordinates for each potential path to a word"""
    return ''.join([grid[p] for p in path])


def is_a_real_word(word, dictionary):
    return word in dictionary


def search(grid, dictionary):
    """ Unpacks sets from dictionary and gets neighbours from function
    Adds any paths that are valid to words.
    """
    neighbours = all_grid_neighbours(grid)
    paths = []
    full_words, stems = dictionary

    def do_search(path):
        """
        Inner function recursively searchs
        """
        word = path_to_word(grid, path)
        if is_a_real_word(word, full_words):
            paths.append(path)
        if word not in stems:
            return
        for next_pos in neighbours[path[-1]]:
            if next_pos not in path:
                do_search(path + [next_pos])
    for position in grid:
        do_search([position])
    words = []
    for path in paths:
        words.append(path_to_word(grid, path))
    return set(words)


def get_dictionary(dictionary_file):
    """Returns two sets of fullwords and stems.
    Strips empty space and capitalises words from dictionary_file.
    Iterates from 1 to length of the word found and adds to stems set.
    """
    full_words, stems = set(), set()

    with open(dictionary_file) as f:
        for word in f:
            word = word.strip().upper()
            if 3 <= len(word) <= 16:
                full_words.add(word)

                for i in range(1, len(word)):
                    stems.add(word[:i])
    print("Dictionary got")
    return full_words, stems


def display_words(words):
    """Prints the actual words found and a total number of words found"""
    for word in words:
        print (word)
    print ("Found {0} words".format(len(words)))


def main(str, dictionary, board_size):
    """
    Defines grid size and runs functions in correct order to solve boggle puzzle
    """
    grid = make_grid_from_string(str,board_size)
    words = search(grid, dictionary)
    return words