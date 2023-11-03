import random
MAX_LINE = 3

MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLM = 3

symbols_count = {"A": 2, "B": 4, "C": 6, "D": 8} # This is appearance of the symbol, less value less it will appear!

symbols_value = {"A": 20, "B": 10, "C": 5, "D": 3} # The values of respective symbol will get multiply to the bet if you won!


def deposit(): # 1. Deposit the initial amount to play the slot game.
    while True:
        amount = input('Deposit your amount: $ ')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('please enter amount greater than 0.')
        else:
            print('Please input a number!')        
    return amount        

def get_lines_num(): # 2. Tell on how many lines you want to bet(1-3)
    while True:
        line = input("Enter the number of lines to bet on (1-" + str(MAX_LINE) + ")? ")
        if line.isdigit():
            line = int(line)
            if 1 <= line <= MAX_LINE:
                break
            else:
                print('Please enter amount greater than 0.')
        else:
            print('Please input a number!')        
    return line

def get_bet(): # 3. How much you want to bet on each line
    while True:
        amount = input('what amount on each line: $ ')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'please bet between {MIN_BET}$ to {MAX_BET}$.')
        else:
            print('Please input a number!')        
    return amount

def get_slot(rows, colo, symbols): # 4. Defining the values in the slot machine. It will returns Colomns[[], [], []]
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)
     
    colomns = []  
    for _ in range(colo):
        colomn = []
        current_symbols = all_symbols[:]
        for _ in range(rows): 
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            colomn.append(value)
            
        colomns.append(colomn)
    
    return colomns

def print_get_slot(colomns): # 5. Printing the actual slot machine and showing the value inside the Columns
    for row in range(len(colomns[0])):
        for i, column in enumerate(colomns):
            if i != len(colomns) - 1:
                print(column[row], end = ' | ')
            else:
                print(column[row], end = '')
        print()

def check_winnings(colomns, lines, bet, values): # 6. It will return how much you win and on which line/lines.
    winnings = 0
    winning_line = []
    for line in range(lines):
        symbol = colomns[0][line]
        for colom in colomns:
            symbol_to_check = colom[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_line.append(line+1)
    return winnings, winning_line

def game(balance): # 7. This method will call all the method mention above and run one game and return the 
    # winnings - total_bet. For continuing the game the main() method comes!
    line = get_lines_num()
    while True:
        bet = get_bet()
        total_bet = line * bet
        if total_bet > balance:
            print(f"You have inefficient amount to bet! Your current amount is {balance}$.")
        else:
            break
    print(f"You are betting {bet} on {line} lines which is equal to {total_bet}$.")
    
    slots = get_slot(ROWS, COLM, symbols_count)
    print_get_slot(slots)
    winnings, winning_line = check_winnings(slots, line, bet, symbols_value)
    print(f'You won $ {winnings}.')
    print(f"You won on the line: ", *winning_line)
    
    return winnings - total_bet
    

def main(): # This method will continue looping untill you want to quit, it will tell you the balance after the game session!
    balance = deposit()
    while True:
        print(f"Your current balance is ${balance}")
        spin = input('Enter to play again or press (q) to quit!').lower()
        if spin == 'q':
            break
        balance += game(balance)
    print(f'You left with ${balance}')
   

main()