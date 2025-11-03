from moviepy import VideoFileClip

VERSAO_ATUAL = '0.2.0'

print('Bem Vindo ao Conversor de Video')
print(f'Versão {VERSAO_ATUAL}')

menu = '''
----Selecione o formato de saida----

1 - mp4
2 - avi 
3 - mov
4 - mkv
5 - webm
6 - gif
7 - mp3
8 - wav
9 - acc
10 - ogg
              
0 - Finalizar

------------------------------------
'''

def converter_mov_to_mp4(input_file):
    try:
        print(input_file)
        input_format = str(input_file).split('.')[-1]

        option = input(menu)

        match option:
            case '1':
                new_format = 'mp4'
            case '2':
                new_format = 'avi'
            case '3':
                new_format = 'mov'
            case '4':
                new_format = 'mkv'
            case '5':
                new_format = 'webm'
            case '6':
                new_format = 'gif'
            case '7':
                new_format = 'mp3'
            case '8':
                new_format = 'wav'
            case '9':
                new_format = 'acc'
            case '10':
                new_format = 'ogg'
            case _:
                print('opcao invalida')

        output_file = str(input_file).replace(f'.{input_format}',f'.{new_format}')               
        videos = VideoFileClip(input_file)

        videos.write_videofile(f'output_movies/{output_file}', codec='libx264', audio_codec='aac')
        videos.close()

        print('Conversão realizada com sucesso')
    except Exception as e:
        print(f'Erro ao converter arquivo: {e}')
    
if __name__ == '__main__':
    input_file = input('Caminho do Arquivo: ')
    converter_mov_to_mp4(input_file)