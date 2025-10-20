// DOM Elements
let screen;
let infoDisplay;
let randomBtn;
let prevBtn;
let nextBtn;

// Global variable to track current Pokemon ID
let currentPokemonId = null;

// Total number of Pokemon in the API (Gen 1-9)
const MAX_POKEMON = 1010;

// Initialize DOM elements when page loads
document.addEventListener('DOMContentLoaded', () => {
    screen = document.getElementById('screen');
    infoDisplay = document.getElementById('infoDisplay');
    randomBtn = document.getElementById('randomBtn');
    prevBtn = document.getElementById('prevBtn');
    nextBtn = document.getElementById('nextBtn');
    
    // Add event listeners
    randomBtn.addEventListener('click', getRandomPokemon);
    prevBtn.addEventListener('click', getPreviousPokemon);
    nextBtn.addEventListener('click', getNextPokemon);
});

/**
 * Generate a random Pokemon ID
 */
function getRandomPokemonId() {
    return Math.floor(Math.random() * MAX_POKEMON) + 1;
}

/**
 * Display loading state
 */
function showLoading() {
    screen.innerHTML = `
        <div class="loading">
            <div class="loading-spinner"></div>
            <p>Loading...</p>
        </div>
    `;
    infoDisplay.innerHTML = `
        <p class="initial-text">Loading Pokémon data...</p>
    `;
}

/**
 * Display error message
 */
function showError(message = "Oh no! That Pokemon isn't available...") {
    screen.innerHTML = `
        <div class="loading">
            <p style="color: #ff4444;">${message}</p>
        </div>
    `;
    infoDisplay.innerHTML = `
        <p class="error-message">${message}</p>
    `;
}

/**
 * Display Pokemon on screen (image)
 */
function displayPokemonImage(pokemon) {
    const imageUrl = pokemon.sprites.other['official-artwork'].front_default || 
                     pokemon.sprites.front_default;
    
    screen.innerHTML = `
        <img src="${imageUrl}" alt="${pokemon.name}">
    `;
}

/**
 * Display Pokemon info
 */
function displayPokemonInfo(pokemon) {
    // Get types
    const types = pokemon.types.map(typeInfo => 
        `<span class="type-badge">${typeInfo.type.name}</span>`
    ).join(' ');
    
    infoDisplay.innerHTML = `
        <div class="pokemon-name">${pokemon.name}</div>
        <div class="pokemon-info">
            <p><strong>Pokemon n°</strong> ${pokemon.id}</p>
            <p><strong>Height:</strong> ${pokemon.height / 10}m</p>
            <p><strong>Weight:</strong> ${pokemon.weight / 10}kg</p>
            <p><strong>Type:</strong> ${types}</p>
        </div>
    `;
}

/**
 * Fetch Pokemon data from PokeAPI
 */
async function fetchPokemon(pokemonId) {
    try {
        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonId}`);
        
        if (!response.ok) {
            throw new Error('Pokemon not found');
        }
        
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching Pokemon:', error);
        throw error;
    }
}

/**
 * Get and display a random Pokemon
 */
async function getRandomPokemon() {
    // Disable buttons during loading
    disableButtons();
    
    // Show loading state
    showLoading();
    
    try {
        // Get random Pokemon ID
        const pokemonId = getRandomPokemonId();
        
        // Fetch Pokemon data
        const pokemon = await fetchPokemon(pokemonId);
        
        // Update current Pokemon ID
        currentPokemonId = pokemon.id;
        
        // Display Pokemon
        displayPokemonImage(pokemon);
        displayPokemonInfo(pokemon);
        
    } catch (error) {
        // Display error message
        showError();
    } finally {
        // Re-enable buttons
        enableButtons();
    }
}

/**
 * Get and display the previous Pokemon
 */
async function getPreviousPokemon() {
    if (currentPokemonId === null) {
        return;
    }
    
    // Disable buttons during loading
    disableButtons();
    
    // Show loading state
    showLoading();
    
    try {
        // Calculate previous ID (wrap around if at first Pokemon)
        let previousId = currentPokemonId - 1;
        if (previousId < 1) {
            previousId = MAX_POKEMON;
        }
        
        // Fetch Pokemon data
        const pokemon = await fetchPokemon(previousId);
        
        // Update current Pokemon ID
        currentPokemonId = pokemon.id;
        
        // Display Pokemon
        displayPokemonImage(pokemon);
        displayPokemonInfo(pokemon);
        
    } catch (error) {
        // Display error message
        showError();
    } finally {
        // Re-enable buttons
        enableButtons();
    }
}

/**
 * Get and display the next Pokemon
 */
async function getNextPokemon() {
    if (currentPokemonId === null) {
        return;
    }
    
    // Disable buttons during loading
    disableButtons();
    
    // Show loading state
    showLoading();
    
    try {
        // Calculate next ID (wrap around if at last Pokemon)
        let nextId = currentPokemonId + 1;
        if (nextId > MAX_POKEMON) {
            nextId = 1;
        }
        
        // Fetch Pokemon data
        const pokemon = await fetchPokemon(nextId);
        
        // Update current Pokemon ID
        currentPokemonId = pokemon.id;
        
        // Display Pokemon
        displayPokemonImage(pokemon);
        displayPokemonInfo(pokemon);
        
    } catch (error) {
        // Display error message
        showError();
    } finally {
        // Re-enable buttons
        enableButtons();
    }
}

/**
 * Disable all buttons
 */
function disableButtons() {
    randomBtn.disabled = true;
    prevBtn.disabled = true;
    nextBtn.disabled = true;
}

/**
 * Enable all buttons
 */
function enableButtons() {
    randomBtn.disabled = false;
    prevBtn.disabled = false;
    nextBtn.disabled = false;
}
