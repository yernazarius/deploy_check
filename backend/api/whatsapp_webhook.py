from fastapi import FastAPI, Request, status, APIRouter
from fastapi.responses import JSONResponse, PlainTextResponse
from config import WHATSAPP_TOKEN, VERIFY_TOKEN
import httpx
import os

router = APIRouter()


@router.get("/")
async def root():
    return PlainTextResponse("Simple Whatsrouter Webhook tester. There is no front-end, see main.py for implementation!")

@router.get("/webhook")
async def verify_webhook(mode: str, token: str, challenge: str):
    if mode == 'subscribe' and token == VERIFY_TOKEN:
        return PlainTextResponse(content=challenge)
    else:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": "Invalid token"})

@router.post("/webhook")
async def handle_webhook(request: Request):
    body = await request.json()
    print('Incoming webhook:', body)

    if body.get("object") == "whatsapp":
        entry = body.get("entry", [])
        for en in entry:
            changes = en.get("changes", [])
            for change in changes:
                message = change.get("value").get("messages", [])[0]
                phone_number_id = change.get("value").get("metadata").get("phone_number_id")
                from_number = message.get("from")
                msg_body = message.get("text", {}).get("body", "")
                
                # Echo the received message back to the sender
                async with httpx.AsyncClient() as client:
                    await client.post(
                        f"https://graph.facebook.com/v12.0/{phone_number_id}/messages?access_token={WHATSAPP_TOKEN}",
                        json={
                            "messaging_product": "whatsapp",
                            "to": from_number,
                            "text": {"body": f"Ack: {msg_body}"}
                        },
                        headers={"Content-Type": "application/json"},
                    )
        return JSONResponse(status_code=status.HTTP_200_OK)
    else:
        # Not from Whatsrouter API
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND)
