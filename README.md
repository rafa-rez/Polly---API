<h1 align="center">Título</h1>

![Logo](https://s3.sa-east-1.amazonaws.com/remotar-assets-prod/company-profile-covers/cl7god9gt00lx04wg4p2a93zt.jpg)

## 📌 Índice
 
- [Descrição do Projeto](#-Descrição-do-Projeto)
- [Desenvolvimento e escolha do tema](#-Desenvolvimento-e-escolha-do-tema)
- [Intents utilizadas](#-Intents-utilizadas)
- [Estrutura de pastas](#-Estrutura-de-pastas)
- [Arquitetura AWS](#-Arquitetura-AWS)
- [Como usar o sistema](#-Como-usar-o-sistema)
- [Experiências obtidas](#-Experiências-obtidas)
- [Tecnologias utilizadas](#-Tecnologias-utilizadas)
- [Dificuldades encontradas](#-Dificuldades-encontradas)
- [Autores](#-Autores)

## 📖 Descrição do Projeto
Construir um chat bot com o Amazon Lex V2 e fazer o deploy em uma plataforma de mensageria.

## 🎯 Desenvolvimento e escolha do tema

## ✔️ Intents utilizadas
- <strong>WelcomeIntent</strong>: Intent inicial, apresentação do bot e das opções disponíveis "Vagas", "Canais de comunicação", "Sobre Nós".
- <strong>AboutUsIntent</strong>: Fornece mais informações sobre a empresa Compass.
- <strong>CommunicationChannelsIntent</strong>: Redes sociais e canais de comunicação para contato com a Compass.
- <strong>JobsIntent</strong>: Intent de vagas do nosso chat bot que possibilita as ações "Consultar vagas", "Candidatar-se em uma vaga" e "Consultar aplicações".
    - <strong>ConsultJobIntent</strong>: Intent para consultar vagas disponíveis de acordo com as tags do departamento: "Fullstack Web Apps", "AI & ML", "Business Management", "Marketing".
    - <strong>RegisterJobIntent</strong>: Intent para cadastrar-se em uma vaga.
    - <strong>CheckIntent</strong>: Mostra as vagas que determinado usuário se cadastrou filtrando por nome e sobrenome.
- <strong>ConverToAudioIntent</strong>: Faz a conversão de escrita para áudio.
- <strong>FallbackIntent</strong>: Tratamento de erros.
- <strong>CancelIntent</strong>: Cancelar um intent/reiniciar o bot.

## 📂 Estrutura de pastas
 
```bash
api-tts/                                          # 
├─ .serveless/                                    # 
├─├─ api-tts.zip                                  # 
├─├─ cloudformation-template-create-slack.json    # 
├─├─ cloudformation-template-update-stack.json    # 
├─├─ meta.json                                    # 
├─├─ serverless-state.json                        # 
├─ scripts/                                       # 
├─├─ polly.py                                     # 
├─ README.md                                      # 
├─ gitignore.txt                                  # 
├─ handler.py                                     # 
├─ serveless.yml                                  #
assets/                                           # 
chatbot/                                          # 
├─ CompassUolBot.zip                              # 
.gitignore                                        # 
package-lock.json                                 # 
package.json                                      # 
README.md
```

## 🏗️ Arquitetura AWS
![Imagem|Diagrama](assets/sprints6-7.jpg)

## 🚀 Como usar o sistema

## 🏆 Experiências obtidas

## 💻 Tecnologias utilizadas

## 🛠️ Dificuldades encontradas
1. <strong>Integração do Lambda com o Amazon Lex</strong>:
Enfrentamos várias dificuldades com a integração. Desde compreender que o bot precisa apenas chamar uma função Lambda para gerenciar todas as outras, até sua implementação. Tivemos dificuldades em estabelecer a conexão devido a repetidos erros de permissão que impediram o progresso.
    - Tínhamos várias ideias para integrar o Lambda com o Lex e explorar diversas funcionalidades adicionais, porém, devido ao tempo necessário para resolver a integração, não conseguimos implementar todas as propostas.
2. <strong>Funcionalidades no Lex vs Slack</strong>:
Enfrentamos um desafio ao perceber que algumas funcionalidades testadas exclusivamente no Lex não continuavam operacionais ao serem implementadas no Slack. Por exemplo, um botão que ainda funcionava no Lex após ser selecionado não operava corretamente no Slack.

## ✍🏻 Autores
| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/120669342?v=4" width=115><br><sub>José Acerbi Almeida Neto</sub>](https://github.com/JoseJaan) | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/142454135?v=4" width=115><br><sub>Lívia Marques Rodrigues</sub>](https://github.com/livmrqs) | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/137515142?v=4" width=115><br><sub>Rafael Alves Silva Rezende</sub>](https://github.com/rafa-rez) | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/123120658?v=4" width=115><br><sub>Samuel de Oliveira Vanoni</sub>](https://github.com/SamuVanoni)
| :---: | :---: | :---: | :---: |
