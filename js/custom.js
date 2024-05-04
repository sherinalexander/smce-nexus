$(document).ready(function() {
    // Select the alert by its ID
    var alert = $("#autoHideAlert");

    // Use setTimeout to hide the alert after 2 seconds
    setTimeout(function() {
        alert.addClass('fade-out');
        alert.alert('close'); 
    }, 2000);
  });