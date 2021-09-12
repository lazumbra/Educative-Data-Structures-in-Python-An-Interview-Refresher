OBS:
Sempre que eu for revisar esses conteúdos eu coloco mais anotações.
Explicando como eu fiz pra resolver o objetivo. Passando as minhas anotações do caderno para cá.

Objetivo:
Implementar a função find_mid() que recebe uma linked list como input e retorna o valor do nó do meio da linked list. Se o tamanho da linked list for par, o valor do nó do meio vai está na posição \frac{length}{2}. Para uma lista que tenha tamanho impart, o meio será a posição \frac{length}{2}+1.

Dica:
Use dois ponteiros: um ponteiro que se move rápido e outro ponteiro que se move lento. A cada interação o ponteiro rápido se move a duas posições e o ponteiro lento se move apenas uma posição. Quando o ponteiro rápido chegar no fim (None), o ponteiro lento estará exatamente no meio. Lembre de mover primeiro o ponteiro rápido, após mover o ponteiro rápido você verifica se ele já chegou no fim, pois se ele chegou no fim, quer dizer que vc não precisa mais mover o ponteiro lento e é só retornar o ponteiro lento pois o ponteiro lento já terá chegado no meio.

Input:
Uma Linked List

Output:
Um inteiro que é o meio da lista


Exemplo:

LinkedList = 9->10->2->4

Resposta será 10.
