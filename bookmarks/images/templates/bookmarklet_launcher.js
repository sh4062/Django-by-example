(function(){
    if(window.myBookmarklet!==undefined){
        myBookmarklet();
    }
    else{
        document.body.appendChild(document.createElement('script')).src='http://127.0.0.1:8000/static/js/bookmarklet.js?r='+Math.floor(Math.random()*99999999999999999999);
        
    }
})();

// jQuery
// 你的用户将会像下面这样在他们的浏览器中添加书签然后使用它：
// 用户从你的网站中拖拽一个链接到他的浏览器。这个链接在它的href属性中包含了 JavaScript 代码。这段代码将会被储存到书签当中。
// 用户访问任意一个网站，然后点击这个书签， 这个书签的 JavaScript 代码就被执行了。
// 由于 JavaScript 代码将会以书签的形式被储存，之后你将不能更新它。这是个很显著的缺点，但是你可以通过实现一个简单的激活脚本来解决这个问题，
//这个脚本从一个 URL 中加载 JavaScript。你的用户将会以书签的形式来保存这个激活脚本，这样你就能在任何时候更新书签代码的内容了。
