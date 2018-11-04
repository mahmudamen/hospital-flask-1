(function($) {

  $.fn.skip = function(options) {

    var defaults = {
        _self: this
    };

    init();
    
    function init(){
        $(defaults._self).find('input').keyup(function(){
        	handlePress(this);
        });
    }
    
    function handlePress(element){
    	
    	var maxlength = $(element).attr('maxlength');
    	var currlength = $(element).val().length;
    	
    	if(currlength >= maxlength){
    		$(element).next().focus();
    	}
    }
  }
})(jQuery);