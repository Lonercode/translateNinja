var a = document.getElementById('why');
a.onkeydown = function(e) {
    if (e.key === "Enter") {
    document.getElementById('btn').click();
    }

};

if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
      navigator.serviceWorker.register("/sw.js").then(function(registration) {
        console.log('ServiceWorker registration successful with scope: ', registration.scope);
      }, function(err) {
        console.log('ServiceWorker registration failed: ', err);
      });
    });
  }