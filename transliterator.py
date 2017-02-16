# Code that transliterates Latin to Cyrillic based on context, etc.

# Program asks for input text in transliterated Russian, including soft and hard signs, if present.

# The program goes through the text replacing each letter with its correct Cyrillic equivalent. In ambiguous cases, the program makes educated guesses based on context, and sometimes asks the user what Cyrillic letter was meant.

# The program then goes through to correct errors in the transliterated Cyrillic that do not correspond to correct Russian orthography, e.g. йа ---> я, цх ---> ч etc. Sometimes it may ask the user for clarification as of to the Cyrillic letter that was meant.
