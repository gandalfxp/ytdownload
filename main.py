from pytube import Playlist

uri = 'https://www.youtube.com/playlist?list=PLOzDu-MXXLlgKMA3S2FXY_XVyDrukc0si'

playlist = Playlist(uri)

print(playlist.video_urls)