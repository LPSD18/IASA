import ambiente.Ambiente;
import ambiente.Evento;
import personagem.Personagem;

public class Jogo {

/*
 * A classe Jogo recebe a classe ambiente e Personagem por composição pois esta classe é composta pelas outras duas
 */

    private Ambiente ambiente;
    private Personagem personagem;
    
    /* 
     * função main
     * corre o executar da classe Jogo
     */
    public static void main(String[] args){
        Jogo jogo= new Jogo();
        jogo.executar();
    }
    /*
     * função onde vai ser realizado o jogo em modo texto
     * utilização dos metodos das classes ambiente evoluir e getEvento para verificar e atualizar o jogo
     * utilização dos metodos da classe personagem executar para poder realizar os "movimentos da personagem"
     * esta função apenas para de correr se o evento for igual a TERMINAR
     * 
     * 
     */
    private void executar(){
        ambiente = new Ambiente();
        personagem = new Personagem(ambiente);
        Evento evento = ambiente.getEvento();
        while(evento !=Evento.TERMINAR){
            personagem.Executar();
            ambiente.evoluir();
            evento = ambiente.getEvento();
        }
        
    }
}
