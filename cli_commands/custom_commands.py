# custom_commands.py

from convert.video_to_mp3 import VideoToMp3

def load():
    print("custom_commands.load() called")

    def greet():
        print("Hello from the custom commands package!")

    def vidmp3(args):
        print(f"Video to mp3, Args received: {args}")
        converter = VideoToMp3()
        converter.run(args)

    return {
        "greet": greet,
        "vidmp3": vidmp3
    }
