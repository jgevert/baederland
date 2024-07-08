import datetime
from database.crud import (
    database_connection,
    get_known_course_dates,
    match_course_dates
)
from parser.website_parser import (
    parse_website,
    get_website,
    parse_deeplink,
    get_dates,
    seek_for_location
)
from messaging.email import send_mail


def run_business_logic(
        url: str,
        location_name: str,
        deeplink: str,
        db_file_sting: str,
        course_name: str,
        email_address_list: list,
        email_server: str,
        email_port: int,
        email_password: str,
        email_sender: str,
) -> None:
    """
    Function holds the business logic for the course notification system.
    :param url: URL of the course website.
    :param location_name: Location name to look for in the course website.
    :param deeplink: Deep link to the course website.
    :param db_file_sting: File path to the SQLite database.
    :param course_name: Name of the course.
    :param email_address_list: EMail addresses to send notifications to.
    :param email_server: EMail server.
    :param email_port: EMail server port.
    :param email_password: EMail server password.
    :param email_sender: EMail sender.
    :return: None
    """
    response = get_website(url)
    locations_list = parse_website(response)
    match = seek_for_location(locations_list, location_name)
    if match:
        website = get_website(deeplink)
        free_course_slots = parse_deeplink(website)
        if free_course_slots > 0:
            available_dates_list = get_dates(website)
            db_connection = database_connection(db_file_sting)
            known_course_dates = get_known_course_dates(db_connection)
            are_courses_known = match_course_dates(
                sql_result=known_course_dates,
                course_dates=available_dates_list,
                db_connection=db_connection,
                course_name=course_name,
                location=location_name,
            )
            if not are_courses_known:
                email_sent = send_mail(
                    match=match,
                    receivers=email_address_list,
                    url=url,
                    email_server=email_server,
                    email_port=email_port,
                    email_password=email_password,
                    email_sender=email_sender,
                    course_name=course_name,
                    course_location=location_name,
                )
                if email_sent is not True:
                    print("E-Mail senden fehlgeschlagen", datetime.datetime.now())
            else:
                print("keine neuen Kurse gefunden", datetime.datetime.now())

    else:
        print("No free slots", datetime.datetime.now())