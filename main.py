import psycopg2

# CONEXÃO COM BANCO DE DADOS 
connection = psycopg2.connect(
  user = "postgres",
  password = "postgres",
  host = "localhost",
  port = "5432",
  database = "teste"
   )
cursor = connection.cursor()

while True :
    print('|--------------SYSTEM----------------|')
    print('| 1-CADASTRAR                        |')
    print('| 2-LISTA                            |')
    print('|------------------------------------|')
    option = int(input('DIGIRE A OPÇÃO ?'))
 
    while option != 5:

     if option == 1:
        try :
            #   INPUTS         
                userName = str(input('NOME  :'))
                userPassword = str(input('SENHA : '))
                userEmail = str(input('EMAIL : '))

                user_insert = f""" INSERT INTO users (id,name,password,email) VALUES (gen_random_uuid(),'{userName}','{userPassword}' , '{userEmail}')"""

            #   EXECUTA SQL
                cursor.execute(user_insert)

            #   COMMIT
                connection.commit()

            #   TOTAL DADOS INSERIDOS
                count = cursor.rowcount
                print ("Usúario cadastrado", count)


        except(Exception, psycopg2.Error) as error:
                print("Error connecting to PostgreSQL database", error)
                connection = None
        
        finally:
             if connection != None:
                cursor.close()
                connection.close()
                print("The PostgreSQL connection is now closed")
        break
     elif option == 2:

        user_select = """ SELECT * FROM users """
        cursor.execute(user_select)
        users =  cursor.fetchall()

        print('|----------------------------------------------------------------------------------|')
        print('|                    CLIENTES CADASTRADOS                                          |')
        print('|----------------------------------------------------------------------------------|\t')
        for i in users:
              print(F'|NOME = {i[1]} ', F'EMAIL = ${i[3]}                                   ')
        
        print('|----------------------------------------------------------------------------------|\t')


        print('| 1-REMOVER  2-ATULIZAR 3- VOLTAR                                                  |')
        print('|--------------------------------------------------------------------------------- |')
        optionuser = int(input('QUAL OPÇÃO :'))
        while optionuser != 3:
          if(optionuser == 1):
            print('Para remover usuário digite o email: ')

            #   INPUTS  
            emailinput = str(input('email : '))

            # VERIFICA SE USÚARIO ESTA CADASTRADO
            user_select = F""" SELECT * FROM users WHERE EMAIL = '{emailinput}' """

             #   EXECUTA SQL
            cursor.execute(user_select)

            users =  cursor.fetchall()
            if(users == []):
                  print('Usuário não encontrado')
                  print('Digite novamente...')
                  break


            user_remove = f""" DELETE FROM users WHERE email = '{emailinput}' """

             #   EXECUTA SQL
            cursor.execute(user_remove)

            connection.commit()

            print('Usuário removido com sucesso!')
            break

          elif(optionuser == 2):
              print('Digite email do usuário cadastrado que deseja atualizar!')
              user_email = str(input('email : '))
              print('|--------------------------------------------------------------------------------- |')

            # VERIFICA SE USÚARIO ESTA CADASTRADO
              user_select = F""" SELECT * FROM users WHERE EMAIL = '{user_email}' """
              cursor.execute(user_select)
              users =  cursor.fetchall()
              if(users == []):
                  print('Usuário não encontrado')
                  print('Digite novamente...')
                  break

              print('|--------------------------------------------------------------------------------- |')
              print(' Digite os dados para serem atualizados!')
              #   INPUTS  
              nome = str(input(f' nome : '))
              senha = str(input(f' senha : ' ))
              email = str(input(f' email : '))
              print('|--------------------------------------------------------------------------------- |')

              user_update = f""" 
                             UPDATE users 
                             SET name = '{nome}',password = '{senha}',email = '{email}'
                             WHERE email = '{user_email}' 
                             """
              #   EXECUTA SQL
              cursor.execute(user_update)
              #   COMMIT
              connection.commit()
              print('dados atualizado')
              break  

        break
