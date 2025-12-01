import random

# Lista de palavras secretas
palavras = ['python', 'programacao', 'desenvolvimento', 'computador', 'algoritmo', 'logica']

def escolher_palavra():
    """Escolhe uma palavra aleatória da lista."""
    return random.choice(palavras).upper()

def inicializar_jogo():
    """Configura o estado inicial do jogo."""
    palavra_secreta = escolher_palavra()
    letras_certas = ['_' for letra in palavra_secreta]
    letras_erradas = []
    tentativas_max = 6
    return palavra_secreta, letras_certas, letras_erradas, tentativas_max

def desenhar_forca(erros):
    """Desenha a forca no terminal de acordo com o número de erros."""
    estagios = [
        # 0 erros
        """
          +---+
          |   |
              |
              |
              |
              |
        =========
        """,
        # 1 erro
        """
          +---+
          |   |
          O   |
              |
              |
              |
        =========
        """,
        # 2 erros
        """
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========
        """,
        # 3 erros
        """
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========
        """,
        # 4 erros
        """
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        =========
        """,
        # 5 erros
        """
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        =========
        """,
        # 6 erros
        """
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        =========
        """
    ]
    print(estagios[erros])
    

def jogar():
    """Função principal que roda o loop do jogo."""
    palavra_secreta, letras_certas, letras_erradas, tentativas_max = inicializar_jogo()
    
    print("Bem-vindo(a) ao Jogo da Forca!")
    
    while True:
        erros = len(letras_erradas)
        desenhar_forca(erros)
        
        print("\nPalavra:", ' '.join(letras_certas))
        print(f"Erros ({erros}/{tentativas_max}):", ', '.join(letras_erradas))
        
        # --- Condições de Fim de Jogo ---
        if erros == tentativas_max:
            print("\n🚨 Você foi enforcado(a)! Fim de jogo.")
            print(f"A palavra secreta era: **{palavra_secreta}**")
            break
        
        if '_' not in letras_certas:
            print("\n🎉 Parabéns! Você acertou a palavra!")
            print(f"A palavra secreta é: **{palavra_secreta}**")
            break
        
        # --- Solicita a entrada do jogador ---
        chute = input("\nDigite uma letra (ou tente adivinhar a palavra): ").strip().upper()

        # Verifica se o chute é uma tentativa de palavra
        if len(chute) > 1:
            if chute == palavra_secreta:
                # Acertou a palavra inteira
                print("\n🎉 Parabéns! Você acertou a palavra!")
                print(f"A palavra secreta é: **{palavra_secreta}**")
                break
            else:
                # Errou a palavra inteira, conta como um erro
                print("❌ Palavra incorreta! Tente novamente.")
                if chute not in letras_erradas: # Adiciona o erro se for diferente
                    letras_erradas.append(chute)
                continue
        
        # Verifica se o chute é uma única letra
        if not chute.isalpha() or len(chute) != 1:
            print("Entrada inválida. Digite apenas uma letra ou a palavra completa.")
            continue
            
        # Verifica se a letra já foi tentada
        if chute in letras_erradas or chute in letras_certas:
            print(f"Você já tentou a letra **{chute}**. Tente outra.")
            continue

        # --- Processa o chute da letra ---
        if chute in palavra_secreta:
            print(f"✅ Boa! A letra **{chute}** está na palavra.")
            # Atualiza as letras certas
            for i, letra_palavra in enumerate(palavra_secreta):
                if letra_palavra == chute:
                    letras_certas[i] = chute
        else:
            print(f"❌ Que pena, a letra **{chute}** não está na palavra.")
            letras_erradas.append(chute)
        
        print("-" * 30)

if __name__ == '__main__':
    jogar()
