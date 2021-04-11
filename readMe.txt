To run this server:
1. Ngrok:-Using ngrok, it gives unique URL to run our server for 2 hr.
2. This URL is ued in webhook to generate an event
3. The "Action-repo" is linked with server code.
4. Whatever action perform on the git repo, it trigger an event and get stored in the database.
5. For checking GET & POST call status/action I have used Postman.
6. Also using GET call it is possible to access data from database
7. I have used ngrok,so the URL for run the server is just valid for 2 hr.So to check code execution,generate the link from ngrok,paste it to postman's URL field then /event or /github-webhook eg( https://3c57486a75ba.ngrok.io/events) 
8. Also paste to the "Action-repo's" webhook and /github.webhook eg.(https://3c57486a75ba.ngrok.io/github-webhook)
 