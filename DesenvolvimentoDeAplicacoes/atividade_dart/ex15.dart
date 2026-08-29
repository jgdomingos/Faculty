import 'dart:io';

void main() {
	List<String> partes = stdin.readLineSync()!.trim().split(RegExp(r'\s+'));
	List<double> numeros = partes.map((e) => double.parse(e)).toList();

	double soma = 0;
	for (double numero in numeros) {
		soma += numero;
	}
	double media = soma / numeros.length;
	print(media);
}
