$(function(){
	function getUrlParam(name) {
        var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
        var r = window.location.search.substr(1).match(reg);
        if (r != null) 
        	return unescape(r[2]); 
        return null;
    }
    function disableCurPageBtn(){
	    var node = "#page_" + getUrlParam("page");
	    $(node).addClass("disabled") 	
    }

    function changeMoreHref(node) {
    	var keyword = $(node).children(".block-title").text()
    	var moreHref = "search/?keyword=" + keyword + "&page=1&isSearch=1"
    	$(node).children(".more").children("a").attr("href", moreHref)
    }

    if(getUrlParam("page"))
    	disableCurPageBtn();


    if(!getUrlParam("page")){
    	console.log(1)
    	var nodes = $(".block-head")
    	for(var i = 0; i < nodes.length; ++i)
    		(function(){
    			var keyword = $(nodes[i]).children(".block-title").text()
		    	var moreHref = "search/?keyword=" + keyword + "&page=1&isSearch=1"
		    	$(nodes[i]).children(".more").children("a").attr("href", moreHref)
    		})(i);
    	console.log(2)
    }
})