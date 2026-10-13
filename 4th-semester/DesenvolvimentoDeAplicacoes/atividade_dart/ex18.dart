import 'dart:io';

String cifrarCesar(String mensagem, int deslocamento) {
	StringBuffer resultado = StringBuffer();

	for (int i = 0; i < mensagem.length; i++) {
		String caractere = mensagem[i];
		int codigo = caractere.codeUnitAt(0);

		if (codigo >= 65 && codigo <= 90) {
			int novoCodigo = ((codigo - 65 + deslocamento) % 26 + 26) % 26 + 65;
			resultado.write(String.fromCharCode(novoCodigo));
		} else if (codigo >= 97 && codigo <= 122) {
			int novoCodigo = ((codigo - 97 + deslocamento) % 26 + 26) % 26 + 97;
			resultado.write(String.fromCharCode(novoCodigo));
		} else {
			resultado.write(caractere);
		}
	}

	return resultado.toString();
}

void main() {
	int deslocamento = int.parse(stdin.readLineSync()!.trim());
	String mensagem = stdin.readLineSync()!;
	print(cifrarCesar(mensagem, deslocamento));
}
