from dotenv import load_dotenv
load_dotenv()

from src.interfaces import app

# import time



# text = """As linguagens de programação normalmente suportam tanto estruturas condicionais como também os chamados laços de repetição, estruturas que permitem a execução de instruções repetidas vezes, até que uma condição seja atingida.

# Neste artigo, veremos como funcionam e como utilizar as estruturas de controle por repetição em Python: FOR e WHILE.

# Loops com FOR e WHILE
# Em algumas situações, é comum que uma mesma instrução (ou conjunto delas) precise ser executada várias vezes seguidas. Nesses casos, normalmente utilizamos um loop (ou laço de repetição), que permite executar um bloco de código repetidas vezes, enquanto uma dada condição é atendida.

# Em Python, os loops são codificados por meio dos comandos for e while. O primeiro nos permite percorrer os itens de uma coleção e, para cada um deles, executar um bloco de código. Já o while, executa um conjunto de instruções várias vezes enquanto uma condição é atendida.

# Na Listagem 1 temos um exemplo de uso do comando for.

# nomes = ['Pedro', 'João', 'Leticia']
# for n in nomes:
#     print(n)
# Listagem 1. Comando for
# A variável definida na linha 1 é uma lista inicializada com uma sequência de valores do tipo string. A instrução for percorre todos esses elementos, um por vez e, em cada caso, atribui o valor do item à variável n, que é impressa em seguida. O resultado, então, é a impressão de todos os nomes contidos na lista.

# O comando while, por sua vez, faz com que um conjunto de instruções seja executado enquanto uma condição for atendida. Quando o resultado passa a ser falso, a execução é interrompida, saindo do loop, e passa para o próximo bloco.

# Na Listagem 2 a seguir, vemos um exemplo de uso do laço while, onde definimos a variável contador, iniciando com 0, e enquanto seu valor for menor que 5, executamos as instruções das linhas 3 e 4.

# contador = 0
# while contador < 5:
#     print(contador)
#     contador = contador + 1
# Listagem 2. Uso do While
# Observe que na linha 4 incrementamos a variável contador, de forma que em algum momento seu valor igual a 5. Quando isso for verificado na linha 2, o laço será interrompido. Caso a condição de parada nunca seja atingida, o loop será executado infinitamente, gerando problemas no programa.

# Estruturas de repetição estão presentes na maioria das linguagens de programação e representam uma parte fundamental de cada uma delas. Sendo assim, é muito importante conhecer a sintaxe e o funcionamento dessas estruturas."""

# # for engine in openai.Engine.list().data:
# #     print(engine.id)

# tic = time.perf_counter()
# completion_data = openai.Completion.create(
#     engine='text-davinci-003',
#     prompt=f'Faça um resumo do texto a seguir: {text}',
#     max_tokens=2048,
#     stop=None
# )
# toc = time.perf_counter()
# print(completion_data.choices[0].text)
# print(f"Response davince in {toc - tic:0.4f} seconds")

# tic = time.perf_counter()
# chat_completion_data = openai.ChatCompletion.create(
#     model='gpt-3.5-turbo',
#     messages=[{ 'role': 'user', 'content': f'Faça um resumo do texto a seguir: {text}' }]
# )
# toc = time.perf_counter()
# print(chat_completion_data.choices[0].message.content)
# print(f"Response Chat GPT 3.5 in {toc - tic:0.4f} seconds")

