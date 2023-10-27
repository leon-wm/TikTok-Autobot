#!/usr/bin/env python
import math
import sys
from os import name
from pathlib import Path
from subprocess import Popen
from typing import NoReturn

from prawcore import ResponseException
from utils.console import print_substep
from reddit.subreddit import get_subreddit_threads
from utils import settings
from utils.cleanup import cleanup
from utils.console import print_markdown, print_step
from utils.id import id
from utils.version import checkversion
from video_creation.background import (
    download_background_video,
    download_background_audio,
    chop_background,
    get_background_config,
)
from video_creation.final_video import make_final_video
from video_creation.screenshot_downloader import get_screenshots_of_reddit_posts
from video_creation.voices import save_text_to_mp3
from utils.ffmpeg_install import ffmpeg_install



#+++

from tiktok_uploader.upload import upload_video
from random import randint
from time import sleep
import os
from datetime import timedelta
from datetime import datetime
from utils import settings
import time
import toml


while True: #Makes the bot run endless

    print(
        """
    ██████╗ ███████╗██████╗ ██████╗ ██╗████████╗    ████████╗██╗██╗  ██╗████████╗ ██████╗ ██╗  ██╗    ██████╗  ██████╗ ████████╗
    ██╔══██╗██╔════╝██╔══██╗██╔══██╗██║╚══██╔══╝    ╚══██╔══╝██║██║ ██╔╝╚══██╔══╝██╔═══██╗██║ ██╔╝    ██╔══██╗██╔═══██╗╚══██╔══╝
    ██████╔╝█████╗  ██║  ██║██║  ██║██║   ██║          ██║   ██║█████╔╝    ██║   ██║   ██║█████╔╝     ██████╔╝██║   ██║   ██║
    ██╔══██╗██╔══╝  ██║  ██║██║  ██║██║   ██║          ██║   ██║██╔═██╗    ██║   ██║   ██║██╔═██╗     ██╔══██╗██║   ██║   ██║
    ██║  ██║███████╗██████╔╝██████╔╝██║   ██║          ██║   ██║██║  ██╗   ██║   ╚██████╔╝██║  ██╗    ██████╔╝╚██████╔╝   ██║
    ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═════╝ ╚═╝   ╚═╝          ╚═╝   ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝    ╚═════╝  ╚═════╝    ╚═╝
        """
    )

    try:
        open('config.toml', 'r')
    except:
        print("Please first run 'videocreator.py' once first!")
        exit()
    
    with open('conf.toml', 'r') as cf2to:
        confTo = toml.load(cf2to)    
    
    with open('config.toml', 'r') as f:
        confToml = toml.load(f)
    

    directory = Path().absolute() #gets the current Path
    try:
        sub = confToml["reddit"]["thread"]["subreddit"]
    except:
        print("Please first run 'videocreator.py' once first!")
        exit()

    try:
        path = f"{directory}/results/{sub}/" #gets the Path with the finished videos
    except:
        print("Please first run 'videocreator.py' once first!")
        exit()

    folder_walk = os.walk(path) #lists the files in the results directory
    
    try:
        firstFileInFolder = next(folder_walk)[2][0] #gets the first file in the directory
    except:
        print("Please first run 'videocreator.py' once first!")
        exit()
    
    print("The uploaded Video will be: " + firstFileInFolder + "\n")

    video = path + firstFileInFolder #gets the spesific path to the video that will be uploaded

    tagList = confTo["settings"]["upload"]["tags"].split("#")

    description1 = firstFileInFolder.rstrip(".mp4") + " " + " ".join(tagList) #creates the description with the Video name and the tags from the config.yaml

    print("The description will be: " + description1 + "\n")

        

    upload_video(f"{video}", description=description1, cookies=confTo["settings"]["upload"]["pathToCookies"]) #uploads the Video settings.config["settings"]["pathToCookies"]

    try: #trys to create the folder for the used Videos 
        os.mkdir(f"{directory}/results/used/")
        print(f"Directory {directory}/results/used/ was created successful \n")
    except OSError as error:  
        print(f"Directory {directory}/results/used/ allready exists \n") 

    os.rename(f"{video}", f"{directory}/results/used/{firstFileInFolder}") #moves the used Video in the used directory
    print(f"The used video {firstFileInFolder} was moved to {directory}/results/used/ \n")
        
    print("No Video found! starting the video creation.")

    #---



    __VERSION__ = "3.2.1"

    print(
        """
    ██████╗ ███████╗██████╗ ██████╗ ██╗████████╗    ██╗   ██╗██╗██████╗ ███████╗ ██████╗     ███╗   ███╗ █████╗ ██╗  ██╗███████╗██████╗
    ██╔══██╗██╔════╝██╔══██╗██╔══██╗██║╚══██╔══╝    ██║   ██║██║██╔══██╗██╔════╝██╔═══██╗    ████╗ ████║██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
    ██████╔╝█████╗  ██║  ██║██║  ██║██║   ██║       ██║   ██║██║██║  ██║█████╗  ██║   ██║    ██╔████╔██║███████║█████╔╝ █████╗  ██████╔╝
    ██╔══██╗██╔══╝  ██║  ██║██║  ██║██║   ██║       ╚██╗ ██╔╝██║██║  ██║██╔══╝  ██║   ██║    ██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗
    ██║  ██║███████╗██████╔╝██████╔╝██║   ██║        ╚████╔╝ ██║██████╔╝███████╗╚██████╔╝    ██║ ╚═╝ ██║██║  ██║██║  ██╗███████╗██║  ██║
    ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═════╝ ╚═╝   ╚═╝         ╚═══╝  ╚═╝╚═════╝ ╚══════╝ ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
    """
    )
    # Modified by JasonLovesDoggo
    print_markdown(
        "### Thanks for using this tool! Feel free to contribute to this project on GitHub! If you have any questions, feel free to join my Discord server or submit a GitHub issue. You can find solutions to many common problems in the documentation: https://reddit-video-maker-bot.netlify.app/"
    )
    checkversion(__VERSION__)


    def main(POST_ID=None) -> None:
        global redditid, reddit_object
        reddit_object = get_subreddit_threads(POST_ID)
        redditid = id(reddit_object)
        length, number_of_comments = save_text_to_mp3(reddit_object)
        length = math.ceil(length)
        get_screenshots_of_reddit_posts(reddit_object, number_of_comments)
        bg_config = {
            "video": get_background_config("video"),
            "audio": get_background_config("audio"),
        }
        download_background_video(bg_config["video"])
        download_background_audio(bg_config["audio"])
        chop_background(bg_config, length, reddit_object)
        make_final_video(number_of_comments, length, reddit_object, bg_config)


    def run_many(times) -> None:
        for x in range(1, times + 1):
            print_step(
                f'on the {x}{("th", "st", "nd", "rd", "th", "th", "th", "th", "th", "th")[x % 10]} iteration of {times}'
            )  # correct 1st 2nd 3rd 4th 5th....
            main()
            Popen("cls" if name == "nt" else "clear", shell=True).wait()


    def shutdown() -> NoReturn:
        if "redditid" in globals():
            print_markdown("## Clearing temp files")
            cleanup(redditid)

        print("Exiting...")
        sys.exit()


    if __name__ == "__main__":
        if sys.version_info.major != 3 or sys.version_info.minor != 10:
            print(
                "Hey! Congratulations, you've made it so far (which is pretty rare with no Python 3.10). Unfortunately, this program only works on Python 3.10. Please install Python 3.10 and try again."
            )
            sys.exit()
        ffmpeg_install()
        directory = Path().absolute()
        config = settings.check_toml(
            f"{directory}/utils/.config.template.toml", f"{directory}/config.toml"
        )
        config is False and sys.exit()

        if (
            not settings.config["settings"]["tts"]["tiktok_sessionid"]
            or settings.config["settings"]["tts"]["tiktok_sessionid"] == ""
        ) and config["settings"]["tts"]["voice_choice"] == "tiktok":
            print_substep(
                "TikTok voice requires a sessionid! Check our documentation on how to obtain one.",
                "bold red",
            )
            sys.exit()
        try:
            if config["reddit"]["thread"]["post_id"]:
                for index, post_id in enumerate(config["reddit"]["thread"]["post_id"].split("+")):
                    index += 1
                    print_step(
                        f'on the {index}{("st" if index % 10 == 1 else ("nd" if index % 10 == 2 else ("rd" if index % 10 == 3 else "th")))} post of {len(config["reddit"]["thread"]["post_id"].split("+"))}'
                    )
                    main(post_id)
                    Popen("cls" if name == "nt" else "clear", shell=True).wait()
            elif config["settings"]["times_to_run"]:
                run_many(config["settings"]["times_to_run"])
            else:
                main()
        except KeyboardInterrupt:
            shutdown()
        except ResponseException:
            print_markdown("## Invalid credentials")
            print_markdown("Please check your credentials in the config.toml file")
            shutdown()
        except Exception as err:
            config["settings"]["tts"]["tiktok_sessionid"] = "REDACTED"
            config["settings"]["tts"]["elevenlabs_api_key"] = "REDACTED"
            print_step(
                f"Sorry, something went wrong with this version! Try again, and feel free to report this issue at GitHub or the Discord community.\n"
                f"Version: {__VERSION__} \n"
                f"Error: {err} \n"
                f'Config: {config["settings"]}'
            )
            raise err

    with open('conf.toml', 'r') as cf2to:
        confTo = toml.load(cf2to)   
    
    timeToSleep = randint(confTo["settings"]["interval"]["min"], confTo["settings"]["interval"]["min"])
    sleepUntil = datetime.now() + timedelta(seconds=timeToSleep)
    print(
    """
    ██████╗ ███████╗██████╗ ██████╗ ██╗████████╗    ████████╗██╗██╗  ██╗████████╗ ██████╗ ██╗  ██╗    ██████╗  ██████╗ ████████╗
    ██╔══██╗██╔════╝██╔══██╗██╔══██╗██║╚══██╔══╝    ╚══██╔══╝██║██║ ██╔╝╚══██╔══╝██╔═══██╗██║ ██╔╝    ██╔══██╗██╔═══██╗╚══██╔══╝
    ██████╔╝█████╗  ██║  ██║██║  ██║██║   ██║          ██║   ██║█████╔╝    ██║   ██║   ██║█████╔╝     ██████╔╝██║   ██║   ██║
    ██╔══██╗██╔══╝  ██║  ██║██║  ██║██║   ██║          ██║   ██║██╔═██╗    ██║   ██║   ██║██╔═██╗     ██╔══██╗██║   ██║   ██║
    ██║  ██║███████╗██████╔╝██████╔╝██║   ██║          ██║   ██║██║  ██╗   ██║   ╚██████╔╝██║  ██╗    ██████╔╝╚██████╔╝   ██║
    ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═════╝ ╚═╝   ╚═╝          ╚═╝   ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝    ╚═════╝  ╚═════╝    ╚═╝
    """
    )
    print(f"Will sleep for {timedelta(seconds=timeToSleep)} which is until {sleepUntil}")
    sleep(timeToSleep)