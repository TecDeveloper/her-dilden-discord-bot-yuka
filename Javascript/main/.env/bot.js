const discordjs = require("discord.js")
const c = new discordjs.Client();

c.on('ready', () => {
  console.log(`Giriş yaptım.`);
});

c.on('message', msg => {
  if (msg.content === 'Sa') {
    msg.reply('As');
  }
});

c.login(process.env.TOKEN);
