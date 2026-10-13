import 'dart:io';

void main() {
  List<String> partes = stdin.readLineSync()!.trim().split(RegExp(r'\s+'));
  double numero1 = double.parse(partes[0]);
  double numero2 = double.parse(partes[1]);
  print(numero1 + numero2);
}
