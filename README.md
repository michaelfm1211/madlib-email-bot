# Madlib Email Bot
This program does exactly what it sounds like, it's an email bot which fills out madlibs for you. Madlib 
Email is licensed under the [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) 
License. Please refer to the LICENSE file in the directory for the full text.

### Runing it
You can run Madlib Email Bot by running `python3 madlib.py`, but that will not work. The `madlib.py`
script takes 6 environment variables. The EMAIL environment variable is the email account to use and
login with for the bot. Email will be retrieved and sent from this address. The PASSWORD environment 
variable is the password to the email account specified with the EMAIL environment variable. The 
SMTP_SERVER and IMAP_SERVER environment variables are URLs to the SMTP sever and IMAP sever the bot should 
use respecivly. The BATCH_SIZE environment variable is how many emails should be processed in one batch, and the INTERVAL environment variable is how long to wait between batches in seconds.

Example Usage:
```
INTERVAL=10 \
BATCH_SIZE=10 \
IMAP_SERVER="imap.gmail.com" \
SMTP_SERVER="smtp.gmail.com:587" \
EMAIL="my.bot@gmail.com" \
PASSWORD="password1" \
python3 madlib.py
```

### How to Use
Once the bot is running, you can email the bot's email address with subject line `MADLIB` to trigger the 
bot and have the email processed. In the email's body, you just write you email regularly, but if you want 
the bot to insert a word, you can use a placeholder. Placeholders are very simple to use. Just write the 
type of word you want, then surround it with brackets. For example, if you want a noun, you would write 
`[noun]`. The supported placeholders are: `[noun]`, `[adjective]`, `[verb]`, `[adverb]`, and `[pronoun]`

Example Email:
```
Hello [noun]!,
I'm so [adjective] today! Right now I'm [adverb] [verb]ing, and later Jeff and I are going to [verb]

Your [adjective] [noun],
Bob
```
Example Output:
```
Hello spectacle!,
I'm so dead today! Right now I'm pointedly blowing, and later Jeff and I are going to deck

Your unfilled luminesce,
Bob
```

####  Dependencies & Legal
Madlib Email Bot uses Python 3, smtplib from Python 3, and the easyimap library. The easyimap license can be found at https://raw.githubusercontent.com/keitaoouchi/easyimap/master/LICENSE.txt.

Madlib Email Bot is in no way affiliated with Penguin Random House LLC, who owns Mad Libs™. The usage of
the word "Madlib" in the title is simply used to quickly describe what the program does. The use of the word "Madlib" is not used to advertise or promote this product. All users of this program should disregard the use of the word "Madlib," as it's only purpose is to give a general sense of what the program does, as most people know what a Madlib is.

<p xmlns:dct="http://purl.org/dc/terms/" xmlns:vcard="http://www.w3.org/2001/vcard-rdf/3.0#">
  <a rel="license"
     href="http://creativecommons.org/publicdomain/zero/1.0/">
    <img src="http://i.creativecommons.org/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" />
  </a>
  <br />
  To the extent possible under law,
  <a rel="dct:publisher"
     href="http://micmacro.com">
    <span property="dct:title">Michael M</span></a>
  has waived all copyright and related or neighboring rights to
  <span property="dct:title">Madlib Email Bot</span>.
This work is published from:
<span property="vcard:Country" datatype="dct:ISO3166"
      content="US" about="http://micmacro.com">
  United States</span>.
</p>