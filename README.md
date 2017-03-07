# Alex_Chatbot
Alex Chatbot é um experimento conduzido ao longo de 3 meses na tentativa de criar um bot de conversação em linguaguem natural usando dados de um grupo do Telegram.

A primeira etapa do desenvolvimento consistiu em obter acesso as mensagens digitadas em um grupo do Telegram. Após receber aval de um dos adminstradores do grupo, foi criado um bot spy para coletar qualquer mensagem digitada durante o período de 3 meses. No final do período de coleta, 21018 mensagens foram armazenadas na base de dados. 

#### Metodologia de treino
A API do Telegram fornece metadados que possibilitam distinguir quem emite a mensagem e se a mensagem é um 'reply' para outra mensagem no chat. Para esse experimento foram utilizadas somente as mensagens que respondem outra dentro do chat. Desse modo consegue-se obter uma estrutura lógica e básica de fluxo de diálogo: pergunta e resposta ou objeto e explicação do objeto. A fim de filtrar as mensagens que compreendessem esse fluxo na massa de treino, o escopo de restrigiu-se em 11487 mensagens. Exemplo de um fluxo de diálogo retirado do Telegram:   

[![N|Solid](http://i.imgur.com/c7ND1O9.png)](https://nodesource.com/products/nsolid)

#### Tecnologias Utilizadas
Infraestrutura
* Mysql (Armazenamento das mensagens)
* Mongodb (Persistência das mensagens já treiandas do bot)
* Docker (Facilitar o start up da infra)
* Python (Linguagem para implementação do bot)
* Node.js (Linguagem para o bot coletor de mensagens)

Bibliotecas
* ChatterBot: Biblioteca que implementa os conceitos básicos de chatbots usando Natural Processing Language (NPL)

#### Treino
O bot foi treinado em três etapas. A primeira consistiu-se em instalar um apanhado de fluxos de diálogos que são disponibilizados pela comunidade que mantém o as bibliotecas que NPL. A segunda etapa foi criar um 'preset' estático sobre informações de quem fez o bot. A terceira etapa foi injetar a base de dados coletada pelo bot spy na engine de conversação. 
Após ter todos os bancos de dados configurados, a engine de conversação treina com o único comando: 

``` shell
python main.py learn
>>
[u'Pq eu detestava de andar de dia', u'Rt']
[u'Quantos ismos', u'Muitos mesmo kkkkk']
[u'Tu acha que vou conferir? ? Passei foi longe', u'Poxa']
[u'E era o que', u'Tu acha que vou conferir? ? Passei foi longe']
```

#### Testes
A motivo de protótipo, os testes foram executados apenas via command line. 

###### Conversando com o bot com o preset estático de treino
O 'preset' estático refere-se as três perguntas e respostas abaixo: 
```python
'Quem te programou?' -> 'Allyson Maciel'
'Quem é o seu mestre?'-> 'Allyson Maciel'
'Em qual linguagem você é escrito?' -> 'Fui escrito em Python e você?'
```

Quando as mensagens são digitadas exatamente como no conjunto de treino, o bot responde o resultado com alto grau de confiança. Nota-se que a segunda mensagem do User tem erros de ortografia e uma estrutura sintática diferente do conjunto de treino. Isso é possível pelo fato que os algoritmos de NPL executarem um matching com o parâmetro enviado pelo usuário e o 'target' no banco de dados. Dessa forma o bot interpreta uma intenção de diálogo de várias formas com apenas um 'input' de treino. 
```shell
User - Quem é o seu mestre?
Bot - Allyson Maciel
User - Qual lingueguem de programação você é escrito?
Bot - Fui escrito em Python e você?
```

Já em uma conversação livre, ou seja, utilizado o corpo de treino coletado no Telegram, as conversas se tornam bem instáveis. Isso ocorre porque muitas respostas dadas as mensagens em um chat dependerem muito do contexto da conversa. No entanto, algumas mensagens que tem o escopo genérico performam bem com essa técnica. 
``` shell
User - Oi
Bot - Olá
User - O que você tá fazendo de bom?
Bot - Nada.
User - Não quer fazer nada?
Bot - Não veja, c++, é mara
User - Não entendi, kkkkk
Bot - Não eh pra entender �???�???
User - Quer falar sobre o que?
Bot - nem doi tanto, só doi o bigóde
User - Porque você fala de bigode?
Bot - Porque noix é br
User - kkkkkk
Bot - Deliciosa
User - Você é uma má influência
Bot - Vc cortou a cabeleira? �??��??�
User - Não muda de assunto
Bot - Mano que chapéu estranho
```
#### Projetos relacionados
AlexBotSpyTelegram: bot coletor de mensagens.
link: https://github.com/Guepardo/AlexBotSpyTelegram/tree/master

#### Projetos Futuros e em andamento
AlexChatBotWebInterfaceTrain: Interface de treino web inspirada na dashboard do IBM Watson para chatbots. 
link: https://github.com/Guepardo/AlexChatBotWebInterfaceTrain