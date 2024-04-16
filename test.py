from pyrogram import Client, types, raw

app = Client(
	"test",
	api_id=27266895,
	api_hash="4015058704fd15571c74e0193091f9aa",
	bot_token="5891498468:AAFx3jPx2DK0EzwGkY47DUodV44Z6ZE14aI"
)

@app.on_delete_messages()
async def OnMessage(client: Client, message: types.Message):
	print(message)

app.run()
