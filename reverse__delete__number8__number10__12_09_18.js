let num1 = `qwerty`, // ввод с консоли возможен только в node.js V8 так что это некая эмуляция ввода
	num2 = `1234567`,
	num3 = '1234',
	num4 = '2322';


function task1(num1){ // реверс надписи
let num1Res = '';

	for(let i = 0;i<num1.length;i++){

		num1Res += num1[num1.length - i - 1];
	}

	return num1Res;
}

function task2(num2){ // удаление четных цифр
let num2Res = '' ;

	for(let i = 0; i < num2.length; i++){
		if(num2[i] % 2 > 0){
			num2Res += num2[i];
		} 
	}

	return num2Res;
}


function task3(num3){ // перевод из 10 в 8 
let num3Res = [] ;

	for(;num3 > 0;){

		num3Res.unshift(num3 % 8 + '');
		num3 = Math.floor(num3 / 8);
	}

	return num3Res.join('');
}

function task4(num4){ // перевод из 8 в 10 
let num4Res = 0 ;

	for(let i = 0;i < num4.length; i++){

		num4Res += (+`${num4[num4.length - i - 1]}`) * Math.pow(8, i);
	}

	return num4Res;
}

// вывод элементов, чтобы проверить код достаточно вставить в консоль браузера
console.log(`task1 -- ${task1(num1)} \ntask2 -- ${task2(num2)}\ntask3 -- ${task3(num3)}\ntask4 -- ${task4(num4)}`);


