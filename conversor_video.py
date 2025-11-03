from moviepy import VideoFileClip

VERSAO_ATUAL = '0.1.0'

print('Bem Vindo ao Conversor de Video')
print(f'Versão {VERSAO_ATUAL}')

def converter_mov_to_mp4(input_file,output_file):
    try:
        videos = VideoFileClip(input_file)

        videos.write_videofile(output_file, codec='libx264', audio_codec='aac')
        videos.close()

        print('Conversão realizada com sucesso')
    except Exception as e:
        print(f'Erro ao converter arquivo: {e}')
    
if __name__ == '__main__':
    input_file = input('Caminho do Arquivo: ')
    output_file = input('Caminho de Saida do arquivo: ')
    converter_mov_to_mp4(input_file,output_file)