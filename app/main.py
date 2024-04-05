import sys
import csv
import psycopg2
import pandas as pd

#
# CARREGAR E PROCESSAR LIGAÇÕES
#======================================================================
def importar( fileToReadParam ):
  # Ler o arquivo Excel
  # dataframe = pd.read_excel('/home/luis/usr/py/py-importar-xls-psql/files/ace-carga.xlsx')
  dataframe = pd.read_excel(  fileToReadParam )

  # Exibir os dados
  #print( dataframe )

  for linha in dataframe.columns :
    print( linha )
    
  for linha in dataframe.values :
    print( linha[0] )
    # print( linha )
    sql = f"""INSERT INTO tabela(
      origem, destino
    , start_time, start_time_local
    , answer_time, answer_time_local
    , end_time, end_time_local
    , duration, disposition
    , direction
    , inicio_dt, inicio_hr
    , termino_dt
    , termino_hr
    , st_ligacao )
    VALUES(
      '{linha[0]}', '{linha[1]}'
      ,'{linha[2]}', '{linha[3]}'
      ,'{linha[4]}', '{linha[5]}'
      ,'{linha[6]}', '{linha[7]}'
      ,'{linha[8]}', '{linha[9]}'
      ,'{linha[10]}'
      , '{linha[3]}'::date, replace( split_part( '{linha[3]}', 'T', 2) , ' BR','' )::time   
      , '{linha[7]}'::date, replace( split_part( '{linha[7]}', 'T', 2) , ' BR','' )::time   
      , 'ATUALIZAR-zzzzz'
      );
    """
    print(sql)
    

    try:
      cmd = conn.cursor()
      #cmd.execute( sql )
      #conn.commit()
    except Exception as err:
      print( sql )
      print( err )
    finally:
      conn.rollback()

#
# ATUALIZAR
#======================================================================
def atualizar( fileToReadParam ):
  sql = f"""
  update tabela set 
    st_ligacao =  'ATUALIZADA'
    ,id_oportunidade = (
       select max( o.id_oportunidade )
       from tabela o
       where replace(replace( replace( replace( o.fone, '-', ''), '(',''), ')',''),' ','') = crm_ligacao.destino )
  where st_ligacao =  'ATUALIZAR-zzzzzz'
  """

  try:
    cmd = conn.cursor()
    cmd.execute( sql )
    conn.commit()
  except Exception as err:
    print( sql )
    print( err )
  finally:
    conn.rollback()


#
# processo principal
#======================================================================
print("Inicio")

conn = psycopg2.connect( host="", database="", user="" , password=""  )
fileToRead = ""

if( len( sys.argv ) < 2 ):
   print("*** FALHA: informe o arquivo CSV em ../file");

if( len( sys.argv ) == 2 ):
  print( sys.argv[1] )
  fileToRead = sys.argv[1]
  importar( fileToRead )
  # atualizar( fileToRead )

print("Fim")
