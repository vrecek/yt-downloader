from pytube import exceptions
from App import App



if __name__ == '__main__':
    APP = App()
    APP.clear()

    while True:
        try:
            url = APP.askForURL()
            APP.setURL(url)
            APP.initializeYT()

        except exceptions.RegexMatchError:
            APP.clear()
            print('Incorrect URL\n')

            continue


        APP.displayVideoDetails()
        action = APP.askForAction()

        match action:
            case '1':
                quality = APP.askForQuality()
                name = APP.askForName()
                path = APP.askForPath()

                try:
                    APP.download(quality, path, name)

                except AttributeError:
                    APP.clear()
                    print('Incorrect quality\n')
                    

            case '2':
                APP.clear()

            case _:
                APP.clear()
                print('Incorrect option\n')