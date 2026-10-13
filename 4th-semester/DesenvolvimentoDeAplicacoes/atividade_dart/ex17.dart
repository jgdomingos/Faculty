import 'dart:io';

void main() {
	String texto = stdin.readLineSync()!.toLowerCase();
	String vogais = "aeiouáéíóúãõâêîôû";
	int contador = 0;

	for (int i = 0; i < texto.length; i++) {
		if (vogais.contains(texto[i])) {
			contador++;
		}
	}
	print(contador);
}
