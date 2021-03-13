# JGen

Generate a text-based journal from a template file.

## Contents

- [Overview](#overview)
- [Usage](#usage)
- [Details](#details)
- [Reserved Keywords](#reserved-keywords)
- [Example](#example)
- [Gotchas](#gotchas)

## Overview

JGen parses a given template file to generate a journal file.

JGen runs through the template file and replaces keywords with their actual values (dates - day/month/year etc.), for a specified number of entries.

## Usage

The JGen Python script contains all the code for the parser.
To get started:

- Download the JGen script.
- Create a template.txt file (or download and rename one of the examples in /templates), and place it in the same directory as the JGen Python script.

  - See [Details](#Details) below for more information on creating a template.

  - See an [Example](#Example) to walk through a specific example of a template file.

- Run the JGen Python script, and input the number of times the template should be reproduced.
  - Ex: 365 entries for a daily journal spanning a year, 52 entries for a weekly journal

## Details

See the [Example](#Example) section below if you want to jump straight into seeing how JGen works, by walking though an example.

JGen parses the template file, replacing any of the reserved keywords, shown below, with their corresponding date values.

Part of the templating process is to indicate using a (+) symbol when to increment the internal date counter, which JGen picks up as it parses the file. It also strips all (+) symbols from the file.

### Reserved Keywords

- DD
  - The date number.
  - 01, 05, 10, 21 etc.
- MM
  - The month number.
  - 01, 10, 12 etc.
- YY
  - The year.
  - 2020, 2021 etc.
- DD_NAME
  - The name of the day.
  - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
- MM_NAME
  - January, February etc.
- DAYNUM
  - Day number of the year.
  - 123, 340 etc.
- WEEKNUM

  - Week number of the year.
  - 13, 51 etc.

- \+

  - used to increment the internal date counter
  - will only increment after the entire line has been parsed

    - for example, parsing

    ```
    DD/MM/YY+ - DD/MM/YY
    ```

    would give

    ```
    21/02/2050 - 21/02/2050
    ```

    and not

    ```
    21/02/2050 - 28/02/2050
    ```

### Example

Given the following template (available as templates/template_weekly.txt) -

```
_____________________________
Week: WEEKNUM, Year: YY
DD_NAME, DD MM_NAME - +++++++
DD_NAME, DD MM_NAME

Todos: - - -

Plans: - - -
```

and running JGen for two entries gives us -

```
_____________________________
Week: 10, Year: 2021
Saturday, 13 March -
Saturday, 20 March

Todos:
	-
	-
	-

Plans:
	-
	-
	-


_____________________________
Week: 11, Year: 2021
Saturday, 20 March -
Saturday, 27 March

Todos:
	-
	-
	-

Plans:
	-
	-
	-

```

Lets break down what happened -

1. JGen sets it's internal date - "today's" date, from your perspective.
2. JGen runs through line 1 and line 2 of template.txt, replacing keywords with their corresponding information and then writing the output to journal.txt.
3. At the end of line 2 there are seven + (plus) symbols
   - JGen removes these from the output, and increments the internal date counter by 7 days.
4. JGen fills out line 3 with the new date information, then fills out the rest of the information for the first entry.
5. It then repeats this for the second entry, carrying over the date from the end of the first entry.
6. JGen halts, with journal.txt containing our final output.

## Gotchas

- \+ can _only_ be used to increment the date.
  - All \+ symbols are removed from the output.
  - ie. journal.txt file will never contain a \+ character
- As mentioned in the "reserved keywords" section of this readme, the \+ characters are only interpreted at the end of a line.

  - Currently, to work around this, just place the second date on a new line (like in templates/template_weekly.txt)
  - For example, parsing

    ```
    DD/MM/YY+ - DD/MM/YY
    ```

    would give

    ```
    21/02/2050 - 21/02/2050
    ```

    and not

    ```
    21/02/2050 - 28/02/2050
    ```
