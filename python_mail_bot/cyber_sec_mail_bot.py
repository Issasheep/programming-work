import yagmail

def send_email():
    """
    Sends an email using yagmail.

    :param subject: Subject of the email
    :param body: Body content of the email
    :param to_email: Recipient's email address
    """
    try:
        # Initialize yagmail with your email and password
        yag = yagmail.SMTP(user='pythontester117@gmail.com', password='ilikedengineeringinschool')
        yag.send(to='jordantait4411@gmail.com', subject="test", contents="hello world")
        print("Email sent successfully")
    except:
        print(f"Error initializing yagmail: {e}")
        return
    

send_email()