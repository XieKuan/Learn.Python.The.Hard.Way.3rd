name = 'Libna Leon'
age = 19
height = 5.4 # feets
weight = 68.5 # kilogram 8.3.2017 hhh a record
eyes = 'brown'
teeth = 'white'
hair = 'curly and brown'

def kg2p(kg):
 pound = kg * 2.2046226218488
 return (pound)

def p2kg(pound):
 kg = pound * 0.4535237
 return (kg)

print "Let's talk about %s." % name
print "She's %d feets tall." % height
print "She's %d kilograms heavy." % kg2p(weight)
print "Actually that's not too heavy?"
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Her teeth are usually %s depending on the coffee." %teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age+height+weight)
