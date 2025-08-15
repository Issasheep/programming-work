import yagmail

def send_email(subject, body, to_email):
    """
    Sends an email using yagmail.

    :param subject: Subject of the email
    :param body: Body content of the email
    :param to_email: Recipient's email address
    """
    try:
        # Initialize yagmail with your email and password
        yag = yagmail.SMTP('pythontester117@gmail.com', 'ilikedengineeringinschool')
    except Exception as e:
        print(f"Error initializing yagmail: {e}")
        return