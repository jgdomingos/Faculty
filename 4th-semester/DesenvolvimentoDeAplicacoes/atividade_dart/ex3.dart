import 'dart:io';

void main() {
  double raio = double.parse(stdin.readLineSync()!.trim());
  double pi = 3.14;
  double area = pi * raio * raio;
  print(area);
}
