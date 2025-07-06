# # MVP - Simulador de Aprovação de Empréstimo com Machine Learning

Sprint: Qualidade de Software, Segurança e Sistemas Inteligentes

Aluno: Victor Magno Thuler Pereira



MVP Full Stack de um sistema bancário simples que prevê a aprovação ou recusa de um empréstimo com base no perfil do cliente, utilizando modelos de machine learning.

---

## Modelo de Machine Learning

O modelo foi treinado no Google Colab com um dataset público de crédito, seguindo as exigências do MVP:

- Carga do dataset via URL
- Limpeza e transformação de dados
- Separação entre treino e teste (holdout)
- Modelagem com KNN, Árvore de Decisão, Naive Bayes e SVM
- Criação de pipelines
- Cross-validation
- Otimização de hiperparâmetros
- Avaliação de métricas (precision, recall, f1-score)


**Notebook Colab:**  
Encontra-se no Git com o nome de arquivo "notebook_emprestimo_mvp.ipynb", é possível também acessar diretamente pelo Colab por [aqui](https://colab.research.google.com/drive/1hqkBqEhNJEhgsjA68--mg4wBKSfP4e9W?usp=sharing).

---

## Estrutura do Projeto
```
MVP_Emprestimo/
├── back_end/
│ ├── app.py
│ ├── test_modelo.py
│ ├── requirements.txt
│ └── modelo/
│ ├── modelo_treinado.pkl
│ └── dados_teste.csv
└── front_end/
├── index.html
├── script.js
└── style.css
```

##Como Rodar o Projeto:

### 1. Back-End (Flask)
```bash
cd back_end
python -m venv venv
# Ative o ambiente virtual:
# Windows:
venv\Scripts\activate

# Instale as dependências:
pip install -r requirements.txt

# Execute o servidor Flask:
python app.py
```

### 2. Front-End
### 1. Rodar o Front-End

Não é necessário servidor. Basta abrir o arquivo `index.html` no navegador:

OBS: O back-end deve estar rodando para que seja possível criar registros no front-end.

```bash
cd ../front
start index.html  # (Windows)
# ou
open index.html   # (macOS)
```

Também pode abrir o arquivo manualmente clicando duas vezes em `index.html`.

### 3. Teste Automatizado (PyTest)
```bash
cd back_end
pytest test_modelo.py
```

