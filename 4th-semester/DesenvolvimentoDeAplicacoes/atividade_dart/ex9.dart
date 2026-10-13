import 'dart:io';

void main() {
	int numero = int.parse(stdin.readLineSync()!.trim());

	if (numero < 0) {
		print("Error");
		return;
	}

	int fatorial = 1;
	for (int i = 2; i <= numero; i++) {
		fatorial *= i;
	}
	print(fatorial);
}
