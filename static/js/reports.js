$(document).ready(function(){
    $(".btn-report").click(function () {
        //get id
        report_id = (this).id.replace('btn-', 'report-');

        //set active button
        $(".btn-report").removeClass( "active" );
        $(this).toggleClass( "active" );

        //toggle hidden section
        $(".report-section").addClass( "hidden" );
        $("#" + report_id).removeClass( "hidden" );
    })
});