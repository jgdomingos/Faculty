import 'dart:io';

void main() {
	String palavra = stdin.readLineSync()!.trim();
	String invertida = String.fromCharCodes(palavra.runes.toList().reversed);
	bool ehPalindromo = palavra == invertida;
	print(ehPalindromo);
}
