# cali_model_deploy
Roda uma aplicação para estimar o valor de casas usando o dataset california housing com R² igual a 0.61 no conjunto de teste.

Além disso, implementa CI/CD usando Docker com deploy no Heroku

## Lista de softwares usados
1. [Github](https://github.com)
2. [VS Code IDE](https://code.visualstudio.com)
3. [Heroku](https://heroku.com)
4. [Git CLI](https://git-scm.com/book/en/v2)

## Tarefas necessárias
1. Criar um novo ambiente

        conda create -p venv python==3.7 -y

2. Rodar o arquivo txt requirements para instalar as bibliotecas no env

        pip install -r requirements.txt

3. Rodar o app para interagir com o modelo

        python app.py