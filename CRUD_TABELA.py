import pymysql.cursors

#CONECTANDO AO MYSQL

conex_DB = pymysql.connect(
            host='',
            user='',
            password='',
            port=3306,
            db='',
            cursorclass=pymysql.cursors.DictCursor)

#Habilitando um cursor para executar comandos SQL.
cursor = conex_DB.cursor()



#Função para criar uma TABLE.

def create_table(nome_tabela):

    #Criando uma tabela usando o IF NOT EXISTS pra não dar conflito caso já exista.
    
    try:    
        cursor.execute(f'CREATE TABLE if not exists {nome_tabela}(id int)') 
    
    except Exception as e:
        print(f"Não foi possível criar a tabela {nome_tabela} devido ao ERRO>> {e}")
    
    else:
        print("Tabela CRIADA COM SUCESSO")

#Função para selecionar uma tabela com where(opcional)

def select(fields, tables, where=None):
    
    try:
        with conex_DB.cursor() as cursor:
            query_my = f'SELECT  {fields}  FROM  {tables}'
            
            #Usando o if caso o USER coloque algum filtro vai retornar TRUE e adicionar na QUERY.
            if (where):
                query_my += f' WHERE  {where}'
            
            cursor.execute(query_my)
            print(cursor.fetchall())
    
    except Exception as e:
        print(f'ERRO >> {e}')

#Função para inserir dados em uma table

def insert_dados_table(name_table, n_columns, n_values):
    
    #NAME_TABLE = NOME DA TABELA
    #N_COLUMNS = Colocar os respectivos nomes das colunas.
    #N_VALUES = Colocar os respectivos valores de cada coluna.

    try:
        query_my = f'INSERT INTO {name_table} ({n_columns}) values({n_values})'
        
        cursor.execute(query_my)
        conex_DB.commit()
    
    except Exception as e:
        print(f'Erro {e}')

    else:
        print(f'DADOS INSERIDOS COM SUCESSO.')

#Função para remover uma TABLE.

def remov_table(name_table):
    
    try:
        cursor.execute(f'DROP TABLE {name_table}')
    
    except Exception as e:
        print("OCORREU UM ERRO >>> {e}")
    
    else:
        print('Table excluída com sucesso.')

#função

def update_dados(nome_table, set_col, set_valor, where_col, where_valor):
    
    #NAME_TABLE = Nome da respectiva tabela que quer mudar.
    #Set_COL = Nome da coluna onde vai ter alteração(vai entrar o novo valor).
    #Set_Valor = Valor da coluna onde vai ter alteração(vai entrar o novo valor).

    #Where_col = Nome da coluna onde vai ser alterado(coluna onde que vai ser modificado).
    #Where_valor = Valor da coluna onde vai ser alterado(valor da coluna ond que vai ser modificado).


    try:
        cursor.execute(f'UPDATE {nome_table} SET {set_col} = "{set_valor}" WHERE {where_col} = "{where_valor}"')
        
        conex_DB.commit()
    
    except Exception as e:
        print(f"ERRO >>> {e}")
    
    else:
        print("UPDATE COM SUCESSO.")

#Função para deletar registros de uma TABELA.

def del_register(nome_tabela, where=False, nome_coluna=None, valor_coluna=None):
    
    #O uso do WHERE é opcional, mas é recomendado o uso do MESMO para evitar uma exclusão geral dos registros da TABELA.

    try:
        query_my = f'Delete from {nome_tabela}'
        
        if(where):
            query_my += f'WHERE {nome_coluna} = "{valor_coluna}"'
        
        cursor.execute(query_my)
        conex_DB.commit()
    
    except Exception as e:
        print(f'ERRO>>> {e}')
    
    else:
        print(f'REGISTROS DELETADOS COM SUCESSO.')

#Função para renomear TABELAS.

def renomear_table(name_old, name_new):
    
    try:
        cursor.execute(f'RENAME TABLE {name_old} TO {name_new}')
        conex_DB.commit()
    
    except Exception as e:
        print(f'ERRO>>> {e}')
    
    else:
        print(f"ALTERADO COM SUCESSO. OLD: {name_old} >>>> NEW: {name_new}")

#Função para adicionar colunas em uma TABELA.

def add_column(name_table, new_column, tipo_column, constraints=None):
    
    #Name_Table = Nome da Tabela onde vai ser adicionado a nova coluna.
    #New_Column = Nome da nova COLUNA.
    #Tipo_Column = Colocar o tipo da COLUNA(smallint, int, bigint, varchar(), text, etc)
    #Constraints = Colocar restrições na coluna(NOT NULL, Primary key, Foreign Key, etc )

    try:
        query = f'ALTER TABLE {name_table} ADD {new_column} {tipo_column}'

        if(constraints):
            query += f'{constraints}'
        
        cursor.execute(query)
        conex_DB.commit()
    
    except Exception as e:
        print(f'ERRO >> {e}')
    
    else:
        print(f'COLUNA <{new_column}> ADICIONADA A TABELA <{name_table}> com sucesso.')


conex_DB.close()


