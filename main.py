import conversor_video as video

VERSAO_ATUAL = '0.2.1'

print('Bem Vindo ao Conversor de Video')
print(f'V.: {VERSAO_ATUAL}')

menu = '''
1 - Converter Videos
0 - Sair

>: '''

if __name__ == '__main__':
    try:
        option = '1'
        while option != '0':
            option = input(menu)
            match option:
                case '1':
                    movie = input('Caminho do seu video: ')
                    video.converter_mov_to_mp4(movie)
                case '0':
                    print('Finalizando Sessão')
    except KeyboardInterrupt:
        print('Finalizado Pelo Usuario')