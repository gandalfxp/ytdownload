from os import mkdir
from pytube import Playlist, YouTube

def on_progress(stream, chunk: bytes, bytes_remaining: int) -> None:
    bytes_downloaded = stream.filesize - bytes_remaining
    progress = 100 / stream.filesize * bytes_downloaded
    print(f'⬇️ [{progress}%] {stream.title}', end='\r')

def on_complete(stream, filepath: str) -> None:
    print(f'✅ {stream.title}')

if __name__ == '__main__':
    url = 'https://www.youtube.com/playlist?list=PLOzDu-MXXLlgKMA3S2FXY_XVyDrukc0si'
    playlist = Playlist(url)
    output_path = f'./{playlist.title}'

    mkdir(output_path)

    for url in playlist.video_urls:
        video = YouTube(url)
        video.register_on_progress_callback(on_progress)
        video.register_on_complete_callback(on_complete)
        video.streams.get_audio_only().download(output_path)