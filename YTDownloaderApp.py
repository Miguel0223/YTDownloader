import tkinter as tk
from pytube import YouTube

app = tk.Tk()
app.title("YouTube Video Downloader")
app.geometry("400x200")

# GUI (Graphical User Interface)
label = tk.Label(app, text="Enter YouTube Video URL:")
label.pack(pady=10)

url_entry = tk.Entry(app, width=50)
url_entry.pack(pady=5)

download_button = tk.Button(app, text="Download")
download_button.pack(pady=10)

status_label = tk.Label(app, text="", fg="green")
status_label.pack()

def download_video():
    url = url_entry.get()
    try:
        yt = YouTube(url)
        title = yt.title
        download_path = 'Downloads'
        yd = yt.streams.get_highest_resolution()
        yd.download(download_path)
        status_label.config(text=f"Download of '{title}' completed successfully!")
    except Exception as e:
        status_label.config(text=f"Error: {e}")

download_button.config(command=download_video)

# Start the main event loop of the application
app.mainloop()
