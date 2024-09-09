document.getElementById('add-meal-button').addEventListener('click', function(event) {
    event.preventDefault();
    // check if the input is valid
    function validateInput(input) {
        const commaSpaceSeparated = input.split(', ').length > 1;
        const commaSeparated = input.split(',').length > 1 && !commaSpaceSeparated;
        const spaceSeparated = input.split(' ').length > 1 && !commaSpaceSeparated;
        const plusSeparated = input.split('+').length > 1;

        if ((commaSeparated && (spaceSeparated || plusSeparated)) ||
            (spaceSeparated && (commaSeparated || plusSeparated)) ||
            (plusSeparated && (commaSeparated || spaceSeparated))) {
            alert('Please use only one type of separator (commaspace, space, or plus sign) to separate food items.');
            return false;
        }

        return true;
    }
    const foodItemsInput = document.querySelector('textarea[name="food_items"]');
    if(!validateInput(foodItemsInput.value)){
        return;
    }
    let foodItems = foodItemsInput.value.split();
    let totalCalories = 0;
    let validInput = true;
    let foodData = "";
    const apiKey = document.querySelector('meta[name="calorie-ninjas-api-key"]').getAttribute('content');
    // Loop through the food items to fetch calories from the API
    Promise.all(foodItems.map(item => {
        return axios.get(`https://api.calorieninjas.com/v1/nutrition?query=${item}`, {
            headers: {
                'X-Api-Key': apiKey
            }
        })
        .then(response => {
            const data = response.data.items;
            if (data.length > 0) {
                for (let i = 0; i < data.length; i++) {
                    totalCalories += data[i].calories;
                    if (i === data.length - 1) {
                        foodData += data[i].serving_size_g + " grams of " + data[i].name;
                    } else {
                        foodData += data[i].serving_size_g + " grams of " + data[i].name + ", ";
                    }
                }
            } else {
                validInput = false;
                alert(`Invalid food items, Please enter valid food items with commaspace, space or plus sign(+) separated values`);
            }
        })
        .catch(error => {
            validInput = false;
            console.error('Error fetching data from API:', error);
            alert(`Error fetching data: Please enter valid food items with commaspace, space or plus sign(+) separated values`);
        });
    }))
    .then(() => {
        if (validInput) {
            // If all inputs are valid, submit the form data along with calculated calories
            const formData = new FormData(document.getElementById('add-meal-form'));
            formData.append('calories', Math.round(totalCalories));
            formData.set('food_items', foodData);
            const submitButton = document.getElementById('add-meal-button');
            const url = submitButton.getAttribute('data-url');

            axios.post(url, formData)
            .then(response => {
                if (response.status === 200) {
                    window.location.href = response.data.redirect_url;
                    location.reload(); // Reload the page to show the new meal
                }
            })
            .catch(error => {
                console.error('Error submitting form:', error);
                alert('Error submitting the form: Please enter vaild food items.');
            });
        }
    });
});
