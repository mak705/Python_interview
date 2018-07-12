from collections import defaultdict
shop_dict = defaultdict(lambda: defaultdict(int))
shops = [(u'shop1', [u'500', u'70', u'86', u'987', u'300']), (u'shoshop2', [u'100']), (u'shop3', [u'50', u'90', u'150', u'108', u'200', u'134']), (u'shop2', [u'700', u'55', u'107', u'800', u'300']), (u'p1', [u'200'])]
for s in shops:
   for e in s[1]:
       shop_dict[s[0]]['sum'] += int(e)
#       print shop_dict[s[0]]['sum']
#       print int(e)
       shop_dict[s[0]]['e'] += 1
#       print shop_dict[s[0]]['e']
for s in shops:
# print shop_dict[s[0]]['sum']/shop_dict[s[0]]['e']
   print shop_dict[s[0]]['sum']
   print shop_dict[s[0]]['e']
  
