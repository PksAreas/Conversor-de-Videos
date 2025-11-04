from moviepy import VideoFileClip

VERSAO_ATUAL = '0.2.1'

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
                newcodec = 'libx264'
            case '2':
                new_format = 'avi'
                newcodec = 'libx264'
            case '3':
                new_format = 'mov'
                newcodec = 'libx264'
            case '4':
                new_format = 'mkv'
                newcodec = 'libx264'
            case '5':
                new_format = 'webm'
                newcodec = 'libvpx'
                audiocodec = 'libvorbis'
            case '6':
                new_format = 'gif'
                newcodec = 'libx264'
            case _:
                print('opcao invalida')

        output_file = str(input_file).replace(f'.{input_format}',f'.{new_format}')               
        videos = VideoFileClip(input_file)

        videos.write_videofile(f'output_movies/{output_file}', codec=newcodec, audio_codec=audiocodec)
        videos.close()

        print('Conversão realizada com sucesso')
    except Exception as e:
        print(f'Erro ao converter arquivo: {e}')
    
if __name__ == '__main__':
    input_file = input('Caminho do Arquivo: ')
    converter_mov_to_mp4(input_file)