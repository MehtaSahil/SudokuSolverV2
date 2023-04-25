from puzzle import Puzzle
from square import Square

if __name__ == '__main__':
    print('initializing')
    # Dummy board for now (all ones)
    p = Puzzle([[1] * 9 for _ in range(9)])
    p.set(0, 0, 5)
    print(p.isSolved())

    for r in range(9):
        for c in range(9):
            p.set(r, c, 8)
        
        p.reset(r, 0)

    print('done')