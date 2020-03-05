import requests
import json
import sys
from queue_python import slack

web_hook_url = sys.argv[1]
actions_api = "https://api.github.com/repos/serglit72/azure_queue/actions/runs"
headers = {'Content-Type':'application/json'}
message = str(slack)

get_report = requests.get(url=actions_api,headers=headers)
report = get_report.json()
total = report["total_count"]
last_id = report["workflow_runs"][0]["id"]

workflow = report["workflow_runs"]

for i in range(total):
    if workflow[i]["event"]=="schedule" and workflow[i]["status"] == "completed":
        event = workflow[i]["event"]
        status = workflow[i]["status"]
        conclusion = workflow[i]["conclusion"]
        timestamp = workflow[i]["created_at"]
#         p_event = "Scheduled on "+timestamp+" run On "+str(event)+" and "+str(status)+" with "+str(conclusion).upper()
        p_event = message
        print(p_event)
        break

if conclusion == "success":
    colorr = "good"
else:
    colorr = "danger"
slack_msg = {"attachments":[{"color":colorr,"fields":[{"title":timestamp,"value":p_event,"short":False}]}],
                 "blocks":[{"type":"section","text":{"type": "mrkdwn","text":"*Actions results :* for *azure_queue* ."}}]}
mssge = json.dumps(slack_msg)    
requests.post(web_hook_url,data=mssge)
