import crossword_tools
import constants
import crossword_gui
import solver
import time

def delay():
    print("")
    print("Next Puzzle")
    time.sleep(1)
    
def main():
    puzzleMap = []
    width = constants.PUZZLE_WIDTH_STR
    height = constants.PUZZLE_HEIGHT_STR
    pfile = open("puzzle.txt", "r") 
    for line in pfile.readlines():
        line = line.replace(" ", "")
        line = line.replace("\n", "")
        puzzleMap.append(line)
    for x in range(len(puzzleMap)):
        on_puzzle_retrieval(crossword_tools.generate_puzzle(puzzleMap[x]))

def on_puzzle_retrieval(puzzle):
    crossword_tools.print_puzzle(puzzle)
    word_bank = []
    word_count = 0
    
    wfile = open("English words 3000.txt","r")
    for word in wfile.readlines():
        word_count += 1
        word = word.replace("\n", "")
        word_bank.append(word)

    print(constants.SOLVING_STR)
    start_time = time.clock()
    solutions = solver.solve(puzzle, word_bank)
    end_time = time.clock()
    diff = end_time - start_time
    seconds = round(diff)
    mills = round((diff - seconds) * 1000)
    
    if seconds == 1:
        seconds_ending = ''
    else:
        seconds_ending = 's'
        
    if mills == 1:
        mills_ending = ''
    else:
        mills_ending = 's'
        
    print(constants.SOLVE_TIME_STR.format(seconds, seconds_ending, mills, mills_ending))
    
    if solutions:
        print(constants.DISPLAYING_SOLUTIONS_STR)
        crossword_gui.display_puzzle_solutions(puzzle, solutions, lambda:delay())
    else:
        user_input = input(constants.NO_SOLUTIONS_STR)

main();