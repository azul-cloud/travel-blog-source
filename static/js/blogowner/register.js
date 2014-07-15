$(document).ready(function(){
  $( "#id_site_name" ).focus(function () {
    $( ".submission-form-help" ).text("What is the name of your Travel Blog site?");
  });

  $( "#id_url" ).focus(function () {
    $( ".submission-form-help" ).text("Full URL that we will send people to.");
  });

  $( "#id_region" ).focus(function () {
    $( ".submission-form-help" ).text("Pick a country or continent that your site is most relevant for. Your blogsite will return in searches for that region.");
  });

  $( "#id_category" ).focus(function () {
    $( ".submission-form-help" ).text("Pick a category you would like your blog to show up when people search for that category.");
  });

  $( "#id_twitter" ).focus(function () {
    $( ".submission-form-help" ).text("Do you have a Twitter handle for this travel blog site? You don't need to put the URL, just the handle. i.e. travelblogsrc");
  });

  $( "#id_facebook" ).focus(function () {
    $( ".submission-form-help" ).text("Do you have a Facebook page for this travel blog site? Don't include the URL, just the name. i.e. travelblogsource");
  });

  $( "#id_quick_info" ).focus(function () {
    $( ".submission-form-help" ).text("Up to 300 characters describing your site.");
  });
});