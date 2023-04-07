const header = document.querySelector("header");

window.addEventListener("scroll", function(){
    header.classList.toggle("sticky", window.scrollY > 80);
})












/*
const form = document.querySelector('form');
const recipeList = document.querySelector('#recipe-list');
const noRecipes = document.getElementById('no-recipes');

let recipes = [];

function handleSubmit(event) {
    // Prevent default form submission behavior
    event.preventDefault();

    // Get recipe name, ingredients, and method input values
    const nameInput = document.querySelector('#recipe-name');
    const ingrInput = document.querySelector('#recipe-ingredients');
    const methodInput = document.querySelector('#recipe-method');
    const name = nameInput.value.trim();
    const ingredients = ingrInput.value.trim().split(',').map(i => i.trim());
    const method = methodInput.value.trim();

    // Check if recipe name, ingredients, and method are valid
    if (name && ingredients.length > 0 && method) {
        // Create new recipe object and add it to recipes array
        const newRecipe = { name, ingredients, method };
        recipes.push(newRecipe);
    }

    // Clear form inputs
    nameInput.value = '';
    ingrInput.value = '';
    methodInput.value = '';

    // Add new recipe to recipe list
    displayRecipes();
}

function displayRecipes() {
    recipeList.innerHTML = '';
    recipes.forEach((recipe, index) => {
        const recipeDiv = document.createElement('div');
        // Create div to display the individual recipe, for each recipe
        recipeDiv.innerHTML = `
            <h3>${recipe.name}</h3>
            <p><strong>Ingredients:</strong></p>
            <ul>
            ${recipe.ingredients.map(ingr => `<li>${ingr}</li>`).join('')}
            </ul>
            <p><strong>Method:</strong></p>
            <p>${recipe.method}</p>
            <button class="delete-button" data-index="${index}">Delete</button>`;
        recipeDiv.classList.add('recipe');
        recipeList.appendChild(recipeDiv);
    });

    // Display warning when there are no recipes in the list
    if (recipes.length > 0) {
        noRecipes.style.display = 'none';
    }
    else {
        noRecipes.style.display = 'flex';
    }
}

form.addEventListener('submit', handleSubmit);
*/