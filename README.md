<h1 align="center">TikTok-Autobot</h1>

<p align="center"><i><b>A bot that trys to mimic a human using TikTok</b></i></p>



## Table of Contents
- [Installation](##installation)
  - [Requirements](###requirements)
  - [Getting the Cookie file](###getting-the-Cookie-file)
  - [Starting the Bot](###Starting-the-Bot)
- [Contributing & Ways to improve](##Contributing-&-Ways-to-improve)
- [Developers and maintainers](##CDevelopers-and-maintainers)
- 

## Installation

### Requirements
- A perquisite to using this program is the installation of a [Selenium-compatible](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/) web browser. [Google Chrome](https://www.google.com/chrome/) is recommended.
- Install [__*Python 3.10*__](https://www.python.org/downloads/release/python-3100/) and delete every other version installt on your Computer.
- Install [🍪 Get cookies.txt](https://github.com/kairi003/Get-cookies.txt-LOCALLY) as an browser extension, to get cookies in a [NetScape cookies format](http://fileformats.archiveteam.org/wiki/Netscape_cookies.txt).

### Getting the Cookie file
- Go on [TikTok.com](https://tiktok.com/) 
- Open the  `🍪 Get cookies.txt` extension
- Select `Export⇩`

### Starting the Bot
1. Clone this repository
2. Run `pip install -r requirements.txt`
3. Run `python -m playwright install` and `python -m playwright install-deps`
4. Open the `conf.toml` file
  - Fill out the `min` and `max` key with the time the Bot should wait minimum/maximum befor uploading the next video(time in seconds => 1h = 3600s)
  - Give the tags __every__ video should get in the `tags` key(Format: tags = "#Reddit#AskReddit")
  - Place the downloaded cookie file in the folder and give it the name `www.tiktok.com_cookies.txt` __or__ change the path to where your file is placed
5. Visit [the Reddit Apps page.](https://www.reddit.com/prefs/apps), and set up an app that is a "script". Paste any URL in redirect URL. Ex:google.com
6. Run `python videocreator.py` or `python3 videocreator.py` once, the Bot will help you to set it up to your likings
7. Run `python main.py` or `python3 main.py` and the Bot will start working right away

 
__❗Note❗__
1. If you got an error installing or running the bot try first rerunning the command with a three after the name e.g. python3 or pip3
2. You can find your *TikTok sessionid* in the downloaded cookie file
3. If you need to reconfigure the bot, simply open the `config.toml` file and delete the lines that need to be changed. Then repeat steps '6.' and '7.'and it will help you reconfigure those options.
4. Currently the Bot can only create and upload videos by itself, but will be improved in the near future, so it will function like a human is using TikTok


## Contributing & Ways to improve
Feel Free to Contribute and improve the Bot, certain goals of the Bot will follow soon

## Developers and maintainers
leon-wm - https://github.com/leon-wm (Owner)

## Links
- Huge thanks to [Lewis Menelaws](https://github.com/elebumm) for the creatin of the [Reddit Video Maker Bot](https://github.com/elebumm/RedditVideoMakerBot)
- Huge tanks to [William Kaiser](https://github.com/wkaisertexas) for the creation of the [tiktok-uploader](https://github.com/wkaisertexas/tiktok-uploader)
