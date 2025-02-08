# email_extraction
**Python Project to extract names and emails from a string; 'sent to' list from gmail.** 
During my internship, my supervisor would sometimes forward me an email that had an extensive 'sent to' list of different names and emails. 
These lists often included more than one hundred names and corresponding emails. 
They would send me this list because they wanted me to put these names and emails in an excel file so they can easily be added to the organization's newsletter via MailerLite.
To avoid a lot of tedious work and save time, I created this project that automatically identifies distinct names and email addresses from the string I copied from the email forwarded to me.
The names and email addresses are then prepared as an excel file, which I then send to my supervisor, from there they easily upload the names and addresses to MailerLite.
I have provided a string containing 100 names and/or email addresses. For confidentiality purposes, the names and email addresses provided in this demonstration are nonexistent/fake.

Here are the steps to building the code:

1.) **Import the libraries**: All that is needed is Pandas, and Regular expression (or Re)

2.) **create a variable for the string**: I called it 'emailtext', then just copy and paste the long string.

3.) **Regular expression**: I created a variable to store the regex pattern that will help pick out the names and email addresses, 
I called the variable 'emailpattern'. I specified 3 capture groups, 'fullname', 'email', and 'emailonly'. An OR operator splits the
3rd group from the first two, to account for email addresses with no corresponding name.  

4.) **Iteration function**: Then, invoke an iteration function that will search for all occurences, or match objects, 
of the pattern specified by 'emailpattern' in the string 'emailtext'. The function is named "matches"

5.) **For Loop**: Now the iterator will be automated using a for loop, I will now review just the For Loop, step-by-step

    A.) **Loop through the matches**: find each match object 'match' via the iterator 'matches'

    B.) **Extract the full name***: I created the variable 'fullname' to refer to the text that matched with the 'fullname' regex capture group

    C.) **Extract the email**: similar to step B, but for the email address, referred to as variable 'email'. 
    I added an 'or' clause to account for the 'emailonly' regex capture group (in case there was no corresponding name) 

    D.) **Check and refine fullname**: I want to have 3 name columns: full name, first name, and last name. 
    I have to first check that there is a name present, then I can clean and split the full names to first and last names by using .strip() and .split() functions

    E.) **Sorting out the first and last name**: the 'firstname' variable will store the first item from the split list made from the last step ('nameparts[0]'),
    given there is a name present ('if len(nameparts) > 0'), otherwise an empty string is assigned to the variable (" else '' "). The 'lastname' will hold the 
    remaining strings from the .split() list, if there is only a first name("if len(nameparts) > 1 else '' "), an empty string will be assigned.  

    F.) **Handling no name records**: now I placed an 'else' clause to account for strings with an email address only, in which all three name variables will 
    be assigned an empty string (example: " fullname = '' ").

    G.) **Append data**: As the loop runs, each name and corresponding email address will be packaged as a dictionary and placed in the list 'data'.
    The loop now completes the cycle with this step. 

6.) **Convert the list to a dataframe**: using Pandas, the list,'data', is turned into a dataframe and assigned to the variable 'df', 'df = pd.DataFrame(data)'

7.) **Excel**: now the dataframe can be transferred to an excel file by calling the ".to_excel()" dataframe method. I specified the filepath so it goes to a desired destination,
then I excluded the dataframe index. Finally, I call a print statement to indicate the job is complete. 

Thank you for reading.
    
