// Conta Letras grupo Caike Augusto e Vinicius Zaia BCC Turma B
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
  int contadorletra[26] = {0};
  int tamanho;
  char chr[50];
  char c;
  
  FILE *fp = fopen("arquivotexto.txt", "r");

  fgets(chr,50,fp);
  tamanho = strlen(chr);
  
  for (int i = 0; i < tamanho; i++){

    c = tolower(chr[i]);

    if (c >= 'a' && c <= 'z'){
      contadorletra[c - 'a']+= 1;
    }
  }
  for (int i = 0; i < 26; i++){
    printf("%c;%d\n",('A' + i), contadorletra[i]);
  }
  
  fclose(fp);
  return 0;
}
