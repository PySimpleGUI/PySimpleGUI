'''
announcements.py

A utility program that will add the last two announcements
into the readme.md file and the index.md file

the exact path to the index.md file is

readme_creator/output/index.md
'''

import requests, re
from markdownify import markdownify
from datetime import datetime
from bs4 import BeautifulSoup
from pathlib import Path

current_directory = Path(__file__).parent

README_PATH = Path(current_directory.parent, 'readme.md')
INDEX_PATH = Path(current_directory, 'output', 'index.md')

print(README_PATH, INDEX_PATH)

class Announcement:
    ANNOUNCEMENT_ISSUE_URL = "https://github.com/PySimpleGUI/PySimpleGUI/issues/142"

    def __init__(self, title: str, message: str, date_object: datetime, perma_link: str) -> None:
        self.title = title
        self.message = message
        self.date_object = date_object
        self.perma_link = perma_link

    def format_for_readme(self) -> str:
        output = f"### [({self.get_formatted_date()} {self.title})]({self.ANNOUNCEMENT_ISSUE_URL}{self.perma_link})\n"
        output += self.message
        output += f"read the rest [here]({self.ANNOUNCEMENT_ISSUE_URL}{self.perma_link})\n"
        return output

    def format_for_docs(self):
        output = f"#### [({self.get_formatted_date()} {self.title})]({self.ANNOUNCEMENT_ISSUE_URL}{self.perma_link})\n"
        output += self.message
        output += f"read the rest [here]({self.ANNOUNCEMENT_ISSUE_URL}{self.perma_link})\n"
        return output

    def get_formatted_date(self) -> str:
        return datetime.strftime(self.date_object, "%d %B, %Y")

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
        title = body.find(["h1", "h2", "h3", "p"]).string
        message = markdownify(str(body.find("p")))

        announcement_objects.append(Announcement(title, message, date_object, perma_link))

    for i in announcement_objects:
        print(i.__dict__)

    return announcement_objects

def inject_into_readme(announcements: list[Announcement]):
    announcements_string = ""

    for i in announcements:
        announcements_string += i.format_for_readme()

    re_announcements = re.compile(r"(?<=<!-- Announcements -->\s)[\s\S]*(?=<!-- Announcements -->)")

    with open(README_PATH, 'r+') as readme_file:
        readme_content = readme_file.read()
        new_content = re.sub(re_announcements, announcements_string, readme_content)
        readme_file.truncate(0)
        readme_file.seek(0)
        readme_file.write(new_content)

def insert_into_docs(announcements: list[Announcement]):
    announcements_string = ""

    for i in announcements:
        announcements_string += i.format_for_docs()

    announcements_string += "\n"

    with open(INDEX_PATH, 'r+') as readme_file:
        readme_content = readme_file.readlines()

        announcements_index = 0

        while readme_content[announcements_index].strip() != "## Announcements":
            announcements_index += 1

        announcements_index += 1

        while readme_content[announcements_index].strip() != "## PyPI Statistics & Versions":
            readme_content.pop(announcements_index)

        readme_content.insert(announcements_index, announcements_string)

        readme_file.truncate(0)
        readme_file.seek(0)
        readme_file.write(''.join(readme_content))

def main():
    announcements = get_announcements()

    inject_into_readme(announcements)
    insert_into_docs(announcements)

if __name__ == "__main__":
    main()