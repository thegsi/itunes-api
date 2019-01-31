import urllib.request
import json
import time


apps = {"results": []}
offset = 3000

def getApps():

    def getRequest ():
        global offset
        try:
            # https://stackoverflow.com/questions/27760167/how-to-use-itunes-search-for-genres
            offsetUrl = 'https://itunes.apple.com/search?term=books&country=gb&entity=software&genreId=6018&offset=%d&limit=20' % offset
            # offsetUrl = 'https://itunes.apple.com/search?term=1&country=gb&media=all&attribute=genreIndex&offset=%d&limit=3' % offset
            appcontent = json.loads(urllib.request.urlopen(offsetUrl).read())
            print(len(appcontent['results']))
            if len(appcontent['results']) > 0 and offset < 3500:
                apps['results'].extend(appcontent['results'])
                offset += len(appcontent['results'])
                print('total' + str(len(apps['results'])))
                print(offset)
                time.sleep(1)
                getRequest()
            else:
                print('no results or offset exceeded')
                return
        except:
            print('error - 403 forbidden')
            return
    getRequest()

getApps()

filename = 'itunes_books%d.json' % offset

with open(filename, 'w') as outfile:
    json.dump(apps, outfile)
