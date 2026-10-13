import 'dart:io';

void main() {
	int numero = int.parse(stdin.readLineSync()!.trim());
	List<int> tabuada = [];
	for (int i = 0; i <= 10; i++) {
		tabuada.add(numero * i);
	}
	print(tabuada);
}
