define(['jquery.min.js'], function() {

    function goTop(ct) {
        this.ct = ct;
        this.target = $('<div id="return-top">回到顶部</div>');
        var $returnTop = this.target;
        this.createNode();
        this.showBtn();
        this.gotop();
    };

    goTop.prototype = {
        showBtn: function() {
            $(window).on('scroll', function() {
                var top = $(this).scrollTop();
                console.log(top);
                if (top > 50) {
                    $returnTop.show();
                    $("#return-top").css({
                        position: "fixed";
                        bottom: 10 px;
                        right: 10 px;
                        border: 1 px solid;
                        padding: 10 px;
                        cursor: pointer;
                        display: none;
                        background: black;
                        color: white;
                    })
                } else {
                    $returnTop.hide();
                }
            });
        };
        gotop: function() {
            $returnTop.on('click', function() {
                $(window).scrollTop(0);
            });
        };createNode: function() {
            $('body').append($returnTop);
        };
    };
    var gotop1 = new goTop('body');
});
