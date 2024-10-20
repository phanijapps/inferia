im
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from .pdf_reader import read_pdf
from .pdf_reader import move_file

class FileHandler(FileSystemEventHandler):
    def __init__(self, directory, callback):
        self.directory = directory
        self.callback = callback
        

    def on_created(self, event):
        print(event)
        if event.is_directory:
            print("Is Dir")
            return
        if event.src_path.endswith(".pdf"):
            print(f"New PDF file detected: {event.src_path}")
            read_pdf(event.src_path, self.callback)
            move_file(event.src_path)


def watch_directory(directory,callback = "default_callback"):
    event_handler = FileHandler(directory,callback)
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=False)
    observer.start()
    print(f"Watching directory: {directory}")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def default_callback(text_chunk="", metadata={}):
    """Default Callback Implement Something"""
    print("Implement Callback")
