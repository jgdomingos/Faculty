import 'dart:io';

void main() {
	List<String> partes = stdin.readLineSync()!.trim().split(RegExp(r'\s+'));
	List<int> numeros = partes.map((e) => int.parse(e)).toList();

	int soma = 0;
	for (int numero in numeros) {
		soma += numero;
	}
	print(soma);
}
