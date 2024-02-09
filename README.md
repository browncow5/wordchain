# wordchain

```
git clone ...
cd wordsmith
touch .env && echo "DDOG_API_KEY=\"<YOUR API KEY>\"" > .env
```
Make sure docker desktop is up and running
```
docker-compose up --build
```

## How to use
Room manager, click create room to generate a room token, and then Join Room to join that room token's room.
Once in the room, you can use the WebSocket Messages to send messages that will update all other clients who are in the same room. 
The List generator will generate a list of n words that are compound related. FYI this function take ~ 5-20 seconds to run. When it finishes, you will see the list below the submit button.
