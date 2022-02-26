const arr_1 = ['사당', '방배', '교대','강남'];
const arr_2 = ['신사', '압구정', '옥수'];

// const와 let의 차이점
// const : 재할당이 불가능, let : 재할당이 가능

// join함수
let result = arr_1.join('-');
console.log(result);

// concat 함수
let result1 = arr_1.concat(arr_2);
console.log(result1);

// slice 함수
let result2 = arr_1.slice(1,4);
console.log(result2)


// sort 함수
let result3 = arr_1.sort()
console.log(result3)

// reverse 함수
let result4 = arr_1.reverse()
console.log(result4)