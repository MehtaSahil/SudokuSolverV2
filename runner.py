from puzzle import Puzzle
from square import Square

if __name__ == '__main__':
    print('initializing')
    # Dummy board for now (all ones)
    p = Puzzle([[1] * 9 for _ in range(9)])
    p.set(0, 0, 5)
    print('done')