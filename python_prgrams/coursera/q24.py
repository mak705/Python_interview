def secret_formula(started):
    jelly_beans = started * 5
    jars = jelly_beans / 10
    crates = jars / 10
    return jelly_beans, jars, crates


start_point = 100
jars, beans, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

#start_point = start_point / 10
#
#print "We can also do that this way:"
#print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
