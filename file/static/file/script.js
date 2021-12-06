$(document).ready(function(){

    // Navbar sticky
    $(window).scroll(function(){
        if(this.scrollY > 20){
            $('.navbar').addClass("sticky")
        }else
        {
            $('.navbar').removeClass("sticky")
        }
    });

    // Type Anime
    var typed = new Typed(".typing",{
        strings: ["Developer","Data Analyst"],
        typeSpeed: 100,
        backSpeed: 60,
        loop: true
    });

    var typed = new Typed(".typing-2",{
        strings: ["Developer","Data Analyst"],
        typeSpeed: 100,
        backSpeed: 60,
        loop: true
    });

    // owl carousel
    $('.carousel').owlCarousel({
        margin: 20,
        autoplayTime: 2000,
        autoplayHoverPause: true,
        responsive: {
            0:{
                items: 1,
                nav: false
            },

            600:{
                items: 2,
                nav: false
            },

            1000:{
                items: 3,
                nav: false
            }
        }
    });
});
