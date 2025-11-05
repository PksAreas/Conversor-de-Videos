from moviepy import VideoFileClip

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

        videos = VideoFileClip(input_file)
        match option:
            case '1':
                new_format = 'mp4'
                newcodec = 'libx264'
                audiocodec = 'libvorbis'
            case '2':
                new_format = 'avi'
                newcodec = 'libx264'
                audiocodec = 'libvorbis'
            case '3':
                new_format = 'mov'
                newcodec = 'libx264'
                audiocodec = 'libvorbis'
            case '4':
                new_format = 'mkv'
                newcodec = 'libx264'
                audiocodec = 'libvorbis'
                
            case '5':
                new_format = 'webm'
                newcodec = 'libvpx'
                audiocodec = 'libvorbis'
            case '6':
                print('Convertendo Video...')
                output_file = str(input_file).replace(f'.{input_format}',f'.gif')               
                videos.write_gif(f'output_movies/{output_file}')
                videos.close()
            case _:
                print('opcao invalida')

        if option != '6':
            output_file = str(input_file).replace(f'.{input_format}',f'.{new_format}')               
            videos.write_videofile(f'output_movies/{output_file}', codec=newcodec, audio_codec=audiocodec)
            videos.close()

        print('Conversão realizada com sucesso')
    except Exception as e:
        print(f'Erro ao converter arquivo: {e}')
