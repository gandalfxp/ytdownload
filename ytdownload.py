from pytube import Playlist, YouTube
import os

def trim(string: str, max_len: int) -> str:
    '''
    Trims a string to a specific length and replaces the last three characters
    with "...". If the string is shorter than the maximum length, it will not be
    manipulated.
    '''

    if len(string) <= max_len:
        return string
    return f'{string[:max_len - 3]}...'

def create_directory(name: str) -> str:
    '''
    Tries to create a directory inside of the working directory. If a directory
    with this name already exists or the name contains invalid characters, the
    user can interactively change the name of the directory.

    If the name did not change, it will be returned as it has been parsed.
    If the name did change, the returned name will differ from the parsed one.
    '''

    while True:
        try:
            os.mkdir(f'./{name}')
            break
        except FileExistsError:
            msg = f'A directory called "./{name}" already exists. Try another name: '
            name = input(msg)
        except OSError:
            msg = f'The directory "./{name}" contains invalid characters. Try another name: '
            name = input(msg)
    
    return f'./{name}'

def download(url: str, dir: str) -> None:
    '''
    Downloads a song as FFMPEG3 and tries to save it in the parsed directory
    with its original title. If a file with this name already exists, it will be
    overwritten. If the title contains invalid characters, the user can
    interactively change the title.
    '''

    song = YouTube(url)
    name = f'{song.title}.mp3'

    while True:
        try:
            with open(f'{dir}/{name}', 'w') as f:
                f.close()
            break
        except OSError:
            msg = f'The filename "{name}" contains invalid characters. Try another name (including the .mp3 suffix): '
            name = input(msg)
    
    song.streams.get_audio_only().download(dir, name)

LOGO = '''
       _      _                     _                 _ 
 _   _| |_ __| | _____      ___ __ | | ___   __ _  __| |
| | | | __/ _` |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |
| |_| | || (_| | (_) \ V  V /| | | | | (_) | (_| | (_| |
 \__, |\__\__,_|\___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|
 |___/                                     by Theo Hoppe

'''


if __name__ == '__main__':
    print(LOGO)


    link = 'https://www.youtube.com/watch?v=tsmPCi7'

    while True:
        try:
            playlist = Playlist(link)
            directory = create_directory(playlist.title)
            break
        except:
            msg = f'Cannot access the link to the playlist. Try another link: '
            link = input(msg)

    for url in playlist.video_urls:
        download(url, directory)
