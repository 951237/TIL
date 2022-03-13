console.log('## for ##')
const color = ['red', 'ble', 'green'];
for (let i = 0; i < color.length; i++) {
    console.log(color[i]);
}
console.log('');

console.log('## while ##');
let i = 0;
while(color[i] != null){
    console.log(color[i]);
    i++;
}
console.log('');

console.log('## forEach ##');
color.forEach(function(value){
    console.log(value);
});
console.log('');

console.log('## forEach with Arrow');
color.forEach(value => console.log(value));
``
