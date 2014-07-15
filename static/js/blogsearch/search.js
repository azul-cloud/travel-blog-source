$(document).ready(function(){
    window.scrollTo(0,150);
    $(".rating").jRating();
    $("#region-table").dataTable();

    $(".rating.jDisabled").click(function() {
        $('#myModal').modal();
    })

    $('.blog-site-link').click(function() {
        id = (this).id
        if( $( this ).closest('tr').hasClass("search-highlight") ) {
            sponsor = "HIGH"
        }
        else if( $( this ).closest('tr').hasClass("search-top") ) {
            sponsor = "TOP"
        }
        else {
            sponsor = "NONE"
        }

        //Record the blogsite click
        $.post(
           "/blogsearch/blogsiteclick/",
            {
    			"blog_id" : id,
    			"origin" : "SEARCH",
    			"sponsor" : sponsor
    		},
            function(data) {
              alert("Response: " + data);
            },
    		'json'
        );
    });

    //record the click for bannerclick
    $('.banner-pic').click(function() {
        id = (this).id
        sponsor = "BANNER"

        $.post(
           "/blogsearch/bannerpicclick/",
            {
    			"banner_pic_id" : id
    		},
            function(data) {
              alert("Response: " + data);
            },
    		'json'
        );
    });
});