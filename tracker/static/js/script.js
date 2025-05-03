function calculateCalories() {
    let total = 0;
    const foodItems = document.querySelectorAll('.food-item');

    foodItems.forEach(item => {
        const foodName = item.getAttribute('data-name').toLowerCase();
        const quantityInput = item.querySelector(`[name="${foodName}"]`);
        const quantity = parseFloat(quantityInput.value) || 0;
        const caloriesPerGramText = item.querySelector('.card-text').textContent;
        const caloriesPerGram = parseFloat(caloriesPerGramText.split(':')[1].split(' ')[0]);

        total += quantity * caloriesPerGram;
    });

    document.getElementById('totalCalories').textContent = `${total.toFixed(2)} calories`;
    showCalorieTip(total);
}

function showCalorieTip(total) {
    let tipBox = document.getElementById('calorieTip');
    if (!tipBox) {
        // Create the tip box if it doesn't exist
        tipBox = document.createElement('div');
        tipBox.id = 'calorieTip';
        tipBox.className = 'alert alert-info mt-3 text-center';
        document.querySelector('.text-center.mt-5').appendChild(tipBox);
    }

    let tip = "";

    if (total === 0) {
        tip = "Add some food to get started!";
    } else if (total < 500) {
        tip = "Low calorie intake. Consider eating more for energy.";
    } else if (total < 1500) {
        tip = "Good balance! You're within a moderate range.";
    } else {
        tip = "High calorie intake. Consider exercising to balance it out.";
    }

    tipBox.textContent = tip;
    tipBox.style.display = "block";

    // Automatically scroll to the tip
    tipBox.scrollIntoView({ behavior: "smooth" });
}

function searchFood(event) {
    event.preventDefault();  // Stops the form from submitting

    const foodItems = [
        { id: 'yogurt', calPerGram: 1.0 },
        { id: 'dates', calPerGram: 3.0 },
        { id: 'banana', calPerGram: 1.0 },
        { id: 'ice_cream', calPerGram: 2.0 },
        { id: 'burger', calPerGram: 3.0 },
        { id: 'pizza', calPerGram: 3.0 },
        { id: 'orange', calPerGram: 0.0 },
        { id: 'apple', calPerGram: 1.0 },
        { id: 'chicken', calPerGram: 2.0 },
        { id: 'biscuits', calPerGram: 4.5 },
        { id: 'fish', calPerGram: 2.0 },
        { id: 'rice', calPerGram: 1.3 }
    ];

    let total = 0;
    for (const item of foodItems) {
        const quantity = parseFloat(document.getElementById(`quantity_${item.id}`).value) || 0;
        total += quantity * item.calPerGram;
    }

    // Display result dynamically
    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = `<h4>Total Calories: ${total.toFixed(2)}</h4>`;
    showCalorieTip(total);
}

function filterFood() {
    const input = document.getElementById('search-input');
    const filter = input.value.toLowerCase();
    const foodItems = document.querySelectorAll('.food-item');
    
    foodItems.forEach(item => {
        const name = item.getAttribute('data-name').toLowerCase();
        item.style.display = name.includes(filter) ? '' : 'none';
    });
    
}

function resetInputs() {
    const inputs = document.querySelectorAll('input[type="number"]');
    inputs.forEach(input => input.value = '');

    document.getElementById('totalCalories').textContent = '';

    const tipBox = document.getElementById('calorieTip');
    if (tipBox) {
        tipBox.style.display = 'none';
    }

    const resultDiv = document.getElementById("result");
    if (resultDiv) {
        resultDiv.innerHTML = '';
    }
}
