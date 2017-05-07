from collections import defaultdict
import json

# initial values are autocreated, avoids having to check for key
d = defaultdict(list)
d['states'].append('OK')
d['states'].append('TX')
d['cities'].append('Tulsa')
d['cities'].append('Dallas')

print json.dumps(d)
