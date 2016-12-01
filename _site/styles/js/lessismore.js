/*!
 * Adapted from Bootstrap docs JavaScript
 */


! function($) {

    $(function() {

        orderTheLeftNavigations();

        function orderTheLeftNavigations() {
            $('#navigation .sidenav').html($("#markdown-toc").html());
            $('#navigation .sidenav ul').addClass("nav");
            $("#markdown-toc").remove();

            // 添加Bootstrap表格样式 table-hover 
            $(".docs-content table").addClass("table table-hover");
        }

        $(window).load(repairTheImagesWhichCrossTheMaxWidth);

        function repairTheImagesWhichCrossTheMaxWidth() {
            var images = $(".docs-content article img");
            if (images != undefined) {
                images.width("100%");
            }
        }
    })

}(jQuery)
