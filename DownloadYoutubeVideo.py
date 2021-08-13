import pytube

def download_video():
    url = input("Enter Youtube URL: ")
    print("Downloading...")
    pytube.YouTube(url).streams.get_highest_resolution().download()
   

if __name__ == "__main__":
    download_video()
    