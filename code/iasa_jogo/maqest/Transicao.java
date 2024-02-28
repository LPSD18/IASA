package maqest;
/*
 * Classe Transicao
 */
public class Transicao <EV,AC> {
/*
 * recebe por associacao uma instancia da classe Estado
 */
    private Estado<EV,AC> estadoSucessor;
    private AC accao;
/*
 * construtor que inicia o a instancia EstadoSucessor e o atributo Accao
 * 
 * @param Estado<EV,AC> estadoSucessor
 * @param AC accao
 */
    public Transicao(Estado<EV,AC> esstadoSucessor, AC accao){
        this.estadoSucessor=esstadoSucessor;
        this.accao =accao;
    }
/*
 * faz return do estado Sucessor
 */
    public Estado<EV,AC> getEstadoSucessor(){
        return this.estadoSucessor;
    }
/*
 * faz return da accao
 */
    public AC getAccao(){
        return this.accao;
    }
}
