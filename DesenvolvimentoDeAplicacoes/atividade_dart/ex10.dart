import 'dart:io';

void main() {
	int quantidade = int.parse(stdin.readLineSync()!.trim());
	List<int> fibonacci = [];

	int a = 0;
	int b = 1;
	for (int i = 0; i < quantidade; i++) {
		fibonacci.add(a);
		int proximo = a + b;
		a = b;
		b = proximo;
	}
	print(fibonacci);
}
