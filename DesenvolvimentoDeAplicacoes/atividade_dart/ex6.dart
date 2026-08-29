void main() {
	List<int> pares = [];
	for (int i = 1; i <= 20; i++) {
		if (i % 2 == 0) {
			pares.add(i);
		}
	}
	print(pares);
}
