# Como obter o dataset

O dataset **News Category Dataset** não está incluído neste repositório por ser grande (~100MB).

## Passos para baixar

1. Acesse: https://www.kaggle.com/datasets/rmisra/news-category-dataset
2. Faça login no Kaggle (crie uma conta gratuita se necessário)
3. Clique em **Download**
4. Extraia e coloque o arquivo `News_Category_Dataset_v3.json` nesta pasta (`data/`)

## Formato do arquivo

JSON Lines — cada linha é um objeto JSON com os campos:
- `category`: categoria da notícia
- `headline`: manchete
- `authors`: autores
- `link`: URL original
- `short_description`: descrição curta
- `date`: data de publicação
