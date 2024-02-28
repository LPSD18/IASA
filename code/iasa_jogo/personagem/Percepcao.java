package personagem;

import ambiente.Evento;
/*
 * classe Percepcao
 * 
 */
public class Percepcao {
/*
 * utiliza um atributo da classe Evento
 */
    private Evento evento;
/*
 * No construtor inicia esse atributo
 * 
 * @param Evento evento
 */
    public Percepcao(Evento evento){
        this.evento=evento;
    }
/*
 * faz return do evento atual
 * 
 * @return Evento
 */
    public Evento getEvento(){

        return this.evento;
    }
}
