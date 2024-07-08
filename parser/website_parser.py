import requests
from bs4 import BeautifulSoup
import re


def get_website(url: str) -> str | None:
    if url:
        r = requests.get(url)
        if r.status_code == 200:
            return r.text
    else:
        raise ValueError("No URL provided")


def parse_website(website: str) -> list:
    soup = BeautifulSoup(website, "html.parser")
    partent_element = soup.find_all("ul", class_="course-info-icon--info--locations")
    locations_html = partent_element[0].find_all("li")
    return [location_html.get_text().strip() for location_html in locations_html if len(location_html.get_text()) > 0]


def parse_deeplink(website: str) -> int:
    free_slots_list: list = []
    soup = BeautifulSoup(website, "html.parser")
    free_slots = soup.find_all('li', class_="freie-plaetze")
    for i in range(len(free_slots)):
        result = eval(free_slots[i].get_text().replace("freie Plätze", "").strip())
        if result > 0:
            free_slots_list.append(result)
    if len(free_slots_list) > 0:
        return min(free_slots_list)
    else:
        return 0


def get_dates(website: str) -> list:
    available_dates_list: list = []
    soup = BeautifulSoup(website, "html.parser")
    available_dates = soup.find_all('li', class_="datum")
    available_hours = soup.find_all('li', class_="termin")
    for i in range(len(available_dates)):
        current_result = available_dates[i].get_text().strip()
        current_hourse = available_hours[i].get_text().strip()
        timestamp_in_string = re.findall(r'\d{2}.\d{2}.\d{4}-\d{2}.\d{2}.\d{4}', current_result)
        hours_in_string = re.findall(r'\d{2}:\d{2}-\d{2}:\d{2}', current_hourse)
        new_string = f"{timestamp_in_string[0]} {hours_in_string[0]}"
        available_dates_list.append(new_string)
    if len(available_dates_list) > 0:
        return available_dates_list
    else:
        return []


def seek_for_location(locations_list: list, location: str) -> bool:
    return location in locations_list
