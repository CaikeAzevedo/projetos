//// Converte Letras grupo Caike Augusto e Vinicius Zaia BCC Turma B

#include <stdio.h>
#include <ctype.h>

int main() {
  FILE *fp = fopen("ArquivoTextoEntrada.txt", "r");
  FILE *fp2 = fopen("ArquivoTextoSaida.txt", "w");
  char ch, CH;
  
  while ((ch = fgetc(fp)) != EOF) {
    CH = toupper(ch);
    fputc(CH, fp2);
    }
  fclose(fp);
  fclose(fp2);
  
  return 0;
}
