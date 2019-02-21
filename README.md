# Projeto Django Transferências

## API Documentação

### Documentação (interação com a API via dashboard):
-   Menu lateral contém navegação da api/endpoints.
https://nixt.herokuapp.com/


### Para interagir com a api, basta ir em: 
Menu lateral > Authentication > Token e preencher Schema: Token, Token: 99116a9dba35b9010026c59ffdd973710d95f456
Feito isso será salvo headers necessários para autenticação e utilização da api


### Recursos:
-   Transferencias
-   Usuarios
-   Auth


### Login Admin: 
-   Url admin: https://nixt.herokuapp.com/admin 
-   username: admin
-   email: admin@admin.com
-   password: admin257



### Authenticação para API:
Authorization: Token token_do_usuario

```bash 
curl -X GET https://nixt.herokuapp.com/api/v1/transferencias/ -H 'Authorization: Token 99116a9dba35b9010026c59ffdd973710d95f456'
```


# IMPORTANTE
## endpoint GET /api/v1/transferencias/  - Lista Transferências

Filtros disponíveis enviados por query_string

Todos os valores são opcionais e quando informados são aplicados ao filtro

### Requisição:

-   @data_inicio : data de inicio no formato YYYY-MM-DD
-   @data_final : data final no formato YYYY-MM-DD
-   @pagador : Nome do pagador
-   @beneficiario: Nome do beneficiária
```bash 
curl -H "Accept: application/json" -H "Content-type: application/json" -X  GET https://nixt.herokuapp.com/api/v1/transferencias/?data_inicio=2019-02-20&data_final=2019-02-25&pagador=Rafael%20Salles&beneficiario=Rafael -H 'Authorization: Token 99116a9dba35b9010026c59ffdd973710d95f456'
```


### Resposta
```json
    {
        "count":0, // total transferências retornados
        "next":null, // url próxima página
        "previous":null, // url página anterior
        "results":[], // array de transferências
        "somatorio":0 // somátoria de valor transfêrido
    }
```




## Setup Local

### Requisitos
-   pipenv https://github.com/pypa/pipenv
-   postgresql

### Passo a passo
1) Clonar repositório git clone git@github.com:rcsalles/nixt.git
2) Criar virtualenv:  pipenv shell
3) Instalar dependências: pipenv install
4) Copiar/Renomear sample.env para .env
5) Editar .env e definir DATABASE_URL para banco local ou remoto
6) Rodar migração para banco (bando já deve ter sido criado):  python manage.py migrate
7) Criar super usuário: python manage.py createsuperuser
8) Rodar servidor: python manage.py runserver 
9) Acessar http://127.0.0.1:8000/

### Comandos Console
```bash
$ git clone git@github.com:rcsalles/nixt.git
$ cd nixt
$ pipenv shell
$ pipenv install
$ cp sample.env .env
$ # alterar .env e definir DATABASE_URL para banco local ou remoto
$ python manage.py migrate
$ # criar admin para sistema
$ python manage.py createsuperuser
$ python manage.py runserver
$
```
