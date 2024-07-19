<h1 align="center">Título</h1>

![Logo](https://s3.sa-east-1.amazonaws.com/remotar-assets-prod/company-profile-covers/cl7god9gt00lx04wg4p2a93zt.jpg)

## 📌 Índice
 
- [Descrição do Projeto](#-Descrição-do-Projeto)
- [Desenvolvimento e escolha do tema](#-Desenvolvimento-e-escolha-do-tema)
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
.gitignore                                        # 
package-lock.json                                 # 
package.json                                      # 
README.md
```

## 🏗️ Arquitetura do projeto

## 🚀 Como usar o sistema

## 🏆 Experiências obtidas

## 💻 Tecnologias utilizadas

## 🛠️ Dificuldades encontradas
1. <strong>Integração do Lambda com o Amazon Lex</strong>:
Enfrentamos várias dificuldades com a integração. Desde compreender que o bot precisa apenas chamar uma função Lambda para gerenciar todas as outras, até sua implementação. Tivemos dificuldades em estabelecer a conexão devido a repetidos erros de permissão que impediram o progresso.
    - Tínhamos várias ideias para integrar o Lambda com o Lex e explorar diversas funcionalidades adicionais, mas não conseguimos avançar na etapa de vinculação entre eles. Isso inclui cartões de resposta dinâmicos, respostas baseadas nos dados da API, além de salvar e recuperar dados do S3.

## ✍🏻 Autores
| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/120669342?v=4" width=115><br><sub>José Acerbi Almeida Neto</sub>](https://github.com/JoseJaan) | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/142454135?v=4" width=115><br><sub>Lívia Marques Rodrigues</sub>](https://github.com/livmrqs) | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/137515142?v=4" width=115><br><sub>Rafael Alves Silva Rezende</sub>](https://github.com/rafa-rez) | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/123120658?v=4" width=115><br><sub>Samuel de Oliveira Vanoni</sub>](https://github.com/SamuVanoni)
| :---: | :---: | :---: | :---: |
