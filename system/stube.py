import subprocess
import yt_dlp

def run(*args):
    query = " ".join(str(arg) for arg in args)
    if not query:
        print("Por favor, ingresa búsqueda o URL de YouTube")
        return

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'noplaylist': False,
        'extract_flat': False,
        'geo_bypass': True,
        'nocheckcertificate': True,
        'cachedir': False,
        'extractor_args': {
            'youtube': {
                'player_client': ['android', 'web']
            }
        },
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'
        }
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            if query.startswith(("http://", "https://")):
                info = ydl.extract_info(query, download=False)
            else:
                info = ydl.extract_info(f"ytsearch20:{query}", download=False)
            if 'entries' in info:
                videos = info['entries']
            else:
                videos = [info]
            if not videos:
                print("No se encontraron resultados!!!")
                return
            audio_urls = []
            titles = []
            for video in videos:
                if 'url' in video:
                    audio_urls.append(video['url'])
                    titles.append(video.get('title', 'Desconocido'))
            if not audio_urls:
                print("No se pudieron extraer URLs de audio")
                return
            print("Reproduciendo continuamente:")
            for title in titles:
                print(f"- {title}")
            subprocess.Popen(['mpv', '--no-video', '--loop-playlist=inf'] + audio_urls,
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    except Exception as e:
        print(f"Error al reproducir: {e}")