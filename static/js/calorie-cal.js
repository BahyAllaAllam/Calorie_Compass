document.addEventListener("DOMContentLoaded", function () {
    document.querySelector(".nutrition-report-display").style.display = "none";
    const query = document.querySelector('input[name="query"]');
    query.value = "";


    // Declare a variable to store the chart instance
    let myPieChart;

    // Function to update the pie chart with new data
    function updatePieChart(carb, proteins, fats) {
      if (myPieChart) {
        myPieChart.data.datasets[0].data = [carb, proteins, fats];
        myPieChart.update(); // Update the chart with new data
      } else {
        const chartElement = document.getElementById("nutritionPieChart");
        if (chartElement) {
          var ctx = chartElement.getContext("2d");
          myPieChart = new Chart(ctx, {
            type: "pie",
            data: {
              labels: ["Total Carb %", "Total Proteins %", "Total Fats %"],
              datasets: [
                {
                  data: [carb, proteins, fats],
                  backgroundColor: ["#8d6e07", "#D1E7DD", "#F8D7DA"],
                },
              ],
            },
            options: {
              responsive: true,
              maintainAspectRatio: false,
            },
          });
        }
      }
    }

    // API Fetching
    document.querySelector("form").addEventListener("submit", function (event) {
      event.preventDefault();

      document.querySelector(".loading-indicator").style.display = "block";
      const apiKey = document.querySelector('meta[name="calorie-ninjas-api-key"]').getAttribute('content');
      axios
        .get(`https://api.calorieninjas.com/v1/nutrition?query=${query.value}`, {
          headers: {
            "X-Api-Key": apiKey,
          },
        })
        .then(function (response) {
          document.querySelector(".loading-indicator").style.display = "none";
          document.querySelector(".nutrition-report-display").style.display = "block";
          const data = response.data.items[0];
          document.querySelector(".food-name").textContent = query.value;
          document.querySelector(".calorie-amount").textContent = Math.round(
            data.calories
          );
          const nutritionReportRows = document.querySelectorAll(
            ".nutrition-report tbody tr"
          );

          // size
          nutritionReportRows[0].children[1].textContent =
            data.serving_size_g + " g";

          // Carb
          const carbPercentage = Math.round(
            (data.carbohydrates_total_g / data.serving_size_g) * 100
          ).toFixed(1);
          nutritionReportRows[1].children[1].textContent =
            data.carbohydrates_total_g + " g";
          nutritionReportRows[1].children[2].textContent = carbPercentage + " %";

          // Fiber
          const fiberPercentage = Math.round(
            (data.fiber_g / data.serving_size_g) * 100
          ).toFixed(1);
          nutritionReportRows[2].children[1].textContent = data.fiber_g + " g";
          nutritionReportRows[2].children[2].textContent = fiberPercentage + " %";

          // Sugar
          const sugarPercentage = Math.round(
            (data.sugar_g / data.serving_size_g) * 100
          ).toFixed(1);
          nutritionReportRows[3].children[1].textContent = data.sugar_g + " g";
          nutritionReportRows[3].children[2].textContent = sugarPercentage + " %";

          // Proteins
          const proteinPercentage = Math.round(
            (data.protein_g / data.serving_size_g) * 100
          ).toFixed(1);
          nutritionReportRows[4].children[1].textContent = data.protein_g + " g";
          nutritionReportRows[4].children[2].textContent = proteinPercentage + " %";

          // Sodium
          const sodiumPercentage = Math.round(
            (data.sodium_mg / 1000 / data.serving_size_g) * 100
          ).toFixed(1);
          nutritionReportRows[5].children[1].textContent = data.sodium_mg + " mg";
          nutritionReportRows[5].children[2].textContent = sodiumPercentage + " %";

          // Potassium
          const potassiumPercentage = Math.round(
            (data.potassium_mg / 1000 / data.serving_size_g) * 100
          ).toFixed(1);
          nutritionReportRows[6].children[1].textContent =
            data.potassium_mg + " mg";
          nutritionReportRows[6].children[2].textContent =
            potassiumPercentage + " %";

          // Fats
          const fatPercentage = Math.round(
            (data.fat_total_g / data.serving_size_g) * 100
          ).toFixed(1);
          nutritionReportRows[7].children[1].textContent = data.fat_total_g + " g";
          nutritionReportRows[7].children[2].textContent = fatPercentage + " %";

          // Saturated Fats
          const satFatPercentage = Math.round(
            (data.fat_saturated_g / data.serving_size_g) * 100
          ).toFixed(1);
          nutritionReportRows[8].children[1].textContent =
            data.fat_saturated_g + " g";
          nutritionReportRows[8].children[2].textContent = satFatPercentage + " %";

          // Cholesterol
          const cholesterolPercentage = Math.round(
            (data.cholesterol_mg / 1000 / data.serving_size_g) * 100
          ).toFixed(1);
          nutritionReportRows[9].children[1].textContent =
            data.cholesterol_mg + " mg";
          nutritionReportRows[9].children[2].textContent =
            cholesterolPercentage + " %";

          // Update the pie chart with new data
          updatePieChart(
            Math.round((data.carbohydrates_total_g / data.serving_size_g) * 100),
            Math.round((data.protein_g / data.serving_size_g) * 100),
            Math.round((data.fat_total_g / data.serving_size_g) * 100)
          );
        })
        .catch(function (error) {
          document.querySelector(".loading-indicator").style.display = "none";
          alert(`Invalid food item: Please enter valid food item`);
        });
    });
});