import yt_dlp


def download_video(link, directory):
    try:
        ydl_opts = {
            'format': 'best[ext=mp4]',
            'outtmpl': directory + '/%(title)s.%(ext)s'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
            return True

    except Exception as e:
        print(f"Error al descargar el video: {str(e)}")
        return False
