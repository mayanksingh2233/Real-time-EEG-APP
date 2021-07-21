from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asyncio import sleep
from random import randint
import time
import pandas as pd
import numpy as np

class GraphConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()


        data = pd.read_csv('data.csv')
        data_numpy =np.array(data)
        main_data =list(data_numpy)
        for row in main_data:
            await self.send(json.dumps({'value':list(row)}))
            await sleep(1)



        # for i in range(1000):
        #     await self.send(json.dumps({'value':randint(-20,20)}))
        #     await sleep(1)

