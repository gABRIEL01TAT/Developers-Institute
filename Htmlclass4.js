//javascript
//Exercise 1
let x = 50;
let y = 20;
if (x > y){
    console.log("x is the biggest number")
}else{
    console.log("hello")
}


//
//Exercise 2
let newDog = "Chihuahua"
console.log(newDog.length)
console.log(newDog.toUpperCase())
console.log(newDog.toLowerCase())

if (newDog==="Chihuahua"){
    console.log("I love Chihuahuas, its my favorite dog breed")
}else{console.log("I dont care, I prefer cats")}

//Exercise 3
let q = prompt("Enter a number")
let c = q%2
if (c==0){
    console.log("The number is even")
    // alert("the number is even")
}else{
    console.log("The number is odd")
   // alert("the number is odd")
}


//Exercise4
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
let a = users.length;
    console.log(a)
if (a==0) {
    alert('There is no user online');
}
else if(a==2){
    alert(`${users[0]} and ${users[1]} are online`)
}
else{
    alert(`${users[0]} , ${users[1]} and ${a-2} are online`)
}