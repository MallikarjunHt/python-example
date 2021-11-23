# "base string with {} placeholders".format(variables)

example = "format() method"

formatted_string = "this is an example of using the {} on a string".format(example)

print(formatted_string)

"""Outputs:
this is an example of using the format() method on a string
"""

# "{0} {1}".format(first, second)

first = "apple"
second = "banana"
third = "carrot"

formatted_string = "{0} {2} {1}".format(first, second, third)

print(formatted_string)

"""Outputs:
apple carrot banana
"""

# "{var1} {var2}".format(var1=value1, var2=value2)

"{:exp1} {:exp2}".format(value1, value2)

# {:d} integer value
'{:d}'.format(10.5) → '10'


Expr  | Meaning    | Example
--------------------------------
{:d}  | integer value | '{:d}'.format(10.5) → '10'

{:.2f} | floating point with that many decimals |'{:.2f}'.format(0.5) → '0.50'

{:.2s} | string with that many characters | '{:.2s}'.format('Python') → 'Py'

{:<6s} | string aligned to the left that many spaces | '{:<6s}'.format('Py') → 'Py    '

{:>6s} | string aligned to the right that many spaces | '{:>6s}'.format('Py') → '    Py'

{:^6s} | string centered in that many spaces | '{:^6s}'.format('Py') → '  Py  '


