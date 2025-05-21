# Dashboard Plafonds

Este projeto é um dashboard comparativo de plafonds que permite aos usuários carregar arquivos CSV, ler faturas, acessar dados de mercado e visualizar resultados de comparações.

## Estrutura do Projeto

```
dashboard-plafonds
├── src
│   ├── app.py                # Ponto de entrada da aplicação
│   ├── pages
│   │   ├── home.py           # Página inicial do dashboard
│   │   ├── upload.py         # Página para upload de arquivos CSV
│   │   ├── leitura_faturas.py # Leitura de dados de faturas
│   │   ├── dados_mercado.py  # Dados de mercado de plafonds
│   │   ├── comparacao.py     # Lógica de comparação de plafonds
│   │   └── resultados.py      # Exibição dos resultados das comparações
│   ├── components
│   │   └── __init__.py       # Inicialização do pacote de componentes
│   └── utils
│       └── file_reader.py     # Funções utilitárias para leitura de CSV
├── requirements.txt           # Dependências do projeto
└── README.md                  # Documentação do projeto
```

## Instalação

1. Clone o repositório:
   ```
   git clone <URL_DO_REPOSITORIO>
   cd dashboard-plafonds
   ```

2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

## Uso

Para iniciar o dashboard, execute o seguinte comando:
```
python src/app.py
```

Acesse o dashboard em seu navegador através de `http://localhost:5000`.

## Funcionalidades

- **Página Inicial**: Uma visão geral do dashboard com links de navegação.
- **Upload de Arquivos**: Permite que os usuários carreguem arquivos CSV para análise.
- **Leitura de Faturas**: Processa os dados das faturas carregadas.
- **Dados de Mercado**: Exibe informações relevantes sobre plafonds.
- **Comparação**: Realiza comparações entre os dados das faturas e os dados de mercado.
- **Resultados**: Apresenta os resultados das comparações de forma clara e visual.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.