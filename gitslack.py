import requests
import json

web_hook_url = "https://hooks.slack.com/services/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"
actions_api = "https://api.github.com/repos/serglit72/azure_queue/actions/runs"
headers = {'Content-Type':'application/json'}

get_report = requests.get(url=actions_api,headers=headers)
report = get_report.json()
last_id = report["workflow_runs"][0]["id"]
event = report["workflow_runs"][0]["event"]
status = report["workflow_runs"][0]["status"]
conclusion = report["workflow_runs"][0]["conclusion"]


slack_msg = {
    "attachments":[{
        "color":"good",
        "fields":[
            {
            "title":conclusion,
            "value":event,
            }
            ]
            }
        ],
        
    "blocks": 
    [
    {
    "type": "section",
    "text": 
        {
        "type": "mrkdwn",
        "text": "Hello, I'm Assistant for  *azure_queue* .\n\n *Actions results :* "
        }
    }
    ]
}
requests.post(web_hook_url,data=json.dumps(slack_msg))
