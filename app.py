from configuration.configuration import run
from operations.operations import run_business_logic


def main():
    # load configurations
    configurations = run(file='config.ini')

    if configurations.get('Target'):
        url = configurations.get('Target').get('targeturl')
        deeplink = configurations.get('Target').get('deeplink')
        location_name = configurations.get('Target').get('targetname')
    else:
        raise ValueError("config file is missing Target section")

    if configurations.get('Database'):
        db_file_sting = configurations.get('Database').get('databasefile')
    else:
        raise ValueError('Database section is missing in config file')

    if configurations.get('EMails'):
        email_address_list = eval(configurations.get('EMails').get('addresses'))
        email_sender = configurations.get('EMails').get('senderemail')
        email_password = configurations.get('EMails').get('emailpassword')
        email_server = configurations.get('EMails').get('emailserver')
        email_port = eval(configurations.get('EMails').get('emailport'))
    else:
        raise ValueError('EMails section is missing in config file')

    if configurations.get('CourseInformation'):
        course_name = configurations.get('CourseInformation').get('coursename')
    else:
        raise ValueError('CourseInformation section is missing in config file')

    run_business_logic(
        url=url,
        location_name=location_name,
        deeplink=deeplink,
        db_file_sting=db_file_sting,
        course_name=course_name,
        email_address_list=email_address_list,
        email_server=email_server,
        email_port=email_port,
        email_password=email_password,
        email_sender=email_sender,
    )


if __name__ == "__main__":
    main()
