from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json
classMyHandler(FileSystemEventHandler):
  i = 1
  def on modified(self, event):
    for filename in os.listdir(folder to track) :
      src = folder_to_track + "/" + filename
      new destination = folder_destination + "/" + filename
      os. rename(src, new_destination)
      
folder_to_track = '/Users/kalle/Desktop/myFolder'
folder_destination = "/Users/kalle/Desktop/newFolder'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
  while True:
    time.sleep(10)
except KeyboardInterrupt:
  observer.stop()
observer.join()
