# Vid

Here is a Python script that will gather data via the command line for videos, allowing the user to input various details. I'll include `link`, `desc`, `title`, and a `1-10` grade, and also suggest a few additional optional fields.

```python
import json

def gather_video_data():
    print("Welcome to the Video Data Collector")

    # Gather mandatory data
    title = input("Enter the video title: ")
    link = input("Enter the video link: ")
    desc = input("Enter the video description: ")
    grade = input("Enter a grade (1-10): ")

    # Optional data
    tags = input("Enter tags for the video (comma separated, leave empty if none): ").split(",") if input("Would you like to add tags? (y/n): ").strip().lower() == "y" else []
    upload_date = input("Enter the video upload date (YYYY-MM-DD): ")
    duration = input("Enter the video duration in minutes: ")
    comments = input("Enter any additional comments: ")

    # Validate grade
    try:
        grade = int(grade)
        if grade < 1 or grade > 10:
            print("Grade must be between 1 and 10. Setting to default value of 5.")
            grade = 5
    except ValueError:
        print("Invalid grade input. Setting to default value of 5.")
        grade = 5

    # Collecting the video data in a dictionary
    video_data = {
        "title": title,
        "link": link,
        "desc": desc,
        "grade": grade,
        "tags": tags,
        "upload_date": upload_date,
        "duration": duration,
        "comments": comments
    }

    # Save the data to a JSON file
    save_option = input("Would you like to save this data? (y/n): ").strip().lower()
    if save_option == "y":
        with open('video_data.json', 'a') as file:
            json.dump(video_data, file, indent=2)
            file.write("\n")
        print("Data saved successfully.")

    # Return the gathered data for further use or display
    return video_data


if __name__ == "__main__":
    video = gather_video_data()
    print("Gathered Video Data:")
    print(json.dumps(video, indent=2))
```

### Optional Fields to Consider Adding:

-   **Category/Genre**: Video's category like "education," "entertainment," etc.
-   **Language**: Language of the video.
-   **Video Quality**: Options like 480p, 720p, 1080p, 4K, etc.
-   **Views**: The number of views the video has.
-   **Likes/Dislikes**: The count of likes or dislikes.
-   **Creator Name**: Name of the person or entity that created the video.
-   **Video Source**: The platform where the video is hosted (YouTube, Vimeo, etc.).
-   **Age Rating**: Age rating like "PG," "18+", etc.
-   **Featured Tags**: Specific features of the video, like "tutorial," "vlog," "comedy," etc.

### Features of the Script:

-   Collects required and optional data.
-   Validates the grade to ensure it's a number between 1 and 10.
-   Saves the collected data to a `video_data.json` file.
