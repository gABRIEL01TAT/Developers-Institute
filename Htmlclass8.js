/*
let grade = parseInt(prompt());

let grade_letters = "";

if (grade>90){
    grade_letters = "A";
    console.log('You have passed A grade');
}
else if (80< grade && grade<=90) {
    grade_letters = "B";
    console.log('You have passed B grade');
}
else if (70< grade && grade<=80) {
    grade_letters = "C";
    console.log('You have passed C grade');
}
else if (70< grade && grade<=60) {
    grade_letters = "D";
    console.log('You have passed D grade');
}
else  {
    grade_letters = "E"
    console.log('You have failed E grade');
}
*/


let verb = prompt("Enter the verb")

if (verb.length >=3 && verb.slice(-3)!="ing") {
    alert(verb + "ing")
}

else if (verb.length >=3 && verb.slice(-3)==="ing"){
    alert(verb + "ly")
}
else{
    alert(verb)
}
