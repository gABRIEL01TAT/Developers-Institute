// function userInfo (myAge) {
//     let mumAge = myAge*2;
//     let dadsAge = myAge*1.2;
//     console.log("My mum'sAge is",{mumAge}, "and my dadsAge is" ,{dadsAge});
// }
// userInfo(40);

// function info(myAge) {
//     let mumsAge = 2*myAge;
//     let ans = ("My age is",{mumsAge}," twice my age");
//     return ans
// }
// let ans = info(100)
// console.log(info(100))

let person= {
    firstName : "Sarah",
    eyeColor: "blue",
    eat : function () {
    console.log("My name is" + this.firstName + "I love chocolate")
    }
}