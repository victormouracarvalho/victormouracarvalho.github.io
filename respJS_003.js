




function primos (){
    console.log ('Q2')
    var aux = Number.parseInt(Document.getElementById('numeroQ2').value);
    primos.push(2);
    for (let numero = 3; numero <= aux; numero += 2) {
        let chk = true;
        for (let i = 0; i < primos,lenght; i++) {
            if(numero % primos [i] === 0) {
                chk = false;
                break;


            }
        }
       if (chk) {primos.push(numero); }
}


function isPrimo (numero) {
    if(numero <2 || numero % 2 === 0) { return false; }
    for(let i = 3; i <= Math.sqrt(numero); i += 2) {
        if(numero % i === 0) { return false; }

    }
    return true;
}



function Q2() {
    console.log('Q2alt');
    var aux = document.getElementById('numerosQ1').value;
    // Segue aqui seu código
    for(let i = 0; i <= aux; i++) {
        if(isPar(i)) {
            pares.push(i);
        
        }
    }
    console.log(pares);
    document.getElementById('RQ2alt').innerHTML = primos2;

}






// funções que estão funcionando abaixo =>






//
//
//

var pares = [];
function isPar (numero) {
    if (numero%2 == 0) {
        return true;
    } else {
        return false;
    }
}
// Crie aqui suas funções de apoio

function Q1() {
    console.log('Q1');
    var aux = document.getElementById('numeroQ1').value;
    // Segue aqui seu código
    for(let i = 0; i <= aux; i++) {
        if(isPar(i)) {
            pares.push(i);
        
        }
    }
    console.log(pares);
    document.getElementById('RQ1').innerHTML = pares;

}









//
//
//









function Q3() {
    console.log('Q3');
    var novaString = document.getElementById('novaString').value;
    document.getElementById('RQ3').innerHTML = listaStrings2;
    var listaStrings = [];
    
    function maiscula (novaString) {
        return ('novaString').toUpperCase
    }

    listaStrings.push(novaString);
    listaStrings2 = listaStrings.replace('novaString', maiscula);
    console.log(listaStrings2)
  
    
    


    
}

//
//
//
//








// Crie aqui suas funções de apoio

function Q4() {
    console.log('Q4');
    var aux = document.getElementById('numerosQ4').value;
    // Segue aqui seu código
    var numerosQ4 = [];
    var ordenados = [];
}

    numerosQ4.push(aux);


function swap(numerosQ4, leftIndex, rightIndex){
    var temp = numerosQ4[leftIndex];
    numerosQ4[leftIndex] = numerosQ4[rightIndex];
    numerosQ4[rightIndex] = temp;
}
function partition(numerosQ4, left, right) {
    var pivot   = numerosQ4[Math.floor((right + left) / 2)], 
        i       = left, 
        j       = right; 
    while (i <= j) {
        while (numerosQ4[i] < pivot) {
            i++;
        }
        while (numerosQ4[j] > pivot) {
            j--;
        }
        if (i <= j) {
            swap(numerosQ4, i, j);
            i++;
            j--;
        }
    }
    return i;
}

function quickSort(numerosQ4, left, right) {
    var index;
    if (numerosQ4.length > 1) {
        index = partition(numerosQ4, left, right); 
        if (left < index - 1) { 
            quickSort(numerosQ4, left, index - 1);
        }
        if (index < right) { 
            quickSort(numerosQ4, index, right);
        }
    }
    return numerosQ4;
}

var sortedArray = quickSort(numerosQ4, 0, numerosQ4.length - 1);
console.log(sortedArray); 
document.getElementById('RQ4').innerHTML = sortedArray ;

