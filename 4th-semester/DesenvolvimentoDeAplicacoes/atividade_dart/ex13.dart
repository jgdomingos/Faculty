import 'dart:io';

void main() {
	List<String> partes = stdin.readLineSync()!.trim().split(RegExp(r'\s+'));
	List<int> numeros = partes.map((e) => int.parse(e)).toList();

	numeros.sort();
	print(numeros);
}
