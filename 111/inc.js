// inc.js

define(function() {

  var a = 0;

  var inc = {

    add1: function() {
      return a+=10;
    },

    getRes: function() {
      return a;
    }
  };

  return inc;
});
