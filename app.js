const searchButton = document.getElementById('search-button');

searchButton.addEventListener('click', () => {
    const cityInput = document.getElementById('location-input');
    const city = cityInput.value;

    if (city == '') {
        return;
}

fetch('/search?city=${city}')
    .then(responce => responce.json)
    .then(data => {
        if (data.error) {
            handleWeatherError();       
    }else {
        displayWeatherData(data);
    }
    });
});

function handleWeatherError(){
    const container = document.querySelector(".container");
    const weatherBox = document.querySelector(".weather-box");
    const weatherDetails = document.querySelector(".weather-details");
    const error404 = document.querySelector(".not-found");

    container.style.height = '400px';
    weatherBox.style.display = 'none';
    weatherDetails.style.display = 'none';
    error404.style.display = 'block';
    error404.classList.add('fadeIn');

}

function displayWeatherData(weatherData){
    const image = document.getElementById('weather-icon');
    const temperature = document.querySelector('.temperature');
    const description = document.querySelector('.weather-text p:last-child');
    const humidity = document.getElementById('humidity');
    const wind = document.getElementById('wind-speed');

}

