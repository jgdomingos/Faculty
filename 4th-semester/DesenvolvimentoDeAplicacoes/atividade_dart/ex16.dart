import 'dart:io';

void main() {
	String texto = stdin.readLineSync()!;
	String invertida = String.fromCharCodes(texto.runes.toList().reversed);
	print(invertida);
}
