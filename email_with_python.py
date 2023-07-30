import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'N3M3515'
email['to'] = 'hellpri3st@gmail.com'
email['subject'] = 'you have won a Ryzen 5 5600XD with and an AMD Radeon 6750XT '

email.set_content(
    'Since you got into college and now you need a new midrange PC hereare the free parts for that , buy the rest by yourself')

# now using this we will login into our gmail to send the email
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()

# this is an encryption mechanism , to connect securely to the server
    smtp.starttls()

    smtp.login('rsdas2016.koustav@gmail.com', 'vangaurd')
    smtp.send_message(email)
    print('all good boss!')
