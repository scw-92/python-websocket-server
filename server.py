from websocket_server import WebsocketServer

# Called for every client connecting (after handshake)
def new_client(client, server):
	print("New client connected and was given id %d" % client['id'])
	server.send_message_to_all("Hey all, a new client has joined us")//此函数会发给已经链接的所客户端


# Called for every client disconnecting
def client_left(client, server):
	print("Client(%d) disconnected" % client['id'])


# Called when a client sends a message
def message_received(client, server, message):
	if len(message) > 200:
		message = message[:200]+'..'
	print("Client(%d) said: %s" % (client['id'], message))


PORT=9001
IPADDR="0.0.0.0"
server = WebsocketServer(PORT,IPADDR)
server.set_fn_new_client(new_client) #注册有客户端链接的回调函数
server.set_fn_client_left(client_left)#注册客户端断开的回调函数
server.set_fn_message_received(message_received)#注册消息处理函数
server.run_forever()#程序执行此函数，启动服务器，进入循环阻塞状态，等待被唤醒（被上述注册的三个事件唤醒）
