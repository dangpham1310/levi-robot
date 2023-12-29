// script.js

// You can add your custom JavaScript code here

// Example: Changing the active state of the navbar link
document.addEventListener("DOMContentLoaded", function() {
    // Get all the navbar links
    var navLinks = document.querySelectorAll(".nav-link");

    // Add click event listeners to each link
    navLinks.forEach(function(link) {
        link.addEventListener("click", function() {
            // Remove the active class from all links
            navLinks.forEach(function(link) {
                link.classList.remove("active");
            });

            // Add the active class to the clicked link
            this.classList.add("active");
        });
    });
});
