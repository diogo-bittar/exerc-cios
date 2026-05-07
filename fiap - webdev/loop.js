//Aula JS sobre loops

//while 
function aumentarNumero(numero){
    while(numero < 10){
        console.log(numero);
        numero++; //somando até chegar em 10
        //i-- diminui
        //i+=2 soma de dois em dois
    }
}

//-----------------------------------------------------------//
//exercício 
//function numeroRegressivo(numer){
    //while (numer >= 1){
        //console.log(numer)
        //numer--
    //}
//}
//const numer = Number(prompt('Informe um número por favor: '))

//------------------------------------------------------------//

//do while
let count = 0; //criar variável fora
do{
    console.log(count);
    count++;
} while(count < 5)
//------------------------------------------------------------//
//ex2
let nome;
let idade;
let salario;
let genero;
let civil;

do{
    nome = prompt('Informe o seu nome: ');
    if(nome.length < 3){
        alert('Informe um nome de verdade: ')
    }
} while(nome.length < 3);


do{
    idade = Number(prompt('Agora, informe a sua idade: '));
    if(idade <=0){
        alert('Idade (-)negativa não existe.')
    }
    else if(idade > 150){
        alert('Idade ultrapassou o limite.')
    }
} while(idade <= 0 || idade >= 150);

do{
    salario = parseFloat(prompt('Mais um detalhe, qual o seu salário?: '))
    if(salario <= 0){
        alert('Informe o seu salário, valores abaixo de zero (0) ou igual, não passam. :)')
    }
} while(salario <= 0);

do{
    genero = prompt('E qual seria o seu gênero? (F / M): ').toUpperCase();
    if(genero !== "F" && genero !== "M"){
        alert('Informe um gênero existente.')
    }
    
}while(genero !== "F" && genero !== "M")

do{
    civil = prompt('E qual seria o seu estado civil? (S / C / V / D): ').toUpperCase();
    if(civil !== "S" && civil !== "C" && civil !== "V" && civil !== "D"){
        alert('Informe um estado civil existente.')
    }
    
}while(civil !== "S" && civil !== "C" && civil !== "V" && civil !== "D")

alert(`Suas informações abaixo:
    \nNOME:${nome}
    \nIDADE:${idade}
    \nGÊNERO:${genero}
    \nSALÁRIO:${salario}
    \nESTADO CIVIL:${civil}`)
//----------------------------------------------------------------------------------
//ex 3


//for

//loops infinitos