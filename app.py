from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Números da Lotofácil
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}

# Preços dos jogos
game_prices = {
    15: 3.00,
    16: 48.00,
    17: 408.00,
    18: 2448.00,
    19: 11628.00,
    20: 46512.00
}

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    chosen_numbers = None
    game_price = None
    game_number = None
    
    if request.method == 'POST':
        try:
            # Pega a quantidade de números selecionada pelo usuário
            game_number = int(request.form['game_number'])

            # Valida o número de jogos
            if game_number < 15 or game_number > 20:
                error = "Escolha um número entre 15 e 20."
            else:
                # Converte o conjunto de números para uma lista
                numbers_list = list(numbers)

                # Sorteia a quantidade de números que o usuário pediu
                chosen_numbers = random.sample(numbers_list, game_number)

                # Recupera o valor do jogo
                game_price = game_prices.get(game_number)

        except ValueError:
            error = "Valor inválido. Por favor, insira um número inteiro entre 15 e 20."
        except Exception as e:
            error = f"Ocorreu um erro inesperado: {e}"

    return render_template('index.html', 
                           error=error, 
                           chosen_numbers=sorted(chosen_numbers) if chosen_numbers else None, 
                           game_price=game_price,
                           game_number=game_number,
                           game_prices=game_prices)

if __name__ == '__main__':
    app.run(debug=True)
