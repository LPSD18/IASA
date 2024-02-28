package ambiente;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/*
 * Classe ambiente 
 * Esta classe é utilizada na classe Jogo sendo o "meio onde a personagem atua"
 * nesta classe é utilizada por associação a classe Eventos
 * 
 * 
 */

public class Ambiente {

    private Evento evento;
    private Map<String,Evento> eventos;

    private Scanner sc = new Scanner(System.in);

/*
 * a classe construtora cria um HashMap da classe eventos para a utilização mais facil do jogo
 */
    public Ambiente(){
        eventos = new HashMap<String,Evento>();
        eventos.put("s",Evento.SILENCIO);
        eventos.put("r",Evento.RUIDO);
        eventos.put("a",Evento.ANIMAL);
        eventos.put("f",Evento.FUGA);
        eventos.put("o",Evento.FOTOGRAFIA);
        eventos.put("t",Evento.TERMINAR);
    }
/* 
 * faz return do evento atual
 */
    public Evento getEvento(){

        return evento;
    }
/*
 * este método é utilizado para poder evoluir o ambiente do jogo e mostrar em que evento se está na altura
 */
    public void evoluir(){
        evento = gerarEvento();
        mostrar();
    }
/*
 * Método para a decisão de que evento se está a ocorrer na altura no jogo
 * @return Evento evento
 */
    private Evento gerarEvento(){
        System.out.println("Escolha o evento");
        String txt = sc.next();
        evento = eventos.get(txt);
        return evento;
    }
/*
 * método para mostrar o evento atual
 */
    private void mostrar(){
        System.out.println("Evento --> " + evento);
    }




}
