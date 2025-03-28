import yt_dlp
import os

# Diretório onde deseja salvar os arquivos (definido diretamente no código)
diretorio = "C:/Users/User/Documents/American Truck Simulator/music"  # Altere este caminho para o diretório desejado

# Verifica se o diretório existe, caso contrário, cria
if not os.path.exists(diretorio):
    print(f"O diretório '{diretorio}' não existe. Criando o diretório...")
    os.makedirs(diretorio)

# Função para baixar áudio
def baixar_audio(url, playlist=False):
    ydl_opts = {
        'format': 'bestaudio/best',  # Melhor qualidade de áudio disponível
        'outtmpl': os.path.join(diretorio, '%(title)s.%(ext)s'),  # Salva o arquivo no diretório especificado com o nome do vídeo
        'noplaylist': not playlist,  # Garante que a playlist inteira será baixada se for uma playlist
        'postprocessors': [{  # Adicionar um pós-processador para converter para MP3
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Convertendo para MP3
            'preferredquality': '192',  # Qualidade do MP3
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except yt_dlp.utils.DownloadError as e:
            print(f"Erro ao baixar {url}: {e}")
            print("Continuando com o próximo...")

# Função para baixar vídeo
def baixar_video(url, playlist=False):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Melhor qualidade de vídeo e áudio disponível
        'outtmpl': os.path.join(diretorio, '%(title)s.%(ext)s'),  # Salva o arquivo no diretório especificado com o nome do vídeo
        'noplaylist': not playlist,  # Garante que a playlist inteira será baixada se for uma playlist
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except yt_dlp.utils.DownloadError as e:
            print(f"Erro ao baixar {url}: {e}")
            print("Continuando com o próximo...")

# Continuar pedindo o link

if __name__ == '__main__':
    print("Plataformas suportadas: YouTube, Instagram, Facebook, Twitter, TikTok, Vimeo, Dailymotion, SoundCloud, Mixcloud, Bandcamp, Twitch, Streamable, Bitchute, Coub, Rumble, Wistia, Vlive, Brightcove, Kaltura, Odysee, The Internet Archive, and many more, basta ter as URLS.")
    print("Com grande poder vem grande responsabilidades!!!")
    print("REGRAS!!: 1- Tenha controle de como você usa esse script 2- Não será possível baixar playlists privadas, apenas deixe-as públicas.")
    while True:
        continuar = input("Deseja baixar outro vídeo? (s/n): ")
        if continuar.lower() == "n":
            break
        url = input("Digite o link do vídeo ou playlist: ")
        tipo_download = input("Deseja baixar o áudio ou o vídeo? (a/v): ")
        playlist = input("É uma playlist? (s/n): ").lower() == 's'
        if tipo_download.lower() == 'a':
            baixar_audio(url, playlist)
        elif tipo_download.lower() == 'v':
            baixar_video(url, playlist)
        else:
            print("Opção inválida. Tente novamente.")

    print("Download concluído!")