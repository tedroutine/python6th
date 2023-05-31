// document.write("hello world!");
// document.write("<h1>Welcome to JS</h1>");

// console.log("welcome to JS")
// console.warn("welcome to JS")
// console.error("welcome to JS")

// alert("welcome to JS")

// console.log(typeof 123);
// console.log(typeof 123.5);
// console.log(typeof "123");
// console.log(typeof true);
// console.log(typeof -1);

// var car
// var car = ""
// var person = {firstName: "John", lastName: "Lee", age: 50, eyeColor: "blue"}
// console.log(person)
// console.log(typeof person)
// person = null
// console.log(person)
// console.log(typeof person)

// person1 = null
// console.log(person1)
// console.log(typeof person1)

// var name = "Ted Lee";
// var age = 29;
// var cgpa = 3.92;
// var lineBreak = "<br/>"

// document.write("name is " + name + lineBreak);
// document.write("age is " + age + lineBreak);

// var lastName = "Lee";
// var firstName = "Ted";

// var fullName =  firstName + " " + lastName;
// console.log(fullName)

// var num1 = 20
// var num2 = 30
// var sum = num1 + num2
// console.log(sum)

// var text = prompt("Enter Your Name");
// document.write("Your Name : " + text + "<br/>");

// var len = text.length
// document.write("Number of characters : " + len + "<br/>");

// document.write(text.charAt(2) + "<br/>")

// document.write(text.toUpperCase() + "<br/>")
// document.write(text.toLowerCase() + "<br/>")

// var text1 = " hi"
// var text2 = "bye"
// var text3 = text1.concat(text2);
// document.write(text3 + "<br/>")

// var text4 = "hello";
// var result = text4.slice(0,2)
// document.write(result + "<br/>")
// var result2 = text4.split('e')
// document.write(result2 + "<br/>")

// var num = 20
// num = num.toString();
// console.log(typeof num)

// var x = 2.56
// console.log(x.toFixed(1), typeof x.toFixed(1))
// console.log(x.toFixed(2))

// var x = 2.56
// console.log(x.toPrecision(1), typeof x.toPrecision(1))
// console.log(x.toPrecision(2))

// console.log(Number(true))
// console.log(Number(false))
// console.log(Number("10"))
// console.log(Number(" 10"))
// console.log(Number("10.25"))

// var num1 = parseInt(prompt("enter first number"))
// var num2 = parseInt(prompt("enter second number"))
// var lineBreak = "<br/>"

// var result = num1 + num2
// document.write("sum is : " + result + lineBreak)

// var result = num1 - num2
// document.write("sub is : " + result + lineBreak)

// var result = num1 * num2
// document.write("multiple is : " + result + lineBreak)

// var result = num1 / num2
// document.write("devide is : " + result + lineBreak)

// var result = num1 % num2
// document.write("remain is : " + result + lineBreak)

// var base = parseFloat(prompt("enter 밑변 : "))
// var height = parseFloat(prompt("enter 높이 : "))

// var area = base * height * 1
// document.write("Area is : " + area)

// var cels = parseFloat(prompt("섭씨 입력 : "))
// var farn = cels * (9 / 5) + 32
// document.write("화씨 : " + farn)

var num1 = 20;
var num2 = 10;
var num3 = "10";
var num4 = 20;
var num5 = 15;

console.log('일반크기 비교')
console.log(num1 > num2, num1, '>', num2 )
console.log(num1 >= num2, num1, '>=', num2 )
console.log(num1 < num2, num1, '<', num2 )
console.log(num1 <= num2, num1, '<=', num2 )

console.log('같은지 여부 비교')
console.log(num1 == num4, num1, '==', num4 )
console.log(num1 != num4, num1, '!=', num4 )

console.log('=== 비교 (타입)')
console.log(num1 === num3, num1, '===', num3 )
console.log(num2 === num3, num2, '===', num3 )
console.log(num2 == num3, num2, '==', num3 )

console.log('and(&&) or 연산자(||)')
console.log('num1 > num2 && num1 >num5 : ', num1 > num2 && num1 >num5)
console.log('num1 > num2 || num2 >num5 : ', num1 > num2 || num2 >num5)










