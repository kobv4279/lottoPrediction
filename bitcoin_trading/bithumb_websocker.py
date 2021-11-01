import websockets
import asyncio
import json


async def bithumb_ws_client():
    uri = "wss://pubwss.bithumb.com/pub/ws"

## 웹소켓에 서버를 연결 인터발None은 ping frame 데이터를 보내지 않는다
    async with websockets.connect(uri, ping_interval=None) as websocket:
        greeting = await websocket.recv()
        print(greeting)

##구독요청 형식을 파이썬 딕셔너리로 표현
        subscribe_fmt = {
            "type":"ticker",
            "symbol":["BTC"],
            "tickTypes":["1H"]
        }
#딕셔너리 ->json타입으로 변환
        subscribe_data = json.dumps(subscribe_fmt)
#서버전송
        await websocket.send(subscribe_data)

#데이터를 받음  
        while True:
            data = await websocket.recv()
#json타입 데이터를 파이썬 딕셔너리 타입으로 변환
            data = json.loads(data)
            print(data)

        
async def main():
    await bithumb_ws_client()



asyncio.run(main())