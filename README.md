# Projeto para a disciplina Projeto Integrador – Análise de Soluções Integradas para Organizações

A aplicação está dividida em dois serviços:
- [Backend](https://pi-analise-solucoes-integradas-production.up.railway.app/): aplicação [Django](http://djangoproject.com) (Python) com API REST criada com [Django Rest Framework (DRF)](https://www.django-rest-framework.org). Instalada na plataforma de infraestrutura em nuvem [Railway](https://railway.com);
- [Frontend](https://pi-analise-solucoes-integradas-orgs.vercel.app/): aplicação web (HTML, CSS e Javascript) construída com [Vite](https://vite.dev). Instalada na plataforma de infraestrutura em nuvem [Vercel](https://vercel.com/).

## Modelo físico do banco de dados

[![image](https://github.com/user-attachments/assets/254f35ee-2a82-48f1-8161-4ccfa275135c)](https://dbdocs.io/embed/b65bef8cf417d931a62afdd5ff6b1ff1/314698636cd94b9e80c1b85e92b34351)

## Tela para o pré-projeto

- [Projeto completo no Figma](https://www.figma.com/design/atLuWZJJmQx8BcZqgy6LPy/AUTISMO_E_APOIO?node-id=55-2&t=UCI3yTqfDXOrEL22-0)

![image](https://github.com/user-attachments/assets/0fcb5821-a26e-4188-bb17-f0b891fe55b8)

![image](https://github.com/user-attachments/assets/bd9b6df5-a099-4537-92fd-0fcd540240b1)

![image](https://github.com/user-attachments/assets/c4521378-18d7-4978-80ab-1b0888178b99)

![image](https://github.com/user-attachments/assets/82a681b4-56a4-4e79-b7ed-f4a370261cd6)

![image](https://github.com/user-attachments/assets/06e28655-fadf-4893-a0fc-c94dd31f4d1d)

![image](https://github.com/user-attachments/assets/e59e1ddd-1fa5-468e-9144-b8cd61122e7f)

## Instalação e configuração

### Configurar repositório 

Clonar o repositório utilizando HTTPS:

```shell
git clone https://github.com/senac-pi-analise-solucoes-integrad-orgs/pi-analise-solucoes-integradas-orgs.git
```
Ou utilizando SSH:
   
```shell
git clone git@github.com:senac-pi-analise-solucoes-integrad-orgs/pi-analise-solucoes-integradas-orgs.git
```

Entrar na pasta do projeto:

```shell
cd pi-analise-solucoes-integradas-orgs
```

### Aplicação Backend

Entrar na pasta da aplicação:

```shell
cd backend
```

#### Configurar ambiente virtual Python

##### Criar ambiente virtual

```shell
python -m venv .venv
```

Caso não funcione com `python`, você pode tentar com `python3`.

##### Entrar no ambiente virtual

```shell
source .venv/bin/activate
```

Caso seu ambiente seja Microsoft Windows, utilize:

```shell
.\.venv\Scripts\activate
```

##### Instalar pacotes necessários

```shell
pip install -r requirements.txt
```

#### Configurar banco de dados 

##### Executar migrate para criar as tabelas

```shell
python manage.py migrate
```

##### Criar Super Usuário

```shell
python manage.py createsuperuser
```

#### Configurar variáveis de ambiente

Fazer uma cópia do arquivo `contrib/env.sample` para `.env`, na raiz do projeto:

```shell
cp contrib/env.sample .env
```

#### Rodar a aplicação

##### Iniciar o servidor

```shell
python manage.py runserver
```

##### Abrir aplicação no navegador

- Acessar aplicação link [http://localhost:8000/](http://localhost:8000/)
- Administração no link [http://localhost:8000/admin/](http://localhost:8000/admin/)

## Instalação e configuração da aplicação Frontend

### Aplicação Frontend

Entrar na pasta da aplicação:

```shell
cd frontend
```

#### Configurar variáveis de ambiente

Fazer uma cópia do arquivo `contrib/env.sample` para `.env`, na raiz do projeto:

```shell
cp contrib/env.sample .env
```

#### Rodar a aplicação

##### Iniciar o servidor de desenvolvimento

```shell
nom run dev
```

##### Abrir aplicação no navegador

- Acessar aplicação link [http://localhost:5173/](http://localhost:5173/)

## Links utilizados durante o desenvolvimento

- [Multipage Vite Vanilla JavaScript](https://dev.to/mochamadboval/multipage-vite-vanilla-javascript-3i0l)
