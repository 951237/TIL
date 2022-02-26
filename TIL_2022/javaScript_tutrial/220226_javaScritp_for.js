// 중첩 for문 구구단 출력하기 
// 문자 출력은 큰따옴표와 더하기로 구성


// 구구단 출력
// for (let i = 1; i <= 9; i++){
//     for (let j = 1; j <10; j++){
//         console.log(i + " * " + j + " = " + i * j );
//     }
//     console.log("");
// }

// 1부터 25까지 5개 단위로 출력하기 
// let result = '';
// let k = 1
// for (let i = 1; i <= 25; i++){
//     if (i % 5 == !0 ){
//         result += "\n"
//     }
//     result += i + '\t';
// }

// console.log(result);

// 곱하기를 옆으로 출력하기
let result = '';
for (let i = 1; i <10; i++){
    for(let j = 2; j < 13; j++){
        result += j + '*' + i + '=' + j*i + '\t';
    }
    result += "\n";
}
console.log(result);