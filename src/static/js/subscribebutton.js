function myFunction(id) {
    var x = document.getElementById("myDIV"+id);
    
    if (x.innerText == "Subscribe") {
     
      // x.innerHTML = "Unsubscribe";
      // alert("you Subscribed at this category");
      console.log("hello");
      // sessionStorage.setItem("myDIV"+id, 'Unsubscribe');
      // x.innerHTML = sessionStorage.getItem("myDIV"+id);
      
      
    } else {
      // x.innerHTML = "Subscribe"; 
      // alert("you Unsubscribed from this category");
      console.log("bye");
       // sessionStorage.setItem("myDIV"+id, 'Subscribe');
       //  x.innerHTML = sessionStorage.getItem("myDIV"+id);
      
      
    }
  } 