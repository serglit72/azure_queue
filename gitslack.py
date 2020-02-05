import requests
import json
import sys

web_hook_url = sys.argv[1]
actions_api = "https://api.github.com/repos/serglit72/azure_queue/actions/runs"
headers = {'Content-Type':'application/json'}

get_report = requests.get(url=actions_api,headers=headers)
report = get_report.json()
total = report["total_count"]
last_id = report["workflow_runs"][0]["id"]

workflow = report["workflow_runs"]

for i in range(total):
    if workflow[i]["event"]=="schedule":
        event = report["workflow_runs"][i]["event"]
        status = report["workflow_runs"][i]["status"]
        conclusion = report["workflow_runs"][i]["conclusion"]
        timestamp = report["workflow_runs"][i]["created_at"]
        p_event = "Scheduled on 15:00 UTC run On "+event+" and "+status+" with "+conclusion
        print(p_event)
        break

if status == "SUCCESS":
    colorr = "good"
else:
    colorr="danger"
slack_msg = {"attachments":[{"color":colorr,"fields":[{"title":timestamp,"value":p_event,"short":False}]}],
                 "blocks":[{"type":"section","text":{"type": "mrkdwn","text":"*Actions results :* for *azure_queue* ."}}]}
message = json.dumps(slack_msg)    
requests.post(web_hook_url,data=message)
