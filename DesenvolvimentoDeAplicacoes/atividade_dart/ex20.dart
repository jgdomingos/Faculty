import 'dart:io';

bool validarLuhn(String numeroEntrada) {
	String numero = numeroEntrada.replaceAll(RegExp(r'[^0-9]'), '');

	List<int> digitos = numero.split('').map((d) => int.parse(d)).toList();
	digitos = digitos.reversed.toList();

	int soma = 0;
	for (int i = 0; i < digitos.length; i++) {
		int digito = digitos[i];
		if (i % 2 == 1) {
			digito *= 2;
			if (digito > 9) {
				digito -= 9;
			}
		}
		soma += digito;
	}

	return soma % 10 == 0;
}

void main() {
	String numeroCartao = stdin.readLineSync()!.trim();
	print(validarLuhn(numeroCartao));
}
