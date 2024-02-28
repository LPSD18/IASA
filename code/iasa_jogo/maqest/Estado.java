package maqest;

import java.util.HashMap;
import java.util.Map;


/*
 * Classe Estado recebe por composição uma instancia da classe Transição
 * é utilizada pela classe MaquinaEstados
 */
public class Estado <EV,AC> {
/*
 * map da instancia da classe Transicoes
 */
    private Map<EV,Transicao<EV,AC>> transicoes;
/*
 * Atributo nome do estado atual
 */
    private String nome;
/*
 * Construto inicia o atributo nome e inicia o HashMap da instancia da classe Transicao
 */
    public Estado(String nome){
        this.nome = nome;
        transicoes = new HashMap<EV,Transicao<EV,AC>>();
        
    }
/*
 * return do nome
 */
    public String getNome (){
        return this.nome;
    }
/*
 * processa o evento atual dependendo da transição
 * 
 * @param EV evento
 * @return Transicao
 */
    public Transicao<EV,AC> processar(EV evento){
        return transicoes.get(evento);
        
    }
/*
 * metodo transicao que faz return da transição com o evento atual e o estado sucessor
 * 
 * @param EV evento
 * @param Estadio>EV,AC> estadoSucessor
 * @return Estado<EV,AC>
 */
    public Estado<EV,AC> transicao(EV evento, Estado<EV,AC> estadoSucessor){
        return this.transicao(evento, estadoSucessor, null);
    }
/*
 * metodo igual ao anterior mas neste faz return da transicao tambem com uma acao
 * 
 * @param EV evento
 * @param Estado<EV,AC> estadoSucessor
 * @param AC accao
 * @return estadoSucessor
 */
    public Estado<EV,AC> transicao(EV evento,Estado<EV,AC> estadoSucessor,AC accao){
        transicoes.put(evento, new Transicao<EV,AC>(estadoSucessor,accao));
        return estadoSucessor;
    }

    

}
