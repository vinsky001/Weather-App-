document.getElementById('search-button').addEventListener('click', function() {
    var locationInput = document.getElementById('location-input');
    var city = locationInput.value;

    // Makes a request to the Python script using API endpoint

    var temperatureElement = document.getElementById('temperature');
    var description = document.getElementById('description');
    var humidityElement = document.getElementById('humidity');
    var windSpeedElement = document.getElementById('wind-speed');


    temperatureElement.textContent = 'Temperature: ' + weatherData.temperature + '°C';
    descriptionElement.textContent = 'Description' + weatherData.description;
    humidityElement.textContent = 'Humidity' + weatherData.humidity;

});

