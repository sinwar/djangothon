$(document).ready(function(){

  function getData() {
    $.get("http://127.0.0.1:8000/file", function( data ) {
      //var sample = 'digraph g { a -> b; }';
      var sample = data;
      var options = {
        format: 'svg'
        // format: 'png-image-element'
      }

      var image = Viz(sample, options);
      var main = document.getElementById('main');
      main.innerHTML = '';

      main.innerHTML = image;		// SVG
      main.appendChild(image);	// PNG
    });
  }

  getData();

});
