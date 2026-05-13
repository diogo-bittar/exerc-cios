function verificarPalavra(frase, palavraBusca) {
  frase = frase.trim();

  if (frase.length < 5) {
    return "A frase é muito curta";
  }

  if (frase.toLowerCase().includes(palavraBusca.toLowerCase())) {
    return "A frase contém a palavra de busca";
  }

  return "A frase não contém a palavra de busca";
}

//

function lancarDados(n) {
  if (typeof n !== "number" || isNaN(n) || n <= 0 || n % 1 !== 0) {
    return "Inválido.";
  }

  let soma = 0;
  let maior = 0;
  let menor = 6;

  for (let i = 0; i < n; i++) {
    let roll = Math.floor(Math.random() * 6) + 1;

    soma += roll;

    if (roll > maior) {
      maior = roll;
    }

    if (roll < menor) {
      menor = roll;
    }
  }

  return `Lançamentos: ${n} | Soma: ${soma} | Maior: ${maior} | Menor: ${menor}`;
}

//

function descreverSoma(a, b) {
  if (
    typeof a !== "number" ||
    typeof b !== "number" ||
    isNaN(a) ||
    isNaN(b)
  ) {
    return "Valores inválidos.";
  }

  const resultado = a + b;

  return `A soma de ${a} e ${b} é ${resultado}.`;
}

//

function converterMoeda(valor, moedaAtual, moedaDestino = "USD") {
  if (typeof valor !== "number" || isNaN(valor) || valor < 0) {
    return "Valor inválido.";
  }

  if (moedaAtual !== "BRL") {
    return "Moeda de origem inválida.";
  }

  const taxas = {
    USD: 5.70,
    EUR: 6.20,
    GBP: 7.10
  };

  if (!taxas[moedaDestino]) {
    return "Moeda de destino inválida.";
  }

  const resultado = (valor / taxas[moedaDestino]).toFixed(2);

  return `R$ ${valor} = ${resultado} ${moedaDestino}`;
}

//

function calcularMulta(valorOriginal, diasAtraso) {
  if (
    typeof valorOriginal !== "number" ||
    typeof diasAtraso !== "number" ||
    isNaN(valorOriginal) ||
    isNaN(diasAtraso)
  ) {
    return "Valor inválido.";
  }

  if (valorOriginal < 0 || diasAtraso < 0) {
    return "Valor inválido.";
  }

  let total = valorOriginal;
  let dia = 1;

  if (diasAtraso > 0) {
    do {
      total += 10;
      dia++;
    } while (dia <= diasAtraso);
  }

  return `Total: R$ ${total.toFixed(2)}`;
}


console.log(verificarPalavra("Oi", "oi"));
// A frase é muito curta

console.log(verificarPalavra("  JavaScript é incrível  ", "javascript"));
// A frase contém a palavra de busca

console.log(verificarPalavra("JavaScript é incrível", "python"));
// A frase não contém a palavra de busca

console.log(lancarDados(9));
// Lançamentos: 5 | Soma: X | Maior: X | Menor: X

console.log(lancarDados(0));
// Inválido.

console.log(descreverSoma(3, 7));
// A soma de 3 e 7 é 10.

console.log(descreverSoma("3", 7));
// Valores inválidos.

console.log(converterMoeda(100, "BRL"));
// R$ 100 = 17.54 USD

console.log(converterMoeda(100, "BRL", "EUR"));
// R$ 100 = 16.13 EUR

console.log(calcularMulta(100, 3));
// Total: R$ 130.00