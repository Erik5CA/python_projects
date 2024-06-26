
import random 

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbols_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += bet * values[symbol]
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols: dict):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] # Copy the list of symbols
        for _ in range(rows):
            symbol = random.choice(current_symbols)
            current_symbols.remove(symbol)
            column.append(symbol)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=' | ')
            else:
                print(column[row], end= '')
        print()
    

def deposit():
    while True:
        amount = input('What would you like to deposit? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than zero.')
        else:
            print('Amount must be a number.')
    return amount

def get_number_of_lines(balance):
    while True:
        lines = input(f'Enter the number of lines to bet on (1-{MAX_LINES})? ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                if lines > balance:
                    print(f"Your balance is: ${balance}.\nThe minimum bet for each line is: ${MIN_BET}.\nYou dont have enough money to bet in {lines} lines.")
                else:
                    break
            else:
                print('Enter a valid number of lines.')
        else:
            print('Please enter a number.')
    return lines
    
def get_bet():
    while True:
        bet = input('What would you like to bet on each line? $')
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f'Amount must be between ${MIN_BET} - ${MAX_BET}.')
        else:
            print('Please enter a number.')
    return bet


def spin(balance):
    lines = get_number_of_lines(balance)
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f'You do not have enough to bet that amount, your current balance is: ${balance}.')
        else:
            break
        
    print(f'You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}.')
    
    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot_machine(slots)
    winnigs, winnig_lines = check_winnings(slots, lines, bet, symbols_value)
    print(f'You won ${winnigs}.')
    print('You won on lines: ', *winnig_lines)
    return winnigs - total_bet

def main(): 
    balance = deposit()
    while True:
        if balance == 0:
            answer =  input(f'Your balance is: ${balance}, you want deposit more money?, enter to Yes (q to quit).')
            if answer == 'q':
                break
            else:
                balance = deposit()
        print(f'Current balance is ${balance}.')
        answer = input('Press enter to play (q to quit).')
        if answer == 'q':
            break
        balance += spin(balance)
    print(f'You left with: ${balance} ')
    
main()