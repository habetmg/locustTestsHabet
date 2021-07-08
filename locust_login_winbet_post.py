#https://bet.priotix.xyz/welcome?action=signIn

'''aid: "cd4d4540-2a1f-4223-986b-af3602c0a314"
cd: "24"
cs: "UTF-8"
ds: "337x4011"
dtm: "1625638682665"
duid: "4e3d48d3-cbca-42c2-8aeb-4445459f010e"
e: "ue"
eid: "747a09ff-7ae9-41ff-b595-e6624a8f957d"
f_ag: "0"
f_dir: "0"
f_fla: "0"
f_gears: "0"
f_java: "0"
f_pdf: "1"
f_qt: "0"
f_realp: "0"
f_wma: "0"
lang: "hy-AM"
p: "web"
refr: "https://bet.priotix.xyz/welcome"
res: "1366x768"
sid: "5de40593-4aeb-4b35-9f77-adb97ab6ec6c"
stm: "1625638682667"
tna: "thrift"
tv: "js-2.16.3"
tz: "Europe/Moscow"
ue_pr: "{\"schema\":\"iglu:com.snowplowanalytics.snowplow/unstruct_event/jsonschema/1-0-0\",\"data\":{\"schema\":\"iglu:com.snowplowanalytics.snowplow/submit_form/jsonschema/1-0-0\",\"data\":{\"formId\":\"FORM\",\"formClasses\":[],\"elements\":[{\"name\":\"username\",\"value\":\"noro2\",\"nodeName\":\"INPUT\",\"type\":\"text\"}]}}}"
uid: "5febedf9-12bb-4e6c-b6cf-a17db6628905"
url: "https://bet.priotix.xyz/welcome?action=signIn"
vid: "82"
vp: "352x595"
schema: "iglu:com.snowplowanalytics.snowplow/payload_data/jsonschema/1-0-4"'''

from locust import HttpUser,task,TaskSet
class Behaviour(TaskSet):
    @task
    def login(self):
        self.client.post("https://www.google-analytics.com/g/collect?v=2&tid=G-DR45FWMDQJ&gtm=2oe6u0&_p=20924399&sr=1366x768&ul=hy-am&cid=917347990.1619003753&_s=2&dl=https%3A%2F%2Fbet.priotix.xyz%2Fesports%2Fhome%2Fmatches%3Faction%3DsignIn&dr=https%3A%2F%2Fbet.priotix.xyz%2Fesports%2Fhome%2Fmatches&dt=All%20Upcoming%20Esports%20Matches&sid=1625648810&sct=109&seg=1&en=page_view&_et=21805")

class User(HttpUser):
    tasks=[Behaviour]
    min_wait = 2000
    max_wait = 5000
    host="https://bet.priotix.xyz/esports/home/matches?action=signIn"