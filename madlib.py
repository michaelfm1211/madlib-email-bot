# Example Usage:
#	INTERVAL=10 \
#	BATCH_SIZE=10 \
#	IMAP_SERVER="imap.gmail.com" \
#	SMTP_SERVER="smtp.gmail.com:587" \
#	EMAIL="my.bot@gmail.com" \
#	PASSWORD="password1" \
#	python3 madlib.py

from os import environ
from random import choice
from time import sleep
from threading import Event, Thread
import smtplib
import easyimap
import re

# Environment Variables

email = environ['EMAIL']  # Email to send & receive from
password = environ['PASSWORD']  # Password to that email account
imap = environ['IMAP_SERVER']  # The IMAP Server
smtp = environ['SMTP_SERVER']  # The SMTP Server
# How many second to wait between batches NOTE: if this is too frequent, you might get blocked
interval = int(environ['INTERVAL'])
# How many emails to process per batch, if you're not in batch, you wait until next batch
batch_size = int(environ['BATCH_SIZE'])

# Setup/Initalization

smtpObj = smtplib.SMTP(smtp)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(email, password)

while True:
    # Get mail
    # Connect to IMAP Server(we need a new one every time to get new mail)
    imapper = easyimap.connect(imap, email, password)

    mails = imapper.unseen(batch_size)  # Read batch_size of emails
    if mails == []:  # If there's no emails, skip
        sleep(interval)
        continue

    # mail = mail[0]	# If we're here, there's email, so grab it(we only got one, so its an array with only that one)

    for mail in mails:  # Do the following for every email in the batch

        if mail.title != "MADLIB":  # If subject line is not MADLIB
            sleep(interval)  # Skip
            continue

        sender = mail.from_addr  # If we're here, the email is valid, so let's get the sender

        # Parse Madlib

        body = mail.body 	# Now let's get the actual content

        print("NEW EMAIL")  # Tell the server's owner about the new email
        print("From: {}".format(sender))
        print(body)
        print("\n")

        # Get a bunch of text
        nouns = open("dict/nouns.txt", "r").read().split("\n")
        adjectives = open("dict/adj.txt", "r").read().split("\n")
        verbs = open("dict/verb.txt", "r").read().split("\n")
        adverbs = open("dict/adv.txt", "r").read().split("\n")

        # And create a regex to search for the placeholders
        expr = re.compile("\[\w+\]")

        # Then search for the regex in the email's content
        placeholders = expr.findall(body)

        new = ""  # Then, create a variable to store the new, parsed, content
        # And split the original content by the regex
        split_body = expr.split(body)
        for s in split_body:  # For everything split item
            # If it's the last split item
            if split_body.index(s) == len(split_body) - 1:
                new += s  # Its the end of the loop, so don't add words to the end of it
                # And stop the loop(we don't want to do the rest, & it's the last item in the list anyway)
                break

            # Get the split item's index in the split's list
            i = split_body.index(s)
            # And get it's corresponding placeholder
            placeholder = placeholders[i]

            # Bunch of logic: basically get a choice for every placeholder in it's corresponding word choices
            if placeholder == "[noun]":
                word = choice(nouns)
            elif placeholder == "[adjective]":
                word = choice(adjectives)
            elif placeholder == "[verb]":
                word = choice(verbs)
            elif placeholder == "[adverb]":
                word = choice(adverbs)
            elif placeholder == "[pronoun]":
                word = choice(["he", "she", "it"])

            new += s + word 	# And add that chosen word to the split item, and add it to the new content

        # Send parsed Madlib back to sender

        # Tidy everything up for the end user, including From & To headers and a subject line with makes a reply
        prepared_new = "From: {}\nTo: {}\nSubject: Re: MADLIB\n\n".format(
            email, sender) + new

        smtpObj.sendmail(email, [sender], prepared_new.encode(
            'utf-8'))  # Send the email
        # Repeat again for next email

    # FROM NOW ON, WE'RE OUT OF EMAIl LOOP, BUT STILL IN PROGRAM LOOP

    imapper.quit()  # And get rid of the IMAP connection
    sleep(interval)  # And just wait a while before we do it again
