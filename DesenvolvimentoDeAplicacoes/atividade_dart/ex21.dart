import 'dart:io';

List<String> traduzirRNA(String rna) {
  Map<String, String> tabelaCodons = {
    'AUG': 'Metionina',
    'UUU': 'Fenilalanina',
    'UUC': 'Fenilalanina',
    'UUA': 'Leucina',
    'UUG': 'Leucina',
    'UCU': 'Serina',
    'UCC': 'Serina',
    'UCA': 'Serina',
    'UCG': 'Serina',
    'UAU': 'Tirosina',
    'UAC': 'Tirosina',
    'UGU': 'Cisteína',
    'UGC': 'Cisteína',
    'UGG': 'Triptofano',
    'UAA': 'STOP',
    'UAG': 'STOP',
    'UGA': 'STOP',
  };

  String sequencia = rna.replaceAll(' ', '');
  List<String> proteinas = [];

  for (int i = 0; i + 3 <= sequencia.length; i += 3) {
    String codon = sequencia.substring(i, i + 3);
    String? aminoacido = tabelaCodons[codon];

    if (aminoacido == 'STOP') {
      break;
    }
    if (aminoacido != null) {
      proteinas.add(aminoacido);
    }
  }

  return proteinas;
}

void main() {
  String rna = stdin.readLineSync()!.trim();
  print(traduzirRNA(rna));
}
