# %%
###########################
######## CHAPTER 9 ########
###########################
## Strings and Text Data ##
###########################

# %%
# import a module
import re

# %% 09-3
# String Formatting
# C-Style
s = 'I only know %d digits of pi' % 7
print(s)

# %%
# For strings, we can use the s placeholder.
print(
    'Some digits of %(cont)s : %(value).2f'
    % {"cont": "e", "value": 2.718}
    )


# %%
# Formatting Numbers
print(
    "In 2005, Lu Chao of China recited {:,} digits of pi".format(67890)
)

# %%
# the 0 in {0:.4} and {0:.4%} refer to the 0 index in this format
# the .4 refers to how many decimal values, 4
# if we provide a %, it will format the decimal as a percentage
print('test number {0:.4} or {0:.4%}'.format(7/67890))

# %%
# the first 0 refers to the index in this format
# the second 0 refers to the character to fill
# the 5 in this case refers to how many characters in total
# the d signals a digit will be used
# Pad the number with 0s so the entire string has 5 characters
print("My ID number is {0:05d}".format(42))

# %% 09-4
# Regular Expressions(RegEx)
# using the re module to write the regular expression pattern

# match 10 digits
tele_num = '1234567890'
m = re.match(pattern='\d\d\d\d\d\d\d\d\d\d', string=tele_num)
print(type(m))      # <class 're.Match'>
print(m)            # <re.Match object; span=(0, 10), match='1234567890'>

# %%
# to run the built-in bool() function to get the boolean value of the match object
print(bool(m))      # True
if m:
    print('match')
else:
    print('no match')

# %%
# to extract some of the match object values

# get the first index of the string match
print(m.start())    # 0
# get the last index of the string match
print(m.end())      # 10
# get the first and last index of the string match
print(m.span())     # (0, 10)
# the string that matched the pattern
print(m.group())    # 1234567890

# %%
# telephone numbers can be a little more complex 
# than a series of 10 consecutive digits

tele_num_spaces = '123 456 7890'

# to simplify the previous pattern
m = re.match(pattern='\d{10}', string=tele_num_spaces)
print(m)    # pattern did not match. object returned None.

# %%
# to see RegEx pattern as a separate variable
# because it can get long and
# make the actual match function call hard to read
p = '\d{3}\s?\d{3}\s?\d{4}'
m = re.match(pattern=p, string=tele_num_spaces)
print(m)

# %%
# Area codes can also be surrounded by parentheses and a dash 
# between the seven main digits
tele_num_space_paren_dash = '(123) 456-7890'
p='\(?\d{3}\)?\s?\d{3}\s?-?\d{4}'
m = re.match(pattern=p, string=tele_num_space_paren_dash)
print(m)

# %%
# a country code before the number
cnty_tele_num_space_paren_dash = '+1 (123) 456-7890'
p='\+?1\s?\(?\d{3}\)?\s?\d{3}\s?-?\d{4}'
m = re.match(pattern=p, string=cnty_tele_num_space_paren_dash)
print(m)
