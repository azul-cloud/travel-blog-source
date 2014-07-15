$(document).ready(function(){

    function search() {
        //get search text
        text = $("#search-input-control").val();

        //redirect
        if(text){
            window.location = "/blogsearch/text/" + text + "/";
        }
    }

    //this function is to handel events while choosing a category
    $(".category-group-item").click(function () {
        $(".category-group-item").removeClass( "active" );
        $(this).toggleClass( "active" );

        //update button href
        var cat = $(this).attr('id');
        $("#go-btn").prop("href", "/blogsearch/category/" + cat + "/");
    });

    //this function is for handling events when choosing a continent/country
    $(".continent-group-item").click(function () {

        //actions on the Continent dropdown
        $(".continent-group-item").removeClass( "active" );
        $("#search-choice").removeClass( "hidden" );
        $(this).toggleClass( "active" );

        //get id to show the correct countries in dropdown
        var cont = $(this).attr('id');
        $("#go-btn").prop("href", "/blogsearch/region/" + cont + "/");

        //remove hidden to the country dropdown
        $(".country-item").addClass( "hidden" );
        $("." + cont).removeClass( "hidden" );
    });


    //enable tooltip
    $(function () { $("[data-toggle='tooltip']").tooltip(); });

    //handle DOM objects when clicking a search method
    $(".search-choice-btn").click(function () {

        //test if it is the first click
        if($("#region-section").hasClass("hidden") && $("#category-section").hasClass("hidden") && $("#search-text-section").hasClass("hidden")){

            //initial changes
            $("#search-header-text").addClass( "hidden" );
            $(".search-row").removeClass( "hidden" );
            $(".search-choice-btn").addClass("search-choice-btn-sm");
            $(".search-choice-initial").css("margin-top","20px");
        }

        //determine what was pressed and unhide appropriate section
        var search_choice = $(this).attr('id');
        if (search_choice == "region" ){
            $("#region-section").removeClass( "hidden" );

            if ($("#div-go-btn").hasClass( "hidden" )){
                $("#div-go-btn").removeClass( "hidden" );
            }

            if (!$("#category-section").hasClass( "hidden" )){
                $("#category-section").addClass( "hidden" );
            }

            if (!$("#search-text-section").hasClass( "hidden" )){
                $("#search-text-section").addClass( "hidden" );
            }
        }
        else if (search_choice == "category" ){
            $("#category-section").removeClass( "hidden" );

            if ($("#div-go-btn").hasClass( "hidden" )){
                $("#div-go-btn").removeClass( "hidden" );
            }

            if (!$("#region-section").hasClass( "hidden" )){
                $("#region-section").addClass( "hidden" );
            }

            if (!$("#search-text-section").hasClass( "hidden" )){
                $("#search-text-section").addClass( "hidden" );
            }
        }
        else if( search_choice == "text" ){
            $("#search-text-section").removeClass( "hidden" );
            $("#search-input-control").focus();

            if (!$("#div-go-btn").hasClass( "hidden" )){
                $("#div-go-btn").addClass( "hidden" );
            }

            if (!$("#region-section").hasClass( "hidden" )){
                $("#region-section").addClass( "hidden" );
            }

            if (!$("#category-section").hasClass( "hidden" )){
                $("#category-section").addClass( "hidden" );
            }
        }

        //call go function when enter is pressed
        $("#search-input-control").keyup(function (e) {
            if (e.keyCode == 13) {
                search();
            }
        });

         $("#search-go").click(function(){
            search();
        });

    })
});