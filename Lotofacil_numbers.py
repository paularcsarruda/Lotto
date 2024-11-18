import random

# lotofácil numbers
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}

# game prices
game_prices = {
    15: 3.00,
    16: 48.00,
    17: 408.00,
    18: 2448.00,
    19: 11628.00,
    20: 46512.00
}

while True:
    
    while True:
        try:
            game_number = int(input("Quantos números você quer jogar? (Entre 15 e 20) "))
            if game_number >= 15 and game_number <= 20:
                break
            else:
                print("Por favor, escolha um número entre 15 e 20.")
        except ValueError:
            print("Por favor, insira um número válido.")
    
    
    numbers_list = list(numbers)
    chosen_numbers = random.sample(numbers_list, game_number)

    print(f"Seus números sorteados são: {sorted(chosen_numbers)}")

    if game_number in game_prices:
        print(f"O valor para um jogo de {game_number} números é: R${game_prices[game_number]:.2f}")
    else:
        print("Erro: Valor não encontrado para o número de jogos escolhido.")

    continuar = input("Você quer fazer outro jogo? (sim/nao) ").strip().lower()
    
    if continuar != 'sim':
        print("Boa sorte! Até a próxima!")
        break
