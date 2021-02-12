from models.calcular import Calcular

def main() -> None:
    pontos: int = 0
    jogar(pontos)

def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Escolha o seu nível de dificuldada (1, 2, 3 ou 4): '))
    
    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operação: ')
    calc.mostrar_operacao()

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print('Parabêns! Você acertou, agora tem {pontos} ponto(s).')
    
    continuar: int = int(input('Deseja continuar jogando? [1 - Sim, 0 - Não]: '))

    if continuar:
        jogar(pontos)
    else:
        print(f'Você finalizou o jogo com {pontos} ponto(s).')
        print(f'Tchau!')

if __name__=='__main__':
    main()