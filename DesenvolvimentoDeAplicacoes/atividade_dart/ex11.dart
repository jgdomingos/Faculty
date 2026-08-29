import 'dart:io';

void main() {
	List<String> partes = stdin.readLineSync()!.trim().split(RegExp(r'\s+'));
	List<int> numeros = partes.map((e) => int.parse(e)).toList();

	int maior = numeros[0];
	int menor = numeros[0];
	for (int numero in numeros) {
		if (numero > maior) maior = numero;
		if (numero < menor) menor = numero;
	}
	print([maior, menor]);
}
