// DOM Elements
let infoContainer;
let findButton;

// Initialize DOM elements when page loads
document.addEventListener('DOMContentLoaded', () => {
    infoContainer = document.getElementById('infoContainer');
    findButton = document.getElementById('findButton');
    
    // Add event listener to button
    findButton.addEventListener('click', findRandomCharacter);
});

/**
 * Generate a random number between 1 and 83 (total Star Wars characters in API)
 */
function getRandomCharacterId() {
    return Math.floor(Math.random() * 83) + 1;
}

/**
 * Display loading state
 */
function showLoading() {
    infoContainer.innerHTML = `
        <div class="loading">
            <i class="fas fa-spinner"></i>
            <p>Loading...</p>
        </div>
    `;
}

/**
 * Display error message
 */
function showError(message = "Oh No! That person isn't available.") {
    infoContainer.innerHTML = `
        <div class="error-message">
            <p>${message}</p>
        </div>
    `;
}

/**
 * Display character information
 * Sanitizes input to prevent XSS attacks
 */
function displayCharacter(character) {
    const { name, height, gender, birth_year, homeworld } = character;
    
    // Sanitize data to prevent XSS
    const sanitizedName = escapeHtml(name);
    const sanitizedHeight = escapeHtml(height);
    const sanitizedGender = escapeHtml(gender);
    const sanitizedBirthYear = escapeHtml(birth_year);
    const sanitizedHomeworld = escapeHtml(homeworld);
    
    infoContainer.innerHTML = `
        <h2 class="character-name">${sanitizedName}</h2>
        <div class="character-info">
            <p><strong>Height:</strong> ${sanitizedHeight}</p>
            <p><strong>Gender:</strong> ${sanitizedGender}</p>
            <p><strong>Birth Year:</strong> ${sanitizedBirthYear}</p>
            <p><strong>Home World:</strong> ${sanitizedHomeworld}</p>
        </div>
    `;
}

/**
 * Escape HTML to prevent XSS attacks
 */
function escapeHtml(text) {
    const map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
    };
    return String(text).replace(/[&<>"']/g, (m) => map[m]);
}

/**
 * Fetch character data from SWAPI
 * Validates character ID before making request
 */
async function getCharacterData(characterId) {
    // Validate characterId
    if (!Number.isInteger(characterId) || characterId < 1 || characterId > 83) {
        throw new Error('Invalid character ID');
    }
    
    try {
        const response = await fetch(`https://www.swapi.tech/api/people/${characterId}`);
        
        if (!response.ok) {
            throw new Error('Character not found');
        }
        
        const data = await response.json();
        
        // Validate response data
        if (!data || !data.result || !data.result.properties) {
            throw new Error('Invalid API response');
        }
        
        return data.result.properties;
    } catch (error) {
        console.error('Error fetching character:', error);
        throw error;
    }
}

/**
 * Fetch homeworld name from URL
 */
async function getHomeworldName(homeworldUrl) {
    try {
        const response = await fetch(homeworldUrl);
        
        if (!response.ok) {
            return 'Unknown';
        }
        
        const data = await response.json();
        return data.result.properties.name;
    } catch (error) {
        console.error('Error fetching homeworld:', error);
        return 'Unknown';
    }
}

/**
 * Main function to find and display a random character
 */
async function findRandomCharacter() {
    // Disable button during loading
    findButton.disabled = true;
    
    // Show loading state
    showLoading();
    
    try {
        // Get random character ID
        const characterId = getRandomCharacterId();
        
        // Fetch character data
        const characterData = await getCharacterData(characterId);
        
        // Fetch homeworld name
        const homeworldName = await getHomeworldName(characterData.homeworld);
        
        // Prepare character object with homeworld name
        const character = {
            name: characterData.name,
            height: characterData.height,
            gender: characterData.gender,
            birth_year: characterData.birth_year,
            homeworld: homeworldName
        };
        
        // Display character information
        displayCharacter(character);
        
    } catch (error) {
        // Display error message
        showError();
    } finally {
        // Re-enable button
        findButton.disabled = false;
    }
}
