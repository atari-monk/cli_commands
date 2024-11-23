import os
import yt_dlp
from cli_logger.logger import setup_logger, LoggerConfig

logger = setup_logger(__name__, LoggerConfig)

class VideoToMp3():
    
    def run(self, args: str):
        argsList = args.split()
        logger.debug("argsList:", argsList, "Length:", len(argsList))
        if len(argsList) != 2:
            logger.error("Error: Two arguments are required - video_url and output_folder.")
            return

        video_url = argsList[0]
        output_folder = argsList[1]

        try:
            if not self._is_valid_video_url(video_url):
                logger.error("Invalid video URL format. URL must be a valid YouTube link.")
                return
            
            if not self._is_valid_output_folder(output_folder):
                logger.error(f"Invalid output folder path: {output_folder}. Please provide a valid writable directory.")
                return
            
            self._download_youtube_as_mp3(video_url, output_folder)

        except ValueError as e:
            logger.error(f"Error: {e}.")
        except Exception as e:
            logger.error(f"Unexpected Error: {str(e)}")

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
            
            logger.info("Download and conversion to MP3 completed.")
        
        except Exception as e:
            logger.error(f"Error: {str(e)}")
