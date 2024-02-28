package personagem;

import ambiente.Ambiente;
/*
 * classe da Personagem do Jogo
 * recebe por associação a classe Ambiente 
 * recebe por composição a classe Controlo
 */
public class Personagem {

    private Controlo controlo;
    private Ambiente ambiente;
/*
 * Construtor da personagem inicia a instancia do atributo da classe Ambiente e do atributo da classe Controlo
 * 
 * @param Ambiente ambiente
 */
    public Personagem(Ambiente ambiente){
        this.ambiente=ambiente;
        controlo = new Controlo();
        
    }
/*
 * Executa os movimentos da personagem dependendo da percepção e actuar processando essa percepcão
 */
    public void Executar(){
        Percepcao p = this.percepcionar();
        Accao a =controlo.processar(p);
        actuar(a);
        
    }
/*
 * cria uma instancia da classe Percepcao e faz return desse atributo
 * 
 * @return Percepcao 
 */
    public Percepcao percepcionar(){
        Percepcao p = new Percepcao(ambiente.getEvento());
        return p;
    }
/*
 * faz print na consola da acção atual da personagem
 * 
 * @param Accao accao
 */
    public void actuar(Accao accao){
        if(accao!=null)
        System.out.println("Estado da ação --> " + accao);
    }


}
