from collections import OrderedDict

regular_dict = dict()
regular_dict['foo'] = 1
regular_dict['bar'] = 2
regular_dict['spam'] = 3
regular_dict['grok'] = 4

# regular dict does not maintain insertion order
for k, v in regular_dict.items():
    print '%s - %d' % (k, v)
print '-' * 20
# grok - 4
# foo - 1
# bar - 2
# spam - 3
# --------------------

ordered_dict = OrderedDict()
ordered_dict['foo'] = 1
ordered_dict['bar'] = 2
ordered_dict['spam'] = 3
ordered_dict['grok'] = 4

# OrderedDict does, but is roughly double the size in memory
for k, v in ordered_dict.items():
    print '%s - %d' % (k, v)

# foo - 1
# bar - 2
# spam - 3
# grok - 4
