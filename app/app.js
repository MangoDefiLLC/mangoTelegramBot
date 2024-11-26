const {Telegraf, Markup} = require('telegraf');
require('dotenv').config();
// Create a bot that uses 'polling' to fetch new updates
const bot = new Telegraf(process.env.BOT_API_KEY);

const WEB_APP_URL = process.env.WEB_APP_URL;
//const provider = process.env.BASE_RPC;
//const serverEndpoint = 'http://localhost:1000'; 
//const botResp = new Actions(serverEndpoint,provider)//http://127.0.0.1:9000/
//const WEB_APP_URL = "https://t.me/mangoDefiBot/Mango";
const welcome = "Bienvenid@!🎉🎊🕺🏻\n\n🥭MANGO DEFI BOT🤖!\nDonde swapiar token es tan facil como comerse un mango🥭\n\n"
const info = "Mango defi es un Telegram Mini app para facilitar el intercambio de block chain based tokens\n\n"
bot.start( async (ctx) => ctx.reply(
		`${welcome+info}`,
		Markup.inlineKeyboard([Markup.button.webApp("OPEN APP!", WEB_APP_URL)]),
	));

bot.launch();
/** 
// Handle callback queries
bot.on('callback_query', async function onCallbackQuery(callbackQuery) {
  let lote = { 10:'10',100:'100',1000:'1000'}
  console.log('this is the query',callbackQuery.message.chat.id)

  let chatId = callbackQuery.message.chat.id
  let amount = callbackQuery.data;
  let text = callbackQuery.message.text
  let index = text.indexOf('0')
  let tokenAddress =  text.slice(index,60)

  if(amount in lote){
   console.log('im in',lote[`${amount}`])
   let dLink = await botResp.getDeepLink(lote[`${amount}`],tokenAddress)
   console.log(dLink)
   let resp = botResp.deepLinkresp()
   bot.sendMessage(chatId,dLink.deepLink,resp)
  }
});


bot.command("/app", ctx =>
  reply(
    "Launch mini app from keyboard!",
    Markup.keyboard([Markup.button.webApp("Launch", WEB_APP_URL)]).resize()
  ));

// Listen for any kind of message. There are different kinds of
// messages.
/**
bot.on('message', async (msg) => {
  const chatId = msg.chat.id;
  let userMsg = msg.text

  //handle token address msg
  if(userMsg.length == 42){
    let hex = userMsg.slice(0,2)

    //if string doest start with 0x return msg
    if(!hex == '0x'){
      bot.sendMessage(  
        chatId, 
        'Su mensaje no es un Address valido!\n\nPara mas info 👉🏽 /info'
        )
    }
    //if is an address the call the resposne from botResp
    let resp = await botResp.addressResp(userMsg)
    //console.log(resp)
    bot.sendMessage(chatId, resp.msg, resp.button)
  }
  if (!userMsg.startsWith('/')){
  
    //handle if User msg is not an address
    if(userMsg.length != 42){
      bot.sendMessage(chatId, 'Para mas info toca eso 👉🏽 /info')
    }
  }
 
});

 */