// require('dotenv').config();
// const telegramAuthToken = process.env.BOT_API_KEY;
const telegramAuthToken = globalThis.BOT_API_KEY;

const webhookEndpoint = "/endpoint";
const WEB_APP_URL = "https://yahdielo.github.io/Mango/";

addEventListener("fetch", (event) => {
  event.respondWith(handleIncomingRequest(event));
});

async function handleIncomingRequest(event) {
  let url = new URL(event.request.url);
  let path = url.pathname;
  let method = event.request.method;
  let workerUrl = `${url.protocol}//${url.host}`;

  if (method === "POST" && path === webhookEndpoint) {
    const update = await event.request.json();
    event.waitUntil(processUpdate(update));
    return new Response("Ok");
  } else if (method === "GET" && path === "/configure-webhook") {
    const url = `https://api.telegram.org/bot${telegramAuthToken}/setWebhook?url=${workerUrl}${webhookEndpoint}`;

    const response = await fetch(url);

    if (response.ok) {
      return new Response("Webhook set successfully", { status: 200 });
    } else {
      return new Response("Failed to set webhook", { status: response.status });
    }
  } else {
    return new Response("Not found", { status: 404 });
  }
}

async function processUpdate(update) {
  if ("message" in update) {
    const chatId = update.message.chat.id;
    const userText = update.message.text;

    if (userText === "/start") {
      const welcomeMessage = "Bienvenid@!🎉🎊🕺🏻\n\n🥭MANGO DEFI BOT🤖!\nDonde swapiar token es tan facil como comerse un mango🥭\n\n"
      const welcomeSubMessage = "Mango defi es un Telegram Mini app para facilitar el intercambio de block chain based tokens\n\n"
      const inlineKeyboard = JSON.stringify({
        inline_keyboard: [
          [
            {
              text: "OPEN APP!",
              web_app: { url: WEB_APP_URL },
            },
          ],
        ],
      });
      const url = `https://api.telegram.org/bot${telegramAuthToken}/sendMessage`;
      const body = {
        chat_id: chatId,
        text: `${ welcomeMessage + welcomeSubMessage }`,
        reply_markup: inlineKeyboard,
      };

      await fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
      });
    } else {
      const responseText = `Command <${userText}> not found\n`;
      const url = `https://api.telegram.org/bot${telegramAuthToken}/sendMessage?chat_id=${chatId}&text=${encodeURIComponent(
        responseText
      )}`;
      await fetch(url);
    }
  }
}
