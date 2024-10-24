import requests

def send_email(api_key, domain, sender_email, recipient_email, subject, body):
    # Mailgun API URL
    mailgun_url = f"https://api.mailgun.net/v3/{domain}/messages"

    # Data payload for the API request
    data = {
        "from": sender_email,
        "to": recipient_email,
        "subject": subject,
        "text": body,
    }

    # Send the request to Mailgun's API
    response = requests.post(
        mailgun_url,
        auth=("api", api_key),
        data=data
    )

    # Check if the request was successful
    if response.status_code == 200:
        print(f"Email sent successfully to {recipient_email}")
    else:
        print(f"Failed to send email: {response.status_code}")
        print(f"Response: {response.text}")
