from os import system
from time import sleep

opcao = 0

valorBebidas = 0
valorLanches = 0
valorSobrimesas = 0

resultadofinal = 0

while opcao != 4:

   	print ( ''' Qual a opção desejada?

    [ 1 ] BEBIDAS
    [ 2 ] LANCHES
    [ 3 ] SOBRIMESAS
  
    [ 4 ] Valor a Pagar
 
    [ 0 ] Enserrar Pedido ''' )

    opcao = int(input(' Qual é a sua opção? '))

System('clear')

    if opcao == 1:
      
			print ( ''' Qual a opção desejada?

			[ 1 ] Suco de Laranja    -  Copo 350 ml  -  R$ 4,00
			[ 2 ] Coca Cola          -  Lata 350 ml  -  R$ 5,50
			[ 3 ] Caldo de Cana      -  Copo 500 ml  -  R$ 5,00
			[ 4 ] Guarana Antartica  -  Lata 350 ml  -  R$ 5,00

			[ 5 ] Retornar a o Manu Principal  ''')

        while opcao == 1:
            bebida = int(input("Escolha uma bebida: "))

            if bebida == 1:
                print("Suco de laranja foi adicionado com sucesso")
                valorBebidas = valorBebidas + 4.00
            elif bebida == 2:
                print("Coca Cola foi adicionado com sucesso")
                valorBebidas = valorBebidas + 5.50
            elif bebida == 3:
                print("Caldo de cana foi adicionado com sucesso")
                valorBebidas = valorBebidas + 5.00
            elif bebida == 4:
                print("Guarana foi adicionado com sucesso")
                valorBebidas = valorBebidas + 5.00
            elif bebida == 5:
                break

    System('clear')

    elif opcao == 2:
        print ( ''' Qual a opção desejada?

			  [ 1 ] X Tudo         -  R$ 6,00
			  [ 2 ] Trio Bomba     -  R$ 10,00
			  [ 3 ] Batata Frita   -  R$ 4,00
			  [ 4 ] Pastel         -  R$ 5,00

			  [ 5 ] Retornar a o Manu Principal ''' )
      

        while opcao == 2:
            lanche = int(input("Escolha seu lanche: ))

            if lanche == 1:
                print("X Tudo foi adicionado com sucesso")
                valorLanches = valorLanches + 6.00
            elif lanche == 2:
                print("Trio Bomba foi adicionado com sucesso")
                valorLanches = valorLanches + 10.00
            elif lanche == 3:
                print("Batata Frita foi adicionado com sucesso")
                valorLanches = valorLanches + 4.00
            elif lanche == 4:
                print("Pastel foi adicionado com sucesso")
                valorLanches = valorLanches + 5.00

            elif lanche == 5:
                break

    System('clear')

    elif opcao == 3:

    	print ( ''' Qual a opção desejada?

			[1] Milk Shake     -  Copo 500ml   -   R$ 9,00
			[2] Casquinha      -      --       -   R$ 2,50
			[3] Pudim          -      --       -   R$ 8,00
		
			[4] Retornar a o Manu Principal 
      
      ''' )
      
        while opcao == 3:
            lanche = int(input("Escolha seu lanche: ))

            if lanche == 1:
                print("Milk Shake foi adicionado com sucesso")
                valorSobrimesas = valorSobrimesas + 9.00
            elif lanche == 2:
                print("Casquinha foi adicionado com sucesso")
                valorSobrimesas = valorSobrimesas + 2.50
            elif lanche == 3:
                print("Pudim foi adicionado com sucesso")
                valorSobrimesas = valorSobrimesas + 8.00
            elif lanche == 4:
                break
      
    System('clear')

    elif opcao == 4:
            resultadofinal = valorBebidas + valorLanches + valorSobrimesas
            print("Valor da conta R${:.2f}".format(resultadofinal))
            sleep(3)

    elif opcao == 0:
        print("O seu pedido foi feito =D")
        break
