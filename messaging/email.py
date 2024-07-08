from email.mime.text import MIMEText


def create_email(
        receivers: list,
        sender: str,
        url: str,
        course_name: str,
        course_location: str
) -> object:
    """
    Function creates an email message.
    :param receivers: list of email addresses to send the email to
    :param sender: string representing the sender's email address'
    :param url: URL of the course information
    :param course_name: Name of the course
    :param course_location: Location of the course
    :return: message object containing the email content
    """
    msg = f"Hallo lieber Abonnement\n\n"\
          f"Wir haben eine neue Schwimmkurs für {course_name} im {course_location} gefunden.\n"\
          "Bitte besuchen Sie den Link um weitere Informationen zu erhalten:\n"\
          f"{url}\n\n"\
          "Viel Spaß\n"\
          "Dein Python Crawler"

    message = MIMEText(msg)
    message['to'] = ", ".join(receivers)
    message['from'] = sender
    message['subject'] = "Schwimmkurs für Bronze im Parkbad gefunden"

    return message


def send_mail(
        match: bool,
        receivers: list,
        url: str,
        course_name: str,
        course_location: str,
        email_server: str,
        email_port: int,
        email_password: str,
        email_sender: str) -> bool:
    """
    Function sends the email using the provided SMTP server and port.
    :param match: bool indicating whether a match was found
    :param receivers: list of email addresses to send the email to
    :param url: Deeplink to the course information
    :param email_server: Email server
    :param email_port: Email server port
    :param email_password: Email password
    :param email_sender: Email sender
    :param course_name: Name of the course
    :param course_location: Location of the course
    :return: bool indicating whether the email was sent successfully
    """
    if match:
        print("Sending messaging...")
        import smtplib
        YOUR_EMAIL = email_sender  # The messaging you setup to send the messaging using app password
        YOUR_EMAIL_APP_PASSWORD = email_password  # The app password you generated

        smtpserver = smtplib.SMTP_SSL(host=email_server, port=email_port)  # Using SSL port 465
        smtpserver.ehlo()
        smtpserver.login(YOUR_EMAIL, YOUR_EMAIL_APP_PASSWORD)
        for receiver in receivers:
            msg_text = create_email(
                receivers=[receiver],
                sender=YOUR_EMAIL,
                url=url,
                course_name=course_name,
                course_location=course_location,
            )
            smtpserver.sendmail(msg_text['from'], msg_text['to'], msg_text.as_string())

        # Close the connection
        smtpserver.close()
        return True
    else:
        return False
