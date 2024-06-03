class Email:
    def __init__(self, sender: str, receivers: str, issue: str, body: str):
        self.sender = sender
        self.receivers = receivers
        self.issue = issue
        self.body = body

    def send_email(self):
        print(f"فرستنده: {self.sender}")
        print(f"گیرندگان: {', '.join(self.receivers)}")
        print(f"موضوع: {self.issue}")
        print(f"بدنه: {self.body}")
        print("ایمیل ارسال شد!")


email = Email(
    sender="example@example.com",
    receivers=["recipient1@example.com", "recipient2@example.com"],
    issue="موضوع ایمیل",
    body="این متن بدنه ایمیل است.",
)
email.send_email()
