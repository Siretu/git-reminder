import json
import urllib2
import oauth_secret
import pprint
import datetime
import os

USER = "Siretu"

def get_events():
    request = urllib2.Request("https://api.github.com/users/%s/events" % USER, 
                            headers={"Authorization" : "token %s" % oauth_secret.secret})
    return json.loads(urllib2.urlopen(request).read())

def get_todays_events():
    events = get_events()
    result = []
    for e in events:
        if e["public"] and e["type"] == "PushEvent":
            date_string = e["created_at"]
            d = datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ").date()
            if d == datetime.date.today():
                result.append(e)
    return result

def get_commits_from_event(event):
    return len(e["payload"]["commits"])

def main():
    events = get_todays_events()
    pprint.pprint(events)
    if events:
        commits = sum([get_commits_from_event(e) for e in events])
        os.system('espeak "Good job, %d commits so far today"' % commits)
    else:
        os.system('espeak "Don\'t forget to commit"')
       

if __name__ == "__main__":
    main()
