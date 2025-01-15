# Projeto de Transcrição de Vídeos do YouTube

Este projeto permite baixar o áudio de vídeos do YouTube, converter para o formato WAV e transcrever o áudio usando a biblioteca `SpeechRecognition` e o serviço de reconhecimento de voz do Google. A interface gráfica é construída usando `PyQt5`.

## Funcionalidades

- Baixar o áudio de vídeos do YouTube
- Converter o áudio para o formato WAV
- Transcrever o áudio para texto
- Exibir o progresso do processamento
- Exibir a transcrição do áudio na interface gráfica

## Requisitos

- Python 3.x
- PyQt5
- pytubefix
- ffmpeg
- SpeechRecognition
- pydub

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/Raphael2203/TranscriptionForIA
   cd TranscriptionForIA
   
Crie um ambiente virtual e ative-o:

bash
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
.\venv\Scripts\activate  # Para Windows

Instale as dependências:

bash
pip install -r requirements.txt
Certifique-se de ter o ffmpeg instalado em seu sistema. Você pode baixar e instalar o ffmpeg a partir de ffmpeg.org.

Uso
Execute a aplicação:

bash
python transcription_gui.py
Insira a URL do vídeo do YouTube na interface gráfica.

Clique no botão "Processar Agora!".

A transcrição do áudio será exibida na interface gráfica.

Estrutura do Projeto
plaintext
.
├── transcription_logic.py  # Lógica principal para baixar, converter e transcrever o áudio
├── transcription_gui.py    # Interface gráfica construída com PyQt5
├── README.md               # Este arquivo
└── requirements.txt        # Arquivo de dependências

Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.
