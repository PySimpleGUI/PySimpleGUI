import requests
from markdownify import markdownify
from datetime import datetime
from bs4 import BeautifulSoup

class Announcement:
    def __init__(self, title, message, date_object, perma_link) -> None:
        self.title = title
        self.message = message
        self.date_object = date_object
        self.perma_link = perma_link

def get_announcements() -> list[Announcement]:
    announcement_objects = []

    URL = "https://github.com/PySimpleGUI/PySimpleGUI/issues/142"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    announcements = soup.find_all(class_="timeline-comment")

    for announcement in announcements[-2:]:
        header = announcement.find(class_="timeline-comment-header")
        perma_link = header.find(class_="js-timestamp")['href']

        timestamp = header.find("relative-time")['datetime']
        date_object = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")

        body = announcement.find(class_="comment-body")
        title = body.find(["h1", "h2", "h3", "p"])
        message = body.find("p")

        announcement_objects.append(Announcement(title, message, date_object, perma_link))

    for i in announcement_objects:
        print(i.__dict__)

    return announcement_objects

def main():
    announcements = get_announcements()

if __name__ == "__main__":
    main()