import json

# with open('itunes_books2.json') as f1:
#     appcontent1 = json.load(f1)

with open('itunes_books1043.json') as f2:
    appcontent2 = json.load(f2)

# appcontent1len = len(appcontent1['results'])
appcontent2len = len(appcontent2['results'])

# print(appcontent1len)
print(appcontent2len)

# for a in appcontent1['results']:
#     print(a['trackCensoredName'])
#     print(a['trackId'])

# for a in appcontent2['results']:
#     print(a['trackCensoredName'])
#     print(a['trackId'])
#     print('------------')

trackNames = []

for a in appcontent2['results']:
    trackNames.append(a['trackId'])

print('full')
# print(trackNames)

print(str(len(trackNames)))

print('nodups')

print(str(len(set(trackNames))))

# duplicates = []
#
#
#
# list(set(duplicates))
#
# print(duplicates)
