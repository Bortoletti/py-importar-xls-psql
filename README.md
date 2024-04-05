# Criar virtual environment
```
python3 -m venv venv

pip list

```
# Ativar o ambiente
```
source venv/bin/activate
```

# instalar lib para acesso ao banco de dados

```
sudo apt install python3-dev libpq-dev

pip install openpyxl

pip install pandas

pip install psycopg2

pip freeze > requirements.txt

```




# Executar importação
```
cd app

python3 main.py ../files/ace-carga.xlsx > ../files/log.txt

```