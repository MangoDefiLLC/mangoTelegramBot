const {Telegraf, Markup} = require('telegraf');
require('dotenv').config();
// Create a bot that uses 'polling' to fetch new updates
const bot = new Telegraf(process.env.BOT_API_KEY);

const WEB_APP_URL = process.env.WEB_APP_URL;

const welcome = "Bienvenid@!🎉🎊🕺🏻\n\n🥭MANGO DEFI BOT🤖!\nDonde swapiar token es tan facil como comerse un mango🥭\n\n"
const info = "Mango defi es un Telegram Mini app para facilitar el intercambio de block chain based tokens\n\n"

bot.start( async (ctx) => ctx.reply(
		`${welcome+info}`,
		Markup.inlineKeyboard([Markup.button.webApp("OPEN APP!", WEB_APP_URL)]),
	));

bot.launch();
