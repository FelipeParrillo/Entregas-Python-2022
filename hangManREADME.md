Leí el codigo y pude seguir lo que hizo el programador del juego.
Hubo dos cosas que no me terminaron de convencer (#Check if the player won# y como se guardaban los char en correctLetters)

1°Vamos a empezar por la mas larga #Check if the player won#:
    A simple vista estaba todo bien, cuando lo lei detenidamente me di cuenta que varias cosas no cerraban, primero ponia un booleano en True para luego en un for in rng
    pasarlo a False mientras corroboraba por posicion que en selectLetters eesten todas las letras de secretWord para luego preguntar 
    en un if fuera del for si habia ganado.. Muy enrredado y poco intuitivo.
    
    Para cambiar esto borre todo lo que habia y simplemente pregunte si la len de ambos era la misma, si len(correctLetters)==len(secretWord) y a correctLetters solo 
    entran las letras correctas entonces ganaste. Esto me llevo al segundo problema y que no vi venir hasta que lo corri con los cambios.
    
2°La forma en la que se guardaban los char en correctLetters:
    Termine descubriendo que en correctLetters los char repetidos, es decir una palabra con dos letras iguales solo se guardaban una vez y no se tomaban como distintas
    por lo que la len(correctLetters) en una palabra con letras repetidas daba un numero erroneo  al corregir esto el primer cambio tambien funciono correctamente.
    
Cosas agregadas/Modificadas:
  1°Metodo littleHelp() el cual envia una ayudita al jugador si erra una letra y siguen faltando vocales en la palabra
  2°Cambie la condicion logica para verificar si el jugador gano o aun no el juego nueva CONDICION de victoria: if (len(secretWord)==len(correctLetters))
  3°Nueva forma de guardar en correctLetters los caracteres repetidos (ahora se guardan como dos letras distintas  dando una len correcta)
   
