function input(a){
    document.frm.inp.value=document.frm.inp.value+a;
}

function eql(){
   var b = document.frm.inp.value ;
   if(b){
    document.frm.inp.value = eval(b)
   }

}

function bck(){
    var c = document.frm.inp.value;
    document.frm.inp.value = c.substring(0,c.length - 1);
}