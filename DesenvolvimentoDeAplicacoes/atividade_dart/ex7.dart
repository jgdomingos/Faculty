import 'dart:io';

void main() {
	int numero = int.parse(stdin.readLineSync()!.trim());
	if (numero % 2 == 0) {
		print("par");
	} else {
		print("impar");
	}
}
