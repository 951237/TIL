const caculator = {
    plus: function(a, b) {
        return a + b;
    },
    minus: function(a, b) {
        return a - b;
    },
    multi: function(a, b) {
        return a * b;
    },
    divide: function(a, b) {
        return a / b;
    }
}

const plus = caculator.plus(12, 5);
const minus = caculator.minus(12, 5);
const multi = caculator.multi(12, 5);
const divide = caculator.divide(12, 5);
console.log(plus)
console.log(minus)
console.log(multi)
console.log(divide)