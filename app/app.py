from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# instancia um bot
chatbot = ChatBot('UEA.bot',
              storage_adapter='chatterbot.storage.SQLStorageAdapter',
              logic_adapters=[
                  {
                      'import_path': 'protocolo_adapter.ProtocoloLogicAdapter',
                  },
                  {
                      'import_path': 'chatterbot.logic.BestMatch',
                      'default_response': 'Desculpe, mas eu não entendi.',
                      'maximum_similarity_threshold': 0.80
                  }
              ]
              )

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "./data/greeting_corpus/custom.corpus.json",
    "./data/estagio_corpus/custom.corpus.json"
)

app = Flask(__name__)


@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['user_input']
    bot_response = chatbot.get_response(user_input)
    bot_response = str(bot_response)
    return render_template('index.html', user_input=user_input,
                           bot_response=bot_response
                           )

@app.route('/chat', methods=['POST'])
def chatprocess():
    user_input = request.form['user_input']
    bot_response = chatbot.get_response(user_input)
    bot_response = str(bot_response)   
    return jsonify({'status_code': 200, 'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)

