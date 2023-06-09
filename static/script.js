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

    switch (weatherData.weather[0].main) {
        case 'Clear':
            image.src = '{{ url_for("static", filename="images/clear.png") }}';
            break;

        case 'Rain':
            image.src = '{{ url_for("static", filename="images/rain.png") }}';
            break;

        case 'Snow':
            image.src = '{{ url_for("static", filename="images/snow.png") }}';
            break;

        case 'Clouds':
            image.src = '{{ url_for("static", filename="images/cloud.png") }}';
            break;

        case 'Haze':
            image.src = '{{ url_for("static", filename="images/mist.png") }}';
            break;

        default:
            image.src = '';
    }


    temperature.innerHTML = `${parseInt(weatherData.main.temp)}<span>°C</span>`;
    description.innerHTML = weatherData.weather[0].description;
    humidity.innerHTML = `${weatherData.main.humidity}%`;
    wind.innerHTML = `${parseInt(weatherData.wind.speed)}Km/h`;

    const container = document.querySelector('.container');
    const weatherBox = document.querySelector('.weather-box');
    const weatherDetails = document.querySelector('.weather-details');
    const error404 = document.querySelector('.not-found');

    error404.style.display = 'none';
    error404.classList.remove('fadeIn');
    weatherBox.style.display = '';
    weatherDetails.style.display = '';
    weatherBox.classList.add('fadeIn');
    weatherDetails.classList.add('fadeIn');
    container.style.height = '590px';
}

