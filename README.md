# Download Playlists from YouTube

Download your favorite songs from YouTube! YTdownload is meant to be
minimalistic and easy-to-use, so why don't you give it a try?

<p align="center">
  <img src="https://i.postimg.cc/MGSWTmVq/ytdownload.png"/>
</p>

## Usage

The command structure looks like this:  

```ytdownload.py [LINK]```

After you hit enter, the script will create a folder in the working directory. 
After that, it will start to download every video as MP3-File.

The folder and the songs it contains are named after their respective titles on
YouTube. Sometimes, it occurs that a title on YouTube contains characters that 
are invalid in file- or directory-names. Therefor you can interactively correct
them at runtime.

## Dependencies

The following dependencies have to be installed manually:
- pytube 15.0.0

All the other dependencies should come bundled with python3.