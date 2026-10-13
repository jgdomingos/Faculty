import 'package:flutter/material.dart';

void main() {
  runApp(const MeuMiniApp());
}

// 1. DART: Modelo de Dados

class Item {
  String titulo;
  bool isConcluido;

  Item({required this.titulo, this.isConcluido = false});
}

class MeuMiniApp extends StatelessWidget {
  const MeuMiniApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Live Code Flutter',
      theme: ThemeData(primaryColor: Colors.purple),
      home: const TelaPrincipal(),
    );
  }
}

// 2. Flutter: Tela reativa (StatefulWidget)

class TelaPrincipal extends StatefulWidget {
  const TelaPrincipal({super.key});

  @override
  State<TelaPrincipal> createState() => _TelaPrincipalState();
}

class _TelaPrincipalState extends State<TelaPrincipal> {
  // Controlador para o campo de texto
  final TextEditingController _controller = TextEditingController();

  // Lista em memória
  final List<Item> _itens = [
    Item(titulo: 'Revisar Conceitos de DART'),
    Item(titulo: 'Criar primeiro Widget Flutter'),
  ];

  // Filtro atual
  String _filtroAtual = 'Todas';

  // 1) ADICIONAR ITEM + SNACKBAR
  void _adicionarItem() {
    // 2) VALIDAÇÃO DE TAREFA VAZIA
    if (_controller.text.trim().isEmpty) {
      showDialog(
        context: context,
        builder: (context) {
          return AlertDialog(
            title: const Text('Atenção'),
            content: const Text('O título da tarefa não pode estar vazio!'),
            actions: [
              TextButton(
                onPressed: () {
                  Navigator.pop(context);
                },
                child: const Text('OK'),
              ),
            ],
          );
        },
      );

      return;
    }

    setState(() {
      _itens.add(Item(titulo: _controller.text.trim()));

      _controller.clear();
    });

    // 3) SNACKBAR
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(
        content: Text('Tarefa adicionada com sucesso!'),
        duration: Duration(seconds: 2),
      ),
    );
  }

  // Alternar status da tarefa
  void _alternarStatus(int index) {
    setState(() {
      _itens[index].isConcluido = !_itens[index].isConcluido;
    });
  }

  // 4) CONFIRMAÇÃO DE EXCLUSÃO
  void _removerItem(int index) {
    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: const Text('Confirmar exclusão'),
          content: const Text('Tem certeza que deseja apagar esta tarefa?'),
          actions: [
            TextButton(
              onPressed: () {
                Navigator.pop(context);
              },
              child: const Text('Cancelar'),
            ),
            ElevatedButton(
              onPressed: () {
                setState(() {
                  _itens.removeAt(index);
                });

                Navigator.pop(context);
              },
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.red,
                foregroundColor: Colors.white,
              ),
              child: const Text('Apagar'),
            ),
          ],
        );
      },
    );
  }

  // 5) FILTRAR LISTA
  List<Item> _itensFiltrados() {
    if (_filtroAtual == 'Pendentes') {
      return _itens.where((item) => !item.isConcluido).toList();
    }

    if (_filtroAtual == 'Concluídas') {
      return _itens.where((item) => item.isConcluido).toList();
    }

    return _itens;
  }

  @override
  Widget build(BuildContext context) {
    // Estatísticas
    final int total = _itens.length;

    final int concluidas = _itens.where((item) => item.isConcluido).length;

    final int pendentes = total - concluidas;

    // Lista de acordo com o filtro
    final List<Item> itensExibidos = _itensFiltrados();

    return Scaffold(
      appBar: AppBar(
        title: const Text('Minhas Tarefas - Live Code'),
        backgroundColor: Colors.orange,
        foregroundColor: Colors.white,
      ),

      body: Padding(
        padding: const EdgeInsets.all(16.0),

        child: Column(
          children: [
            // ESTATÍSTICAS
            Container(
              width: double.infinity,
              padding: const EdgeInsets.all(12),
              decoration: BoxDecoration(
                color: Colors.orange.shade50,
                borderRadius: BorderRadius.circular(10),
              ),
              child: Text(
                'Total: $total | Concluídas: $concluidas | Pendentes: $pendentes',
                textAlign: TextAlign.center,
                style: const TextStyle(
                  fontWeight: FontWeight.bold,
                  fontSize: 16,
                ),
              ),
            ),

            const SizedBox(height: 15),

            // CAMPO DE ENTRADA + BOTÃO
            Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: _controller,
                    decoration: const InputDecoration(
                      labelText: 'Nova tarefa',
                      border: OutlineInputBorder(),
                    ),
                    onSubmitted: (_) {
                      _adicionarItem();
                    },
                  ),
                ),

                const SizedBox(width: 10),

                ElevatedButton(
                  onPressed: _adicionarItem,
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.orange,
                    padding: const EdgeInsets.all(16),
                  ),
                  child: const Icon(Icons.add, color: Colors.white),
                ),
              ],
            ),

            const SizedBox(height: 20),

            // FILTROS
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                ChoiceChip(
                  label: const Text('Todas'),
                  selected: _filtroAtual == 'Todas',
                  onSelected: (_) {
                    setState(() {
                      _filtroAtual = 'Todas';
                    });
                  },
                ),

                ChoiceChip(
                  label: const Text('Pendentes'),
                  selected: _filtroAtual == 'Pendentes',
                  onSelected: (_) {
                    setState(() {
                      _filtroAtual = 'Pendentes';
                    });
                  },
                ),

                ChoiceChip(
                  label: const Text('Concluídas'),
                  selected: _filtroAtual == 'Concluídas',
                  onSelected: (_) {
                    setState(() {
                      _filtroAtual = 'Concluídas';
                    });
                  },
                ),
              ],
            ),

            const SizedBox(height: 20),

            // LISTA DINÂMICA
            Expanded(
              child: itensExibidos.isEmpty
                  ? const Center(child: Text('Nenhuma tarefa encontrada'))
                  : ListView.builder(
                      itemCount: itensExibidos.length,

                      itemBuilder: (context, index) {
                        final item = itensExibidos[index];

                        // Encontrar o índice original
                        final int indexOriginal = _itens.indexOf(item);

                        return Card(
                          elevation: 2,

                          child: ListTile(
                            leading: Checkbox(
                              value: item.isConcluido,

                              onChanged: (_) {
                                _alternarStatus(indexOriginal);
                              },
                            ),

                            title: Text(
                              item.titulo,

                              style: TextStyle(
                                decoration: item.isConcluido
                                    ? TextDecoration.lineThrough
                                    : TextDecoration.none,
                              ),
                            ),

                            trailing: IconButton(
                              icon: const Icon(Icons.delete, color: Colors.red),

                              onPressed: () {
                                _removerItem(indexOriginal);
                              },
                            ),
                          ),
                        );
                      },
                    ),
            ),
          ],
        ),
      ),
    );
  }
}
