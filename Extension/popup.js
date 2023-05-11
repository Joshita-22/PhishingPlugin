
  chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    var url = tabs[0].url;
    document.getElementById('url').textContent = url;
  
    document.getElementById('check').addEventListener('click', function() {
      var markup = "url="+url+"&html="+document.documentElement.innerHTML;
      var xhr=new XMLHttpRequest();
      xhr.open("POST","http://ec2-3-25-106-97.ap-southeast-2.compute.amazonaws.com:8080/",false);
      //xhr.open("POST","http://localhost/plugin_demo1/clientServer.php",false);
      xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
      xhr.send(markup);
      var response = xhr.responseText.trim();
      var resultElement = document.getElementById('result');
      resultElement.textContent = response;
      if (response === "PHISHING") {
        resultElement.style.color = 'red';
      } else {
        resultElement.style.color = 'green';
      }
    });
  });


  
  