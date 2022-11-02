# pyort_scanmap

O pyort_scanmap é um portscan(uma ferramenta que scaneia um servidor para saber quais portas estão abertas ou fechadas).
Ele foi feito usando python, eu utilizei as libs file e Socket.
O código em si esta em inglês, mas acho que n vai te atrapalhar tanto.
Esse tipo de ferramenta é muito usada por hackers para fazer um pentest de um site ou host, então você pode usar o pyort_scan para isso.
_____

# como instalar:
Você pode instala-lo baixando o arquivo zip e extraindo, para executar.
Ou pode usar o comando:<br>
git clone https://github.com/IagoManoel/pyort_scanmap.git
______________________________

# como usar:
Para usa-lo, primeiro você terá que executalo, se ainda não tem o python ou o socket, vai precisar instalar.
De início vai aparecer um menu com algumas o opições:<br>
Scan: 1<br>
See scan_historic: 2<br>
<br>
E vai aparecer um input: which option will you use? <br>
E você vai colocar 1, se quiser fazer um scan ou 2, se quiser ver um histórico de todos os hosts que você
Ja escaneou e os dados das portas. <br>
________
AO COLOCAR 1: <br>
Vai aparecer um input: what is the target? E você vai colocar o alvo do scan, pode ser um site ou um IP.
Após dar enter, vai começar a aparecer uma lista de portas do servidor e vai dizer quais estão abertas ou fechadas, você pode
Mudar a lista de portas editando o código e mudando os números da variavel "ports". <br>
Após isso vai aparecer outro input: want to do another scan?[y/n] (você quer fazer outro scan?),
se você digitar "y" o código vai reiniciar para a parte onde pergunta: which option will you use? E vai repetir o código novamente até o usuario dizer "n"
<br>

AO COLOCAR 2: <br>
Vai simplesmente mostrar todo o histórico, de hosts que você escaneou e mostrar quais portas estavam fechadas ou abertas, mas se
você ainda não fez scan ou apagou o arquivo, então não vai aparecer nada.




