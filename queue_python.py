import base64
import argparse
import sys

sys.path.append('/usr/local/lib/python3.7/site-packages')
# sys.path.append('/usr/local/opt/python/bin/python3.7')
from azure.storage.queue import QueueServiceClient


parser = argparse.ArgumentParser(description='Script for running acceptance test on Kaspersky side')

parser.add_argument("--InfraName", default="AF")
parser.add_argument("--InfraEnv",  default="Beta")
#parser.add_argument("--InfraEnv",  default="Prod")
#parser.add_argument("--InfraVer",  default="1.0.0.0.0")
parser.add_argument("--InfraVer",  default="0.7.1.0.rc3")
args = parser.parse_args()
 
tmp = {'InfraName': args.InfraName, 'InfraEnvironment': args.InfraEnv, 'InfraReleaseVersion': args.InfraVer}

message = str(tmp)
slack = args.InfraEnv+" v."+args.InfraVer
encodedBytes = base64.b64encode(message.encode('utf-8'))
encodeMessage = str(encodedBytes, "utf-8")

queue_service = QueueServiceClient(account_url = 'https://ksdetoolapp.queue.core.windows.net/', credential='st=2019-10-30T13%3A09%3A30Z&se=2024-10-31T13%3A09%3A00Z&sp=raup&sv=2018-03-28&sig=zv65h0y6mBGoWKeO83sa7nwtfespLMoLLuntSRgOGdE%3D')

queue_client = queue_service.get_queue_client(queue="afintegration")

queue_client.send_message(encodeMessage)
