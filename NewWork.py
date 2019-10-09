x = "There are %d types of people." % 10
binary = "binary"
doNot = "don't"
y = "those who know %s and those who %s." % (binary, doNot)

print(x)
print(y)

print("I said: %r" % x)
print("I also said:  '%s'." % y)

hilarious=False
joke_evaluation="Isn't that joke so funny?! %r"
print(joke_evaluation % hilarious)

w = "This is the left side of.."
e = "a string with a right side."

print(w + e)


# more stuff 10-8

print("Mary had a little lamb")
print("Its fleece was what as %s." % 'snow')
print("And everywhere that Mary went.")
print("." * 10)

end1 = "c"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "b"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1 + end2 + end3 + end4 + end5 + end6 + end7 + end8 + end9 + end10 + end11 + end12)

# More Formatting
formatter = "%r %r %r %r"
# setting the format
print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
# saying its true and false
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))

# why did I  use %r instead of %s?
# because you used it at the beginning

# Time for some strange stuff in te world of printing...

days = "mon tue wed thu fri sat sun"
months = "jan\nfeb\nmar\napr\nmay\njun\njuly\naug"

print("here are the days: ", days)
print("here are the months: ", months)

