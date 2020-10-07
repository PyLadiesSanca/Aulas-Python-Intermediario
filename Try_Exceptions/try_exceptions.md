Este arquivo apresenta informações básicas para ajudar você a tratar erros e exceções no seu programa, essencialmente como depurar o seu programa. Este texto é uma referência direta ao cápitulo 11 do livro *Automate The Boring Stuff*(sem tradução para o português) que pode ser acessado nesse [link](https://automatetheboringstuff.com/2e/chapter11/), contendo o conteúdo completo e com mais exemplos.

#Tratamento de erros
Agora que estamos escrevendo programas mais complicados, é muito comum nos depararmos com erros ou bugs, quando isso acontece o compilador irá emitir uma mensagem de erro, porém as vezes o erro é um erro de lógica e dificilmente será identificado pelo compilador da forma correta. Como por exemplo, por que essa variável esta tendo esse valor ou por que o meu programa não executa tal bloco.
Em cassos como esse, é necessário depurar o programa.

Cuidado com o que você pede, o seu computador só vai fazer o que você manda-lo fazer, não vai ler a sua mente e fazer o que você **pretendeu** fazer. Mesmo programadoras profissionais criam bugs o tempo todo, não se sinta desencorajada se o seu programa estiver com problemas.

Felizmente existem ferramentas e técnicas para identificar examatamente o que o seu programa esta fazendo e o que está acontecendo de errado.

##Tratar exceções
Até o momento, ao encontrar um erro ou *exception* o seu programa inteiro para. Ao invés disso, que tal se o seu programa detectasse erros, lidasse com eles e então continuasse executando ?
Python ergue uma exceção(raise an ecpection) ou erro, sempre que tentar executar um código inválido, erros de sintaxe por exemplo. Erros esperados podem ser manipulados com *try* and *except* statements. O código que possivelmente contém  um erro entra no bloco try. O programa executa o bloco *except* caso aconteça o erro.
> []mostrar alguns tipos de except, mostrar primeiro sem try
```
try: 
	<faça algo>
except Exception:
	<lide com o erro>
```

O código a seguir lida com o erro ZeroDivisionError:
```
def divisao(divisor):
    try:
		print(f'Resultado: {42/divisor}')
    except ZeroDivisionError:
		print('Erro: não pode ser dividido por 0')
print(divisao(2))
print(divisao(12))
print(divisao(0))
print(divisao(1))
```
Após passar pelo erro, o **programa** continua sua execução normalmente.

Outro exemplo é o código a seguir que tenta abrir um arquivo:
```
try:
	open('arquivo_inexistente.txt')
except:
	print('Algo deu errado')
```
Ao abrir um arquivo, pode acontecer de não achar o arquivo ou que o nome é um diretório e posso especificamente lidar com esse erro ao passar para o except:
```
try: 
	open('eh_diretorio.txt')
except IsADirectoryError:
	print('Esse nome é um dirétorio, não é possível abrir')
```

Note que erros **dentro** da função serão apanhados:
```
def divisao(divisor):
	print(f'Resultado: {42/divisor}')
	try:
		print(divisao(2))
		print(divisao(12))
		print(divisao(0))
		print(divisao(1))
    except ZeroDivisionError:
		print('Erro: não pode ser dividido por 0')
```

A razão pela qual o programa para é porque  quando o bloco *except* é excecutado, o programa não retorna novamente ao bloco *try*, ao invés disso continua indo depois da função executada.
Se antes, apenas um erro faria seu programa quebrar, dessa forma você pode executar o seu código mesmo quando um erro for detectado.

Agora, saiba que é possível erguer erros para o seu próprio código. Erguer uma exceção é um jeito de dizer 'Pare de excecutar o código dessa função e vá para o bloco *except*'

* *raise*  keyword
* Chamada para a função Exception()
* Uma string contendo uma mensagem de erro útil passada para a função Excpetion
```
>>> raise Exception('This is the error message.')
Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    raise Exception('This is the error message.')
Exception: This is the error message.
```

Se não tiver blocos de *try* e *except* cobrindo a declaração *raise* que ocorreu, o programa para e mostra a mensagem de erro do *except*.

Em um exemplo prático, não é a função sozinha que vai lidar com o erro mas sim o código. Então é comum a declaração *raise* dentro das funções e o bloco *try* e *except* no corpo do código chamando a função. Como o código a seguir que imprime uma caixa de símbolos:
```
def boxPrint(simbolo, largura, altura):
    if len(simbolo) != 1:
        raise Exception('Símbolo tem de ser apenas um caractere')
    if largura <= 2:
        raise Exception('Largura deve ser maior do que 2')
    if altura <= 2:
        raise Exception('Altura deve ser maior do que 2')

    print(simbolo * largura)
    for i in range(altura - 2):
        print(simbolo + (' ' * (largura - 2)) + simbolo)
    print(simbolo * largura)

for sym, w, h in (('@', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
       print('An exception happened: ' + str(err))
```
Outro exemplo
O programa usa a declaração *except Exception as err*, uma forma da declaração de *except*. Se um objeto *Exceção*(Exception) é retornado da função, a declaração *except* irá guardar na variável *err*. Então o objeto *Exception* é convertido em uma string ao passar na função *str()* para podermos visualizar a mensagem de erro.

##Traceback
Quando Python encontra um erro, é produzido um tesouro de informações de erro chamadas *traceback*. O traceback inclui a mensagem de erro, o número da linha que causou o erro e a sequência de funções que levaram ao erro. Essa sequência é chamada de *call stack*.

Execute o código:
```
def spam():
    bacon()

def bacon():
    raise Exception('This is the error message.')

spam()
```
Observe o traceback. Qual é a sequência de chamada das funções ?


É possível obter a mensagem de erro como uma string através da função *traceback.format_exc()*. Essa função é útil se você quer a informação de algum *except* de um tracceback mas também quer que o erro seja tratado no seu programa. É necessário importar o módulo *traceback* no programa.
```
>>> import traceback
>>> try:
...          raise Exception('This is the error message.')
except:
...          errorFile = open('errorInfo.txt', 'w')
...          errorFile.write(traceback.format_exc())
...          errorFile.close()
...          print('The traceback info was written to errorInfo.txt.')
```

Assim, ao invés do seu programa parar quando ocorrer um erro, o seu programa grava a informação do traceback em um arquivo de texto e deixa o programa continuar executando. Você pode olhar depois para o arquivo de texto, quando você estiver pronta para debugá-lo.

## Assertions
Um *assertion* é uma tipo de checagem que pode ser feita para garantir que o seu código não esta fazendo algo obviamente errado. É feita pela declaração *assert* e se falhar, um *AssertionError* excpetion é erguido. No código, uma declaração *assert* consiste no seguinte:
* *assert* como palavra-chave
* uma condição(uma expressão avaliada para *True* ou *False*)
* uma vírgula
* uma string para mostrar quando a condição for *False*

Execute o código a seguir:
```
>> ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
>>> ages.sort()
>>> ages
[15, 17, 22, 26, 47, 54, 57, 73, 80, 92]
>>> assert ages[0] <= ages[-1] # Assegure que a primeira idade é menor que a última
```

A declaração *assert* nesse trecho garanteque o primeiro item em *ages* seja menor ou igual ao último item. Se a função *sort()* fez o seu trabalho, então a afirmação será *True*. Já que a expressão foi avaliada para *True* então a declaração *assert* não faz nada.

Agora imagine que cometemos um erro e acidentalmente colocamos a função de lista *reverse()* ao inves de sort(). Quando escrevermos o código a seguir no terminal a declaração *assert* erguirá um *AssertionError*:
Escreva o código a seguir no terminal interativo:
```			
>>> ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
>>> ages.reverse()
>>> ages
[73, 47, 80, 17, 15, 22, 54, 92, 57, 26]
>>> assert ages[0] <= ages[-1] # Assegure que a primeira idade é menor que a última
```

Ao contrário das *exceptions*, o seu código não deverá lidar com as declarações *assert* com *try* e *except*, se uma afirmação(*assertion*) falhar, o seu programa **dever** parar.

*Assertions* são apenas para erros da programadora, não erros cometidos pela usuária. *Assertions* devem apenas falhar enquanto o programa esta em desenvolvimento, a usuária não deve ver um erro de *assertion* no produto final. 
Para erros que o seu programa vai encontrar como uma parte normal da sua operação (como um arquivo não ser encontrado ou a usuária digitar uma data inválida), forneça um *exception* ao invés de detectar esse erro com uma declaração *assert*. Você também não deve usar as declarações *assert* no lugar de levantar exceções, pois usuárias podem desligar as afirmações.

## Depurador
Debugger é uma ferramenta que para testar e depurar o seu programa. Está presente em diversos IDEs e em versões gráficas ou pela linha de comando. Com essa ferramenta é possível interagir com seu programa durante a sua execução uma linha por vez ou pausar a execução em um ponto especifíco, examinando-o para entender seu processo e achar erros. 

Consiste nas seguintes funções:
* Continue
Executa o programa normalmente  até que termine o programa ou encontre um *breakpoint
* Step In
Executa a próxima linha do código e parar. Se a próxima linha for uma função o programa "entra" nessa função e vai para a primeira linha dessa função.
* Step Over
Similar ao Step In, porém se a próxima linha de código for uma função, então essa chamada é "pulada". A função é executada.
* Step Out
Executa as linhas do código e retorna para a atual função. Se você entrou em uma função pelo Step In e agora quer executar o resto do código da função e "sair" da função atual.
* Stop
Para o processo do debugger.
* Breakpoints
Pode ser colocado em uma linha específica do código e força o debugger a parar quando o essa linha for executada.

###Debuggers
Linha de comando:
* pdb
* ipdb
* outros..

Gráficos:
* pudb
* IDEs
	Visual Studio Code
	PyCharm
* Outros

###Referências
[Try and Except](https://pythonbasics.org/try-except/)

["Goodbye Print Statements, Hello Debugger!"](https://www.youtube.com/watch?v=HHrVBKZLolg)
