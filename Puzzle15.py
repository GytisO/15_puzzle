from random import shuffle

class Puzzle15:
    move_count = 0

    def __init__(self):
        self.lst = {}
        self.lst2 = []
        self.current_position = None
        self.to_position = None

    def table(self):
        '''Printing game table'''
        i = self.lst2
        print('\n+----+----+----+----+')
        print(f'| {i[0]} | {i[1]} | {i[2]} | {i[3]} |')
        print('+----+----+----+----+')
        print(f'| {i[4]} | {i[5]} | {i[6]} | {i[7]} |')
        print('+----+----+----+----+')
        print(f'| {i[8]} | {i[9]} | {i[10]} | {i[11]} |')
        print('+----+----+----+----+')
        print(f'| {i[12]} | {i[13]} | {i[14]} | {i[15]} |')
        print('+----+----+----+----+\n')

    def data(self):
        '''Generating data dictionary and list'''
        for num in range(1, 17):
            self.lst[num] = self.beautify(str(num))
        for a, b in self.lst.items():
            if b.strip() == '16':
                self.lst[a] = '  '
                break
        self.lst2 = list(self.lst.values())
        shuffle(self.lst2)
        self.current_position = self.lst2.index('  ')

    def beautify(self, num):
        '''Correcting spaces shown in the table'''
        num = num.strip()
        if len(num) == 1:
            return ' '+num
        elif len(num) == 2:
            return num

    def movement(self):
        '''Possible moves for the blank tile'''
        current_position = self.current_position
        if current_position in [5, 6, 9, 10]:
            return self.lst2[current_position - 4], self.lst2[current_position - 1], self.lst2[current_position + 1], self.lst2[current_position + 4]
        elif current_position in [4, 8]:
            return self.lst2[current_position - 4], self.lst2[current_position + 4], self.lst2[current_position + 1]
        elif current_position in [7, 11]:
            return self.lst2[current_position - 4], self.lst2[current_position + 4], self.lst2[current_position - 1]
        elif current_position in [1, 2]:
            return self.lst2[current_position - 1], self.lst2[current_position + 1], self.lst2[current_position + 4]
        elif current_position in [13, 14]:
            return self.lst2[current_position - 1], self.lst2[current_position + 1], self.lst2[current_position - 4]
        elif current_position == 0:
            return self.lst2[current_position + 1], self.lst2[current_position + 4]
        elif current_position == 3:
            return self.lst2[current_position - 1], self.lst2[current_position + 4]
        elif current_position == 12:
            return self.lst2[current_position + 1], self.lst2[current_position - 4]
        elif current_position == 15:
            return self.lst2[current_position - 1], self.lst2[current_position - 4]

    def change(self, to_position):
        '''Tile movement and list update'''
        from_position = self.current_position
        to_position = str(to_position)
        if len(to_position) == 1:
            to_position = str(' ' + to_position)
        from_position, to_position = self.lst2.index(
            '  '), self.lst2.index(str(to_position))
        self.lst2[to_position], self.lst2[from_position] = self.lst2[from_position], self.lst2[to_position]
        self.current_position = to_position
        self.move_count += 1

    def completed(self):
        '''Checking if game is completed'''
        status = False
        if list(self.lst.values()) == self.lst2:
            status = True
        return status

    def start(self):
        '''To start game'''
        print()
        print('*'*30)
        print('PUZZLE 15, Good luck!')
        print('*'*30)
        self.data()
        self.table()


class GameHelp(Puzzle15):

    def data(self):
        '''Solved table example'''
        for num in range(1, 17):
            self.lst[num] = self.beautify(str(num))
        for a, b in self.lst.items():
            if b.strip() == '16':
                self.lst[a] = '  '
                break
        self.lst2 = list(self.lst.values())

    def expl(self):
        '''start help'''
        print()
        print('*'*30 + '\nWelcome to Puzzle 15 game. \n'+'*'*30)
        print('\nBy moving tiles around blank tile you have\nto put together numbers in ascending order.\nAs a picture shown below: ')
        self.data()
        self.table()
        print('You can access in game help by leaving blank and pressing ENTER\nTo quit game just type \'0\'.')
        print('*'*30)
        print()
        input('To start game press \'ENTER\'')


# Start initialization
z = input('To start game press \'ENTER\', for help type \'help\': ')
if z.lower() == 'help':
    gh = GameHelp()
    gh.expl()
game = Puzzle15()
game.start()

# Basic interaction with the player
print('*'*30)
print('HINT: Press enter for help')
print('*'*30)

while True:
    lst = game.movement()
    lst1 = []
    print(f"Possible moves: ", end=' ')
    for i in lst:
        lst1.append(int(i))
        print(i.strip(), end=' ')
    try:
        x = int(input('\nEnter tile number: '))
    except ValueError:
        x = 99
    if x == 0:
        print()
        print('*'*30, '\nBuh-bye')
        print('*'*30)
        break
    elif x == 99:
        print()
        print('*'*30, '\nHELP')
        print('*'*30)
        print('To move tile enter it\'s number:',
              *lst, '\nTo quit game type 0')
        print('*'*30)
        while False:
            x = int(input('Enter tile number: '))
    elif x not in lst1:
        print()
        print('*'*30, '\nInvalid move')
        print('*'*30)
    else:
        game.change(x)
        print(f'\n****** Total moves: {game.move_count} ******')
    game.table()

    if game.completed():
        print('*'*30)
        print('You did it! Congratulations!')
        print(f'Total moves: {game.move_count}')
        print('*'*30)
        again = input("\nWant to play again? (y/n): ")
        if again.lower() == 'n':
            print()
            print('*'*30, '\nBuh-bye')
            print('*'*30)
            break
        game.data()
        game.table()
        game.completed()
