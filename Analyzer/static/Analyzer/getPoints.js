


// function initMap() {
//             var location = {lat: 34, lng: 27};
//             var map = new google.maps.Map(document.getElementById('map'), {
//                 zoom: 2,
//                 center: location
//                 });
//         }

function initPoint(location, map){
  var marker = new google.maps.Marker({
    position: location,
    map: map
  });
  }

function processData(data, map, offset){
            
  if(data){
    offset++;                
    clearTimeout(0);
    var location = JSON.stringify(data);
    geocodeAddress(location,map)
    setTimeout(function(){
    doPoll(map, offset);
    },1000); 
  }else{
    doPoll(map, offset);
  }            
}
function start(map){
  //var map = initMap();
  updateButton();
  doPoll(map,0);
}
function doPoll(map, offset){
  
 $.ajax({
  type: 'GET',
  url: 'http://localhost:8000/Analyzer/'+offset +'/coordinates/',
  success: function(data){
  processData(data, map, offset);
          }
        })
      }       
        

function geocodeAddress(location, map){
  var geocoder = new google.maps.Geocoder();
  geocoder.geocode({'address': location}, function(results, status){
  if(status === 'OK'){
    initPoint(results[0].geometry.location, map);
      }else{
        alert(status);
            }
        })

}

function updateButton(){
  var btn = document.getElementById("startButton");
  var icon = btn.getElementsByTagName('span')[0];
  
  if(btn.value == "start"){
    btn.value = "stop";
    btn.innerHTML = "Stop ";
    var newSpan = document.createElement('span');
    newSpan.setAttribute('class', 'glyphicon glyphicon-remove-sign');
    newSpan.setAttribute('id','startIcon');
    btn.appendChild(newSpan);
  
  }else{
    btn.innerHTML = "Start ";
    btn.value = "start";
    var newSpan = document.createElement('span');
    newSpan.setAttribute('class', 'glyphicon glyphicon-ok-sign');
    newSpan.setAttribute('id','startIcon');
    btn.appendChild(newSpan);

  }
}
