import os
import yt_dlp

class VideoToMp3():
    
    def run(self, *args):
        if len(args) != 2:
            print("Error: Two argument required - video_url, output_folder.")
            return

        video_url = args[0]
        output_folder = args[1]

        try:
            if not self._is_valid_video_url(video_url):
                print("Invalid video URL format. URL must be a valid YouTube link.")
                return
            
            if not self._is_valid_output_folder(output_folder):
                print(f"Invalid output folder path: {output_folder}. Please provide a valid writable directory.")
                return
            
            self._download_youtube_as_mp3(video_url, output_folder)

        except ValueError as e:
            print(f"Error: {e}.")
        except Exception as e:
            print(f"Unexpected Error: {str(e)}")

    def _is_valid_video_url(self, video_url):
        return isinstance(video_url, str) and ("youtube.com/watch?v=" in video_url or "youtu.be/" in video_url)

    def _is_valid_output_folder(self, output_folder):
        if not isinstance(output_folder, str):
            return False
        
        try:
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            test_file = os.path.join(output_folder, '.test_write')
            with open(test_file, 'w') as f:
                f.write('test')
            os.remove(test_file)
            return True
        except (OSError, IOError):
            return False
        
    def _download_youtube_as_mp3(self, video_url, output_folder):
        try:
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
            
            print("Download and conversion to MP3 completed.")
        
        except Exception as e:
            print(f"Error: {str(e)}")
