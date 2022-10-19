// function sum(n1 , n2){
//     return n1 + n2;
// }

// var a = sum(10,3);
// document.write(a)

function check(){
var num = parseInt(document.getElementById("num").value) , temp;


if(num%2==0){
    // temp = document.getElementById("ans");
    document.getElementById("ans").innerHTML ="even";
}else{
    document.getElementById("ans").innerHTML ="odd";
}
}