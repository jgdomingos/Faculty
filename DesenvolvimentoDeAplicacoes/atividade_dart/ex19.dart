import 'dart:io';

bool validarCPF(String cpfEntrada) {
	String cpf = cpfEntrada.replaceAll(RegExp(r'[^0-9]'), '');

	if (cpf.length != 11) {
		return false;
	}

	bool todosIguais = true;
	for (int i = 1; i < cpf.length; i++) {
		if (cpf[i] != cpf[0]) {
			todosIguais = false;
			break;
		}
	}
	if (todosIguais) {
		return false;
	}

	List<int> digitos = cpf.split('').map((d) => int.parse(d)).toList();

	int soma1 = 0;
	for (int i = 0; i < 9; i++) {
		soma1 += digitos[i] * (10 - i);
	}
	int resto1 = soma1 % 11;
	int digitoVerificador1 = resto1 < 2 ? 0 : 11 - resto1;

	if (digitoVerificador1 != digitos[9]) {
		return false;
	}

	int soma2 = 0;
	for (int i = 0; i < 10; i++) {
		soma2 += digitos[i] * (11 - i);
	}
	int resto2 = soma2 % 11;
	int digitoVerificador2 = resto2 < 2 ? 0 : 11 - resto2;

	if (digitoVerificador2 != digitos[10]) {
		return false;
	}

	return true;
}

void main() {
	String cpf = stdin.readLineSync()!.trim();
	print(validarCPF(cpf));
}
