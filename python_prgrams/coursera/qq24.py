def sec_for(mak):
    hi = mak * 5
    hello = hi / 2
    return hi, hello


maku = 10
hi, hello = sec_for(maku)

print "With a starting point of: %d" % maku
print "We'd have %d hi, %d hello" % (hi, hello)

maku = maku / 10

print "We can also do that this way:"
print "We'd have %d hi, %d hello" % sec_for(maku)

