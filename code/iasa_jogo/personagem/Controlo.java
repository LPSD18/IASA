package personagem;

import ambiente.Evento;
import maqest.Estado;
import maqest.MaquinaEstados;
/*
 * Classe controlo utilizada pela personagem para poder decidir quais os proximos movimentos
 */
public class Controlo {
/*
 * utilizado para saber os movimentos
 */
    private MaquinaEstados<Evento,Accao> maqest;
/*
 * Criação da instancia maqest com um HashMap e atribuição dos estados do jogo com os eventos e ações utilizadas
 */
    public Controlo(){
        Estado<Evento,Accao> procura = new Estado<>("Procura");
        Estado<Evento,Accao> inspeccao = new Estado<>("Inspeccao");
        Estado<Evento,Accao> observacao = new Estado<>("Observacao");
        Estado<Evento,Accao> registo = new Estado<>("Registo");

        procura.transicao(Evento.ANIMAL,observacao,Accao.APROXIMAR);
        procura.transicao(Evento.RUIDO,inspeccao,Accao.APROXIMAR);
        procura.transicao(Evento.SILENCIO,procura,Accao.PROCURAR);

        inspeccao.transicao(Evento.ANIMAL, observacao,Accao.APROXIMAR);
        inspeccao.transicao(Evento.RUIDO, inspeccao,Accao.PROCURAR);
        inspeccao.transicao(Evento.SILENCIO, procura);

        observacao.transicao(Evento.FUGA,inspeccao);
        observacao.transicao(Evento.ANIMAL,registo);

        registo.transicao(Evento.ANIMAL, registo);
        registo.transicao(Evento.FUGA,procura);
        registo.transicao(Evento.FOTOGRAFIA,procura);

        maqest = new MaquinaEstados<>(procura);
    }
/*
 * return do estado atual da maquina de estados
 */
    public Estado<Evento,Accao> getEstado(){
        return maqest.getEstado();
    }
/*
 * faz o processamento do evento e retorna a ação realizada ao acontecer esse evento
 * 
 * @param Percepcao percepcao
 * @return Accao
 */
    public Accao processar (Percepcao percepcao){
        Evento e = percepcao.getEvento();
        Accao a = maqest.processar(e);
        mostrar();
        return a;

    }
/*
 * print do estado atual da mquina de estados
 */
    private void mostrar(){
       System.out.println("Maquina de Estados --> " + maqest.getEstado().getNome()); 
    }
}
