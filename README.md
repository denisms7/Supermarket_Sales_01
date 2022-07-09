# Supermarket Sales v01
## 🚀 Aplicação de Análise de Dados
Dashboard web interativo de análise de vendas para dispositivos moveis e computadores

![vendas](https://user-images.githubusercontent.com/82631808/178117148-46acf8ec-dd49-47f0-8a6c-9a8a4a20afb4.png)

## 📦 Configuração

### 📋 Pré-requisitos

Crie um ambiente virtual conforme o arquivo de [requerimentos](https://github.com/denisms7/Supermarket_Sales_01/blob/main/requirements.txt)


### 🔧 Instalação

Após a configuração do ambiente virtual basta executar o arquivo app.py e a aplicação estará on-line no link: http://127.0.0.1 não sendo necessário informar a porta pois o mesmo está sendo disponibilizado na porta 80 do servidor, esta porta pode ser alterada na variável port= localizada ao final do arquivo app.py

````
if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=80, debug=False)
````


## 📦 Desenvolvimento

Este e um projeto desenvolvido com embase em Flask então para implementação da aplicação em produção recomendamos utilizar a documentação do próprio Flask: [Deploying to Production](https://flask.palletsprojects.com/en/2.1.x/deploying/)


## 🛠️ Construído com

* [Python](https://www.python.org/) - Linguagem matriz utilizada
* [Dash](https://plotly.com/dash/) - Framework web daseado em [Flask](https://flask.palletsprojects.com/en/2.1.x/)
* [Plotly](https://plotly.com/python/) - Usado para gerar os Graficos
* [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/) - Framework CSS usado


## ✒️ Autores

* **Desenvolvedor** - *Denis Muniz Silva* - [Denis Muniz Silva](https://github.com/denisms7)


## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE.md](https://github.com/denisms7/Supermarket_Sales_01/blob/main/LICENSE) para detalhes.
