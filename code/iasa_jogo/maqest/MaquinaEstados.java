package maqest;

/*
 * Classe MaquinaEstados 
 * utilizada para poder ser utilizada por outra classe geral sem ter de mudar o codigo
 * recebe por associacão a classe Estado que é utilizada nos metodos desta classe
 * 
 */


public class MaquinaEstados <EV,AC> {

    public Estado<EV,AC> estado;

/*
 * construtor onde se inicia a classe Estado
 */
    public MaquinaEstados (Estado<EV,AC> estado){
        this.estado =estado;
    }
/*
 * faz return do estado atual
 */
    public Estado<EV,AC> getEstado(){
        return this.estado;
    }
/*
 * método que recebe um evento e processa utilizando o método da classe Transicao e atualiza recebendo o estado sucessor e a proxima ação
 * faz return da ação
 * 
 * @param EV evento
 * @return AC
 */
    public AC processar(EV evento){
        Transicao<EV,AC> t = estado.processar(evento);
        if(t!=null){
            estado =  t.getEstadoSucessor();
            AC accao = t.getAccao();
            return accao;
            
        }
        return null;
    }
    

}
