# processamento-biometria-digital
Projeto de Processamento de Biometrias

Todos os post podem ser feito com o Postman/Insomnia no formato form-data.

Requerimentos:
    - Instalar Postman
    - rodar o comando pip install -r requirements.txt para instalar todas depedências do projeto.
    - rodar o arquivo server.py - python server.py

1 - Cadastro de Biometria

Enviar uma biometria com o nome, email e level e o arquivo file.
    nome: Paulo
    email: professor@gmail.com
    level: 01
    file: photo.png
enviar um post para rota: http://127.0.0.1:5000/uploader

    Aqui o professor pode enviar o formulário com campos faltantes para perceber que a API retornará uma reposta negativa e não salavará a foto.

2 - Comparação de Biometria

Enviar a biometria a ser comparada com email e a foto da biometria.
    email: professor@gmail.com
    file: photo.png
enviar um post para rota: http://127.0.0.1:5000/compare

        Aqui nesta parte o professor poderá enviar alguma foto de outra biometria para comparar que a resposta irá ser negativa

3 - Alterar Biometria

    Enviar a biometria que irá ser alterada e o email para que identificaçãoda biometria
    email: professor@gmail.com
    file: photo.png
enviar um post para rota: http://127.0.0.1:5000/edit

    Aqui o professor também poderá enviar um e-mail que não foi cadastrado para ter a resposta negativa quando mandar alguma digital que o e-mail não existe.

