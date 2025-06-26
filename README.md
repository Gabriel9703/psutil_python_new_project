# Monitoring System

Este projeto tem como objetivo monitorar informações do sistema e hardware utilizando a biblioteca **psutil**, armazenar logs em um banco de dados **MySQL**, e disponibilizar um dashboard interativo com **Streamlit**. Todo o ambiente é containerizado utilizando **Docker**.

## Funcionalidades

- Coleta de métricas do sistema (CPU, memória, disco, rede, etc) via `psutil`
- Armazenamento dos logs em um banco de dados MySQL
- Dashboard web para visualização dos dados em tempo real com Streamlit
- Deploy facilitado com Docker

## Estrutura do Projeto

```
monitoring-system/
├── collector/         # Scripts de coleta de dados
├── dashboard/         # Aplicação Streamlit
├── docker-compose.yml # Orquestração dos containers
├── README.md
```

## Como executar

1. **Clone o repositório:**
    ```bash
    git clone https://github.com/Gabriel9703/psutil_python_new_project.git
    cd moniroring-system
    ```


2. **Suba os containers:**
    ```bash
    docker-compose up --build
    ```

3. **Acesse o dashboard:**
    - Abra o navegador em `http://localhost:8501`

## Tecnologias

- [psutil](https://psutil.readthedocs.io/)
- [MySQL](https://www.mysql.com/)
- [Streamlit](https://streamlit.io/)
- [Docker](https://www.docker.com/)

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto está licenciado sob a licença MIT.
