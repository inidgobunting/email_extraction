import pandas as pd
import re

#paste copied text here
emailtext = """John Doe <johndoe92@randommail.com>, Jane Smith <janesmith76@fakemail.org>, Bobby J <bobjohnson88@nomail.net>, Alice Brown <alicebrown21@mockemail.com>, Mike <michaelwhite45@dummy.org>, 
Sarah Green <sarahgreen99@madeupmail.com>, David Black <davidblack32@notreal.net>, Emily Adams <emilyadams65@fauxmail.com>, Chris Miller <chrismiller87@pretendmail.com>, Jess W. <jessicawilson54@fakemail.org>,
Tom Clark <tomclark12@randommail.com>, Laura Harris <lauraharris90@nomail.net>, Kevin Roberts <kevinroberts34@dummy.org>, Rachel Hall <rachelhall73@mockemail.com>, Brian King <brianking56@madeupmail.com>, 
Anna Scott <annascott28@notreal.net>, Daniel Lewis <daniellewis47@fauxmail.com>, Megan W. <meganwalker67@pretendmail.com>, Matthew Young <matthewyoung89@fakemail.org>, Olivia A. <oliviaallen23@randommail.com>, 
Jason Hernandez <jasonhernandez55@nomail.net>, Stephanie Wright <stephaniewright38@dummy.org>, Nathan Hill <nathanhill61@mockemail.com>, Angela P. <angelaperez95@madeupmail.com>, Justin Carter <justincarter29@notreal.net>, 
Emma Murphy <emmamurphy74@fauxmail.com>, Ryan Nelson <ryannelson42@pretendmail.com>, Lisa Mitchell <lisamitchell83@fakemail.org>, Patrick Ramirez <patrickramirez19@randommail.com>, Kimberly Cooper <kimberlycooper57@nomail.net>, 
Andrew Bailey <andrewbailey68@dummy.org>, Michelle <michelleflores22@mockemail.com>, Joshua Reed <joshuareed90@madeupmail.com>, Rebecca Gonzales <rebeccagonzales31@notreal.net>, Timothy Simmons <timothysimmons44@fauxmail.com>, 
Hannah Foster <hannahfoster75@pretendmail.com>, Ethan Rogers <ethanrogers26@fakemail.org>, <sophiajenkins55@randommail.com>, <brandonmartinez39@nomail.net>, Victoria Stewart <victoriastewart97@dummy.org>, 
Tyler Barnes <tylerbarnes81@mockemail.com>, Lauren Ross <laurenross20@madeupmail.com>, Dylan Brooks <dylanbrooks50@notreal.net>, Natalie Sanders <nataliesanders71@fauxmail.com>, Jeremy Evans <jeremyevans18@pretendmail.com>, 
Kaitlyn Rivera <kaitlynrivera94@fakemail.org>, Jonathan Hayes <jonathanhayes63@randommail.com>, Caroline Ward <carolineward33@nomail.net>, Eric <ericmorales48@dummy.org>, Vanessa Price <vanessaprice86@mockemail.com>, 
Shane Bell <shanebell37@madeupmail.com>, <amyhoward66@notreal.net>, Gregory Butler <gregorybutler24@fauxmail.com>, Rachel James <racheljames79@pretendmail.com>, Vincent Long <vincentlong46@fakemail.org>, 
Cassandra Powell <cassandrapowell58@randommail.com>, Jared Bryant <jaredbryant17@nomail.net>, Melanie Griffin <melaniegriffin93@dummy.org>, Aaron Lopez <aaronlopez72@mockemail.com>, Cynthia Wood <cynthiawood35@madeupmail.com>, 
Oscar Bennett <oscarbennett51@notreal.net>, Danielle Turner <danielleturner70@fauxmail.com>, Trevor Patterson <trevorpatterson29@pretendmail.com>, <morganhughes92@fakemail.org>, Evan Coleman <evancoleman60@randommail.com>, 
Madison Jenkins <madisonjenkins32@nomail.net>, Gabriel Sanders <gabrielsanders45@dummy.org>, Allison Perry <allisonperry88@mockemail.com>, Sean Edwards <seanedwards54@madeupmail.com>, <lydiarussell27@notreal.net>, 
Colin Thompson <colinthompson69@fauxmail.com>, Valerie Scott <valeriescott94@pretendmail.com>, Anthony Flores <anthonyflores36@fakemail.org>, Julia Myers <juliamyers85@randommail.com>, Cameron <cameronwatson19@nomail.net>, 
Brooke Alexander <brookealexander71@dummy.org>, Travis Griffin <travisgriffin41@mockemail.com>, <kaylasimmons99@madeupmail.com>, B. Hall <blakehall56@notreal.net>, Savannah <savannahwright28@fauxmail.com>, 
Gavin Collins <gavincollins75@pretendmail.com>, <haleycampbell23@fakemail.org>, Seth Robinson <sethrobinson62@randommail.com>, <leahbarnes33@nomail.net>, Austin Ward <austinward44@dummy.org>, 
Paige Mitchell <paigemitchell86@mockemail.com>, Connor Butler <connorbutler57@madeupmail.com>, J. Reed <jennareed21@notreal.net>, Lucas Phillips <lucasphillips48@fauxmail.com>, Sophie Foster <sophiefoster72@pretendmail.com>, 
Nathaniel Price <nathanielprice30@fakemail.org>, Molly Parker <mollyparker91@randommail.com>, Christian Hayes <christianhayes67@nomail.net>, Brittany B. <brittanybrooks38@dummy.org>, Jordan Ward <jordanward55@mockemail.com>, 
Amber Torres <ambertorrres24@madeupmail.com>, Dylan Kelly <dylankelly90@notreal.net>, Vanessa Hughes <vanessahughes33@fauxmail.com>, Sean Ramirez <seanramirez71@pretendmail.com>, M. J. <madisonjames49@fakemail.org>
"""
#Regex
emailpattern = r'(?P<fullname>[^<>,]*)\s*<(?P<email>[^<>]+)>|(?P<emailonly>[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'
matches = re.finditer(emailpattern, emailtext)
#going through the matches
data = []
for match in matches:
    fullname = match.group('fullname')
    email = match.group('email') or match.group('emailonly')
    if fullname:
        fullname = fullname.strip()
        nameparts = fullname.split()
        firstname = nameparts[0] if len(nameparts) > 0 else ''
        lastname = ' '.join(nameparts[1:]) if len(nameparts) > 1 else ''
    else:
        fullname = ''
        firstname = ''
        lastname = ''
    data.append({
        "full name": fullname,
        "first name": firstname,
        "last name": lastname,
        "email": email
    })
#convert to df
df = pd.DataFrame(data)
#save as excel file
df.to_excel(r'_:\_____\_____\______\name.xlsx', index=False)
print("extraction complete")
