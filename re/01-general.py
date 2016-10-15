'''
Regular Expressions (sometimes shortened to regexp, regex, or re) are a tool for matching patterns in text. In Python, we have the re module. The applications for regular expressions are wide-spread, but they are fairly complex, so when contemplating using a regex for a certain task, think about alternatives, and come to regexes as a last resort.

An example regex is r"^(From|To|Cc).*?python-list@python.org" Now for an explanation: the caret ^ matches text at the beginning of a line. The following group, the part with (From|To|Cc) means that the line has to start with one of the words that are separated by the pipe |. That is called the OR operator, and the regex will match if the line starts with any of the words in the group. The .*? means to un-greedily match any number of characters, except the newline \n character. The un-greedy part means to match as few repetitions as possible. The . character means any non-newline character, the * means to repeat 0 or more times, and the ? character makes it un-greedy.

So, the following lines would be matched by that regex: From: python-list@python.org To: !asp]<,. python-list@python.org

A complete reference for the re syntax is available at the python docs.

As an example of a "proper" email-matching regex (like the one in the exercise), see this
'''