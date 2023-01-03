from pytube import YouTube
from os import system


class App:
    def __init__(self) -> None:
        pass


    def askForURL(self) -> str:
        return input("Enter video's URL: ")

    
    def setURL(self, url: str) -> None:
        self.url = url


    def initializeYT(self) -> None:
        self.yt = YouTube(self.url)


    def displayVideoDetails(self) -> None:
        print(f'\nTITLE: {self.yt.title}')
        print(f'AUTHOR: {self.yt.author}')
        print(f'VIEWS: {self.yt.views}')
        print(f'LENGTH: {self.yt.length} seconds')


    def askForAction(self) -> str:
        print('\n1. Download')
        print('2. Cancel')

        return input('')


    def askForQuality(self) -> str:
        return input('\nSelect quality (144p 360p 480p 720p 1080p): ')


    def askForName(self) -> str:
        return input('Enter video name: ')


    def askForPath(self) -> str:
        return input('Enter output path (optional): ')


    def download(self, quality: str, path: str = './', name: str = '') -> None:
        if not name:
            name = f'{self.yt.title}.mp4'

        print('\nDOWNLOADING...')
        self.yt.streams.get_by_resolution(quality).download(filename=name, output_path=path)

        self.clear()
        print('...DOWNLOADED')

        exit(0)


    def clear(self) -> None:
        system('clear')