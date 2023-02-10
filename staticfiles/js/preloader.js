$(document).ready(function() {
    //Preloader
    preloaderFadeOutTime = 2000;
    function hidePreloader() {
        var preloader = $('.preloader');
        preloader.fadeOut(preloaderFadeOutTime);
    }
    hidePreloader();
});