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
console.log(result2);


// sort 함수
let result3 = arr_1.sort();
console.log(result3);

// reverse 함수
let result4 = arr_1.reverse();
console.log(result4);

// splice 함수 - 배열의 요소 대치
arr_1.splice(2, 1, "서초", "역삼");
console.log(arr_1);

// pop 함수
let data1 = arr_1.pop();  // arr1의 마지막 요소를 추출
let data2 = arr_2.shift(); // arr_2의 첫번째 것을 추출
console.log(data1, data2);

// push 함수
arr_1.push(data2)  // arr_1의 마지막에 data2를 넣기
console.log(arr_1)

// unshift 함수 
arr_2.unshift(data1)
console.log(arr_2)