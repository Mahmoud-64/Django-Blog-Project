function myFunction(id) {
  var x = document.getElementById("myDIV"+id);
  
  if (x.innerText == "Subscribe") {
   
    x.innerHTML = "Unsubscribe";
    // alert("you Subscribed at this category");
    console.log("hello");
    
    
  } else {
    x.innerHTML = "Subscribe"; 
    // alert("you Unsubscribed from this category");
    console.log("bye");
    
  }
} 