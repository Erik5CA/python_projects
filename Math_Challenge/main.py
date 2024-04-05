import random
import time

OPERATORS = [
    '+', '-', '*'
]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    rigth = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    
    expr = f'{left} {operator} {rigth}'
    answer = eval(expr)
    # print(expr, answer)
    return expr, answer

wrong = 0
input('Press enter to start!')
print('---------------------')
start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input(f'Problem {i + 1}: {expr} = ')
        if guess == str(answer):
            break
        wrong += 1
    
end_time = time.time()
total_time = round(end_time - start_time, 2)
print('---------------------')
print('Great work!')
print(f'You finished in {total_time} seconds!')