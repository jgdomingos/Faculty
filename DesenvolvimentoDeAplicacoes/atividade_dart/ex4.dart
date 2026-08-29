import 'dart:io';

void main() {
	double celsius = double.parse(stdin.readLineSync()!.trim());
	double fahrenheit = celsius * 9 / 5 + 32;
	print(fahrenheit);
}
