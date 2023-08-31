window.onload = function() {
    // 1초마다 출력되는 문자 변경
    function ChangeString() {
      var stringElement = document.getElementById("iloveyou");
      var currentString = stringElement.innerHTML;
  
      if (currentString == "영원") {
        stringElement.innerHTML = "사랑";
      } else if (currentString == "사랑") {
        stringElement.innerHTML = "빛";
      } else if (currentString == "빛") {
        stringElement.innerHTML = "어둠";
      } else if (currentString == "어둠") {
        stringElement.innerHTML = "삶";
      } else if (currentString == "삶") {
        stringElement.innerHTML = "영원";
        clearTimeout(timer);
      }
  
      timer = setTimeout(ChangeString, 500);
    }
  
    // 첫 실행
    var timer = setTimeout(ChangeString, 500);
  };
  