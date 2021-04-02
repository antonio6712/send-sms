from apikey import TOKEN,SERVICE_ID,NUMERO_TELEFONO,NUMERO_TELEFONO_R

import clx.xms
import requests
import json

client = clx.xms.Client(service_plan_id=SERVICE_ID,token=TOKEN)

create = clx.xms.api.MtBatchTextSmsCreate()
create.sender = NUMERO_TELEFONO
create.recipients = {NUMERO_TELEFONO_R}
create.body = "amorcito"

try:
    batch = client.create_batch(create)
except (requests.exceptions.RequestsException,clx.xms.exceptions.ApiException) as ex:
    print('Failed to communicate with XMS: %s' % str(ex))