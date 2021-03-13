"""

Generate a journal from a template

Protected Keywords: 

- +
    - used to increment the internal date counter

- DD
    - The date - 1, 2, 12, 21 etc.
- MM
    - The month - 01, 10, 12 etc.
- YY
    - The year - 2020, 2021 etc.
- DD_NAME
    - The name of the day (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)
- MM_NAME
    - January, February etc.
- DAYNUM
    - Day number of the year - 123, 340 etc.
- WEEKNUM
    - Week number of the year - 13, 51 etc.

"""

from datetime import datetime, timedelta
import re

###			###
###			###
#  Functions  #
###			###
###			###


"""
    String parseData(
        template_line : String, 
        date					: datetime 
    )

    Given an input string and a datetime date, 
    replace keywords in the input string with various date attributes.
    Strips any "+" characters from the template.

"""


def parseData(template_line, date):

    KEYWORDS = [
        {"keyword": "DD", "variable": date.strftime("%d")},
        {"keyword": "MM", "variable": date.strftime("%m")},
        {"keyword": "YY", "variable": date.strftime("%Y")},
        {"keyword": "DD_NAME", "variable": date.strftime("%A")},
        {"keyword": "MM_NAME", "variable": date.strftime("%B")},
        {"keyword": "DAYNUM", "variable": date.strftime("%j")},
        {"keyword": "WEEKNUM", "variable": date.strftime("%U")},
    ]

    # Go through the line and replace keywords
    # with their associated variables
    for keyword_obj in KEYWORDS:
        kw = keyword_obj["keyword"]
        var = keyword_obj["variable"]

        # template_line = template_line.replace(kw, var)
        template_line = re.sub(r"\b%s\b" % kw, var, template_line)
        template_line = template_line.replace("+", "")

    return template_line


########
## main #
## code #
#######
##      #
##      #
#######

# Check that a template file exists

try:
    f = open("template.txt")
except IOError:
    pass
finally:
    print("found template file.")

# Welcome user to CLI app,
# prompt them for the number of entries to generate

welcome_message = """

Thanks for using JGen.
How many times should the template be duplicated?
Ex - 52 times for a weekly journal, 365 for a daily journal.

"""

print(welcome_message)

journal_length = int(input(">>> "))
print(journal_length)


### MAIN CODE ###

# reads the template.txt file line by line.
# parses each line using parseData.
# writes the parsed line into journal.txt

# creates a date, then increments it whenever it reads a +

with open("template.txt") as template:
    data = template.readlines()
    date = datetime.now()
    with open("journal.txt", "w+") as output_journal:
        for i in range(journal_length):
            for line in data:
                print(parseData(line, date))
                output_journal.write(parseData(line, date))

                if "+" in line:
                    date += timedelta(days=1 * line.count("+"))
