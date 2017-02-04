var $ = require("jquery");

var Carousel = require("./carousel.js");
require("style-loader!css-loader!../css/carousel.css");
Carousel.init($(".carousel"));

var GoTop = require("./gotop.js");
require("style-loader!css-loader!../css/gotop.css")
new GoTop;

var Waterfall = require("./waterfall.js");
new waterfall;

var Addmore = require("./addmore.js");
new Addmore($('.portfolio'));

var Exposure = require("./exposure.js")
new Exposure($(".exposure"));
