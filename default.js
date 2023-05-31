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

// var num1 = 20;
// var num2 = 10;
// var num3 = "10";
// var num4 = 20;
// var num5 = 15;

// console.log('일반크기 비교')
// console.log(num1 > num2, num1, '>', num2 )
// console.log(num1 >= num2, num1, '>=', num2 )
// console.log(num1 < num2, num1, '<', num2 )
// console.log(num1 <= num2, num1, '<=', num2 )

// console.log('같은지 여부 비교')
// console.log(num1 == num4, num1, '==', num4 )
// console.log(num1 != num4, num1, '!=', num4 )

// console.log('=== 비교 (타입)')
// console.log(num1 === num3, num1, '===', num3 )
// console.log(num2 === num3, num2, '===', num3 )
// console.log(num2 == num3, num2, '==', num3 )

// console.log('and(&&) or 연산자(||)')
// console.log('num1 > num2 && num1 >num5 : ', num1 > num2 && num1 >num5)
// console.log('num1 > num2 || num2 >num5 : ', num1 > num2 || num2 >num5)


// var num1 = parseInt(prompt('첫 번째 숫자 입력 : '))
// var num2 = parseInt(prompt('두 번째 숫자 입력 : '))

// if (num1 > num2) {
//     console.log('큰 수는 : num1 ' + num1)
// }
    
// if (num1 < num2) {
//     console.log('큰 수는 : num2 ' + num2)
// }

// if (num1 == num2) {
//     console.log('같은 수')
// }

// if (num1 > num2) {
//     console.log('큰 수는 : num1 ' + num1)
// } else if (num1 < num2) {
//     console.log('큰 수는 : num2 ' + num2)
// } else if (num1 == num2) {
//     console.log('같은 수')
// }

// if (num1 > num2) {
//     console.log('큰 수는 : num1 ' + num1)
// } else if (num1 < num2) {
//     console.log('큰 수는 : num2 ' + num2)
// } else {
//     console.log('같은 수')
// }

// var letter = prompt("Enter a letter : ");
// letter = letter.toLowerCase();

// if (letter == 'a' || letter == 'e' || letter == 'i' || letter == 'o' || letter == 'u') {
//     console.log('Vowel')
// } else {console.log('Consonant')}

// var digit = parseInt(prompt("숫자 입력"))

// switch(digit) {
//     case 0: 
//         document.write('Zero');
//         break;
//     case 1: 
//         document.write('One');
//         break;
//     case 2: 
//         document.write('Two');
//         break;
//     case 3: 
//         document.write('Three');
//         break;
//     case 4: 
//         document.write('Four');
//         break;
//     case 5: 
//         document.write('Five');
//         break;
//     case 6: 
//         document.write('Six');
//         break;
//     case 7: 
//         document.write('Seven');
//         break;
//     case 8: 
//         document.write('Eight');
//         break;
//     case 9: 
//         document.write('Nine');
//         break;
//     default:
//         document.write('Not a digit');
//         break;

// }

// var i = 1 
// do {
//     document.write('멋쟁이사자i : ' + i++ + "<br/>")
// } while (i < 1)

// document.write("<br/>")

// var j = 1 
// while (j < 1) {
//     document.write('멋쟁이사자j : ' + j++ + "<br/>")
// }

// // break
// for (var i = 1; i <= 100; i++ ) {
//     if (i == 20) {
//         break;
//     }
//     document.write(i+"<br/>")
// }
// document.write("---------------------------------------" + "<br/>")
// // continue
// for (var j = 1; j <= 100; j++ ) {
//     if (j == 20) {
//         continue;
//     }
//     document.write(j+"<br/>")
// }

// // 함수
// // 매개변수 없는 함수
// function message() {
//     document.write("Hello without parameter" + "<br/>")
// }

// // 매개변수 한 개 있는 함수
// function messageName(name) {
//     document.write("Hello " + name + "<br/>")
// }

// // 매개변수 두 개 있는 함수
// function addition(num1, num2) {
//     var sum = num1 + num2
//     document.write(sum)
// }

// // 값을 반환하는 함수 return
// function square(num) {
//     return num * num
// }

// message();
// messageName("Ted");
// addition(1, 2);
// document.write("<br/>");
// document.write("2 * 2 = " + square(2) + "<br/>");

// 즉시 실행 함수
(function display(message) {
    console.log(message);
})("hi") 

// 함수를 변수에 선언할 수도 있음.
var display2 = function displayMessage(message) {
    console.log(message);
}
display2("Hi");

(function addNumbers(num1, num2){
    console.log(num1 + num2)
}(3, 4));

























