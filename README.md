# Robotic Process Automation 

Este projeto tem como objetivo automatizar tarefas repetitivas usando Python, baseando-se nos princípios de RPA (*Robotic Process Automation*). As ações a serem executadas são definidas em um arquivo CSV (`tarefas.csv`), onde cada linha descreve uma tarefa. O script lê esse arquivo e, **usando a biblioteca PyAutoGUI**, realiza as ações na ordem especificada. As tarefas suportadas incluem **digitação de texto**, **pressionamento de teclas**, **espera (delay)**, **combinações de teclas (hotkeys)** e **cliques** em coordenadas específicas da tela. Ao final da execução, o programa gera um **relatório em formato Excel** contendo o status (sucesso ou falha) de cada tarefa e o tempo gasto em sua execução.

## Pré-requisitos

- **Python 3.x** instalado no sistema.
- **Virtual environment (venv)** configurada com as dependências do projeto. (As principais bibliotecas incluem o **PyAutoGUI** para automação de mouse/teclado e uma biblioteca para manipulação de Excel, como **pandas** ou **openpyxl**, já instaladas na venv do projeto.)
- Sistema operacional Windows, Linux ou macOS com acesso ao ambiente de desktop (PyAutoGUI funciona nos principais sistemas, mas pode requerer configurações adicionais em Linux ou permissões no macOS).

> **Observação:** Certifique-se de ter permissões adequadas no sistema para que o Python controle o mouse e teclado. No macOS, por exemplo, pode ser necessário conceder acesso de "Acessibilidade" ao Python para o PyAutoGUI funcionar.

## Estrutura esperada do arquivo `tarefas.csv`

O arquivo `tarefas.csv` contém as instruções das tarefas a serem automatizadas. Cada linha representa uma tarefa, composta por pelo menos duas colunas principais: **Tipo** e **Dados**. A coluna **Tipo** indica o tipo de ação a ser realizada, e a coluna **Dados** fornece os parâmetros ou informações necessárias para aquela ação. Abaixo estão os tipos suportados e exemplos de valores esperados em cada caso:

| **Tarefa**         | **Tipo** (exemplo)         | **Dados**                                            |
|--------------------|----------------------------|------------------------------------------------------|
| `digitar_texto`    | texto                      | Digita o texto fornecido. (Olá, mundo!)              |
| `pressionar_tecla` | tecla                      | Pressiona a tecla especificada (enter)               |
| `delay`            | espera                     | Aguarda pelo número de segundos indicado (5)         |
| `hotkey`           | hotkey                     | Pressiona simultaneamente as teclas (Ctrl+C)         |
| `clique`           | click                      | Clica nas coordenadas X=100, Y=200 da tela.          |

*Exemplo de conteúdo do arquivo `tarefas.csv`:*

```csv
Tarefa,Tipo,Dado
digitar_texto,texto,"Olá, mundo!"
delay,espera,5
pressionar_tecla_enter,tecla,enter
copiar_conteudo,hotkey,"ctrl+c"
clique_img,click,("x=150,y=350")
```

No exemplo acima, usamos aspas para encapsular valores que contêm vírgula, como coordenadas ou textos com pontuação, garantindo que sejam lidos corretamente como um único campo do CSV. Certifique-se de estruturar o arquivo conforme o formato esperado:
- **Tipo:** um dos valores suportados listados na tabela (não diferenciar maiúsculas/minúsculas, conforme implementado no código).
- **Dados:** o parâmetro da ação:
  - Texto a digitar, no caso de `digitar_texto`.
  - Nome da tecla a pressionar, no caso de `pressionar_tecla` (por exemplo, *enter*, *esc*, *tab*, *f1*).
  - Quantidade de segundos (número) para esperar, no caso de `delay`.
  - Combinação de teclas para atalho, no caso de `hotkey` (por exemplo, *ctrl+c*, *alt+F4*, *ctrl+shift+n*). As teclas podem ser separadas por `+` ou outro delimitador conforme o script esperar.
  - Coordenadas X e Y, no caso de `clique`. Dependendo da implementação, pode ser um único campo com "X,Y" ou duas colunas separadas. No exemplo, consideramos um único campo com os valores separados por vírgula.

> **Dica:** Edite o `tarefas.csv` em um editor adequado (Excel, LibreOffice Calc ou um editor de texto). Se usar vírgula como separador de coluna, lembre de envolver em aspas os campos que contenham vírgulas internas (como no caso das coordenadas). Alternativamente, você pode usar ponto-e-vírgula (;) como separador de coluna no CSV para evitar conflitos com a vírgula das coordenadas.

## Como instalar

Siga os passos abaixo para preparar o ambiente e instalar o projeto:

1. **Obtenha o código do projeto:** Clone o repositório para o seu computador ou faça o download dos arquivos do projeto. Por exemplo, via Git:

   ```bash
   git clone https://github.com/gustavor0d/robotic_process_automation.git
   ```
   Em seguida, entre no diretório do projeto:
   ```bash
   cd robotic_process_automation
   ```

2. **Ative a virtual environment do projeto:** Antes de executar o script, é necessário ativar a venv que contém as dependências.
   - **No Windows:** abra o Prompt de Comando na pasta do projeto e execute `.\venv\Scripts\activate`.
   - **No Linux/Mac:** abra o terminal na pasta do projeto e execute `source venv/bin/activate`.

   Após esse comando, seu prompt deverá indicar que a venv está ativa (por exemplo, aparecendo `(venv)` no início da linha).

3. **(Opcional) Instalando dependências manualmente:** Caso você não utilize a venv fornecida (ou ela não funcione em seu sistema), poderá criar um novo ambiente virtual e instalar as dependências manualmente. Por exemplo:
   ```bash
   python3 -m venv venv_nova
   source venv_nova/bin/activate  # (ou venv_nova\Scripts\activate no Windows)
   pip install pyautogui openpyxl pandas
   ```
   *(Use um arquivo `requirements.txt` se fornecido, ou instale as bibliotecas necessárias individualmente conforme listado acima.)*

   No entanto, em condições normais, usar a venv já incluída simplifica o processo, pois todas as bibliotecas já estão instaladas nela.

## Como executar o projeto (passo a passo)

Após instalar os pré-requisitos e preparar o ambiente, você pode executar o script de automação seguindo os passos:

1. **Prepare o arquivo de tarefas:** Certifique-se de que o arquivo `tarefas.csv` está preenchido corretamente com as ações desejadas, conforme a estrutura especificada na seção anterior. Salve-o na pasta do projeto (ou no local esperado pelo script).

2. **Ative a venv (se ainda não estiver ativa):** Caso não tenha ativado durante a instalação, ative a virtual environment conforme descrito acima, para garantir que as dependências do projeto sejam utilizadas.

3. **Execute o script principal:** Rode o script Python que inicia a automação. Por exemplo, no diretório do projeto, execute:
   ```bash
   (venv) $ python executar_tarefas.py
   ```
   *(Substitua `executar_tarefas.py` pelo nome correto do arquivo principal do projeto, caso seja diferente.)*

   Ao executar esse comando, o programa iniciará a leitura do `tarefas.csv` e realizará cada ação em sequência. Você verá o mouse mover-se e teclas sendo digitadas automaticamente conforme as instruções do arquivo.

4. **Aguarde a conclusão:** Deixe o script executar todas as tarefas até o fim. Não interfira usando o mouse ou teclado durante a execução (veja **Observações e cuidados** abaixo). Ao término de todas as ações, o próprio script irá gerar um arquivo de relatório com os resultados.

5. **Verifique o relatório:** Após a finalização, procure pelo arquivo de relatório Excel gerado (por exemplo, `relatorio_tarefas.xlsx`) no diretório do projeto. Nele constará o status de cada tarefa executada e o tempo gasto. *(Mais detalhes na próxima seção.)*

## Geração do relatório

Ao fim da execução do script, um arquivo de **relatório Excel (.xlsx)** é criado automaticamente resumindo os resultados de cada tarefa. Esse relatório normalmente contém uma tabela com colunas parecidas com as seguintes:

- **Tarefa** – uma identificação ou breve descrição da tarefa executada. Pode ser o próprio tipo de ação junto com seu dado. *Ex:* `digitar_texto: Olá, mundo!` ou `hotkey: ctrl+c`.  
- **Status** – o resultado da execução da tarefa. Geralmente indica **Sucesso** (ou "OK") se a tarefa foi concluída corretamente, ou **Falha** caso tenha ocorrido algum erro durante aquela ação.  
- **Tempo de Execução** – o tempo gasto para realizar a tarefa, geralmente em segundos (pode incluir casas decimais para maior precisão). Isso permite avaliar o desempenho de cada passo.

Cada linha do relatório corresponde a uma linha do `tarefas.csv` executada. Por exemplo, se havia 10 tarefas no CSV, o relatório listará 10 entradas com o status e tempo de cada uma na mesma ordem. O relatório facilita a identificação de eventuais problemas - por exemplo, se uma tarefa falhou (status "Falha"), o usuário pode verificar se houve algum erro de instrução no CSV ou alguma condição inesperada na hora da execução.

O arquivo de relatório é salvo no próprio diretório do projeto (a menos que o script esteja configurado para outro caminho). Você pode abri-lo em qualquer editor de planilhas (Excel, LibreOffice Calc, etc.) para analisar os resultados. 

## Observações e cuidados

Ao utilizar este projeto de automação, leve em conta as seguintes considerações para garantir que tudo ocorra bem:

- **Mantenha o contexto correto:** Antes de iniciar o script, abra e deixe em foco a janela ou aplicativo onde as ações devem ser realizadas. O script **não** abre aplicativos automaticamente; ele apenas digita teclas e realiza cliques na interface atual. Por exemplo, se as tarefas envolvem digitar texto em um campo de formulário, deixe esse campo ativo (clique nele manualmente) **antes** de rodar o script.

- **Não interfira durante a execução:** Evite mover o mouse, usar o teclado ou controlar o computador enquanto o robô está executando as tarefas. Qualquer interferência manual pode desordenar a sequência de ações (por exemplo, movendo o mouse para longe do alvo do clique) e levar a resultados indesejados. Idealmente, não use o computador até que o script finalize todas as tarefas.

- **Coordenadas de clique:** As coordenadas X,Y utilizadas para cliques devem corresponder à sua tela e resolução atuais. Se você trocar de monitor ou alterar a resolução, atualize os valores no CSV. Para descobrir coordenadas de pontos específicos na tela, você pode usar a função `pyautogui.position()` em um prompt Python (ela retorna a posição atual do cursor) ou outras ferramentas de captura de coordenadas. Certifique-se de que o ponto indicado está correto – um clique no local errado pode causar falhas ou comportamentos indesejados na automação.

- **Nomes de teclas e atalhos:** Quando especificar teclas no CSV, use os nomes reconhecidos pelo PyAutoGUI (geralmente correspondentes às teclas em inglês, minúsculas). Por exemplo, use `"enter"` em vez de "Entrar", use `"space"` para espaçador, `"esc"` para Escape, `"tab"` para Tab, etc. Para combinações de teclas (`hotkey`), separe claramente as teclas com `+` (ou em colunas separadas, conforme o caso). Exemplo: `"ctrl+alt+delete"` representa Ctrl+Alt+Del. Um nome de tecla incorreto pode fazer com que o pressionamento não funcione.

- **Tempo entre ações:** O script pode incluir pequenas pausas automáticas entre uma ação e outra (o PyAutoGUI, por padrão, insere um delay curto global após cada comando). Se necessário, você pode adicionar **ações do tipo `delay` no CSV** para esperar períodos maiores entre passos – isso pode ajudar caso o computador seja mais lento ou um programa demore a responder, evitando que a automação prossiga antes do sistema estar pronto. Ajuste esses tempos de acordo com a necessidade.

- **Mecanismo de segurança (*Fail-safe*):** O PyAutoGUI possui um recurso de segurança que interrompe imediatamente a execução se o mouse for movido rapidamente para o canto superior esquerdo da tela (coordenada 0,0). Esse fail-safe está **ativado por padrão**. Use-o se precisar abortar o script em caso de emergência. Por exemplo, se você perceber que algo não está certo na automação, mova o mouse para o topo esquerdo para parar tudo. (Note que o script poderá lançar uma exceção PyAutoGUIFailSafe ao interromper, o que é esperado nesse caso.)

- **Testes antes de execuções longas:** Antes de rodar uma longa sequência de tarefas ou algo em um ambiente crítico, faça testes com poucas linhas no `tarefas.csv`. Verifique se cada tipo de ação está se comportando conforme esperado (digitando nos campos corretos, clicando nos lugares certos, etc.). Ajuste o que for necessário (como coordenadas ou tempos de delay) e só então proceda com a execução completa.

- **Uso responsável:** Utilize este automação de forma responsável. Se for automatizar ações em softwares de terceiros ou em sistemas online, garanta que está de acordo com os termos de uso e políticas dessas plataformas. A automação não deve violar regras do sistema alvo.
