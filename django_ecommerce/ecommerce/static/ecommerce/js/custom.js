// start search buttons
$(document).ready(function(){
    $("#search-button-confirm").click(function (){
        var category_option
        var input_value
        category_option = document.getElementById("search-category-select-option")[document.getElementById("search-category-select-option").selectedIndex].text
        input_value = document.getElementById("search-category-input").value
        if (!input_value){
            input_value = " "
            };
        window.location.replace(
            window.location.origin + "/catalog-search/" + category_option + "-" + input_value + "/"
        );
    });
});

$(document).ready(function(){
    $("#search-button-confirm-on-scroll").click(function (){
        var category_option
        var input_value
        category_option = document.getElementById("search-category-select-option-on-scroll")[document.getElementById("search-category-select-option-on-scroll").selectedIndex].text
        input_value = document.getElementById("search-category-input-on-scroll").value
        if (!input_value){
            input_value = " "
            };
        window.location.replace(
            window.location.origin + "/catalog-search/" + category_option + "-" + input_value + "/"
        );
    });
});
// end search buttons