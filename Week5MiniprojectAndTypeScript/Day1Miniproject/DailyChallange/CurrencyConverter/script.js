// DOM Elements
let fromCurrencySelect;
let toCurrencySelect;
let amountInput;
let convertBtn;
let switchBtn;
let loadingDiv;
let resultDiv;
let resultAmount;
let conversionRate;
let errorDiv;

// API Configuration
// Using a demo API key - for production, get your own key from https://www.exchangerate-api.com/
// Free tier: 1,500 requests/month
const API_KEY = 'bae94d58236b1ff5020c97e7';
const BASE_URL = 'https://v6.exchangerate-api.com/v6';

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    // Get DOM elements
    fromCurrencySelect = document.getElementById('fromCurrency');
    toCurrencySelect = document.getElementById('toCurrency');
    amountInput = document.getElementById('amount');
    convertBtn = document.getElementById('convertBtn');
    switchBtn = document.getElementById('switchBtn');
    loadingDiv = document.getElementById('loading');
    resultDiv = document.getElementById('result');
    resultAmount = document.getElementById('resultAmount');
    conversionRate = document.getElementById('conversionRate');
    errorDiv = document.getElementById('error');

    // Add event listeners
    convertBtn.addEventListener('click', convertCurrency);
    switchBtn.addEventListener('click', switchCurrencies);
    
    // Allow Enter key to trigger conversion
    amountInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            convertCurrency();
        }
    });

    // Load supported currencies
    loadSupportedCurrencies();
});

/**
 * Fetch all supported currencies from the API
 */
async function loadSupportedCurrencies() {
    try {
        // Using the codes endpoint to get all supported currencies
        const response = await fetch(`${BASE_URL}/${API_KEY}/codes`);
        
        if (!response.ok) {
            throw new Error('Failed to fetch currencies');
        }

        const data = await response.json();

        if (data.result === 'success') {
            populateCurrencySelects(data.supported_codes);
        } else {
            throw new Error('API returned an error');
        }

    } catch (error) {
        console.error('Error loading currencies:', error);
        showError('Failed to load currencies. Please check your API key and try again.');
        fromCurrencySelect.innerHTML = '<option value="">Error loading currencies</option>';
        toCurrencySelect.innerHTML = '<option value="">Error loading currencies</option>';
    }
}

/**
 * Populate the currency select dropdowns with options
 */
function populateCurrencySelects(currencies) {
    // Clear existing options
    fromCurrencySelect.innerHTML = '';
    toCurrencySelect.innerHTML = '';

    // Add currency options
    currencies.forEach(([code, name]) => {
        // Create option for "From" select
        const optionFrom = document.createElement('option');
        optionFrom.value = code;
        optionFrom.textContent = `${code} - ${name}`;
        fromCurrencySelect.appendChild(optionFrom);

        // Create option for "To" select
        const optionTo = document.createElement('option');
        optionTo.value = code;
        optionTo.textContent = `${code} - ${name}`;
        toCurrencySelect.appendChild(optionTo);
    });

    // Set default values
    fromCurrencySelect.value = 'USD';
    toCurrencySelect.value = 'ILS';
}

/**
 * Convert currency using the API
 */
async function convertCurrency() {
    const fromCurrency = fromCurrencySelect.value;
    const toCurrency = toCurrencySelect.value;
    const amount = parseFloat(amountInput.value);

    // Validation
    if (!fromCurrency || !toCurrency) {
        showError('Please select both currencies');
        return;
    }

    if (isNaN(amount) || amount <= 0) {
        showError('Please enter a valid amount');
        return;
    }

    // Hide previous results and errors
    hideResult();
    hideError();

    // Show loading
    showLoading();

    // Disable button
    convertBtn.disabled = true;

    try {
        // Fetch conversion rate using pair endpoint with amount
        const response = await fetch(
            `${BASE_URL}/${API_KEY}/pair/${fromCurrency}/${toCurrency}/${amount}`
        );

        if (!response.ok) {
            throw new Error('Failed to fetch conversion rate');
        }

        const data = await response.json();

        if (data.result === 'success') {
            displayResult(data, fromCurrency, toCurrency, amount);
        } else {
            throw new Error('Conversion failed');
        }

    } catch (error) {
        console.error('Error converting currency:', error);
        showError('Failed to convert currency. Please try again.');
    } finally {
        hideLoading();
        convertBtn.disabled = false;
    }
}

/**
 * Display the conversion result
 */
function displayResult(data, fromCurrency, toCurrency, amount) {
    const convertedAmount = data.conversion_result;
    const rate = data.conversion_rate;

    resultAmount.textContent = `${convertedAmount.toFixed(2)} ${toCurrency}`;
    conversionRate.textContent = `1 ${fromCurrency} = ${rate.toFixed(4)} ${toCurrency}`;

    showResult();
}

/**
 * Switch the "From" and "To" currencies
 */
function switchCurrencies() {
    const fromValue = fromCurrencySelect.value;
    const toValue = toCurrencySelect.value;

    if (fromValue && toValue) {
        fromCurrencySelect.value = toValue;
        toCurrencySelect.value = fromValue;

        // Automatically convert with switched currencies if we have a valid amount
        if (parseFloat(amountInput.value) > 0) {
            convertCurrency();
        }
    }
}

/**
 * Show loading indicator
 */
function showLoading() {
    loadingDiv.classList.remove('hidden');
}

/**
 * Hide loading indicator
 */
function hideLoading() {
    loadingDiv.classList.add('hidden');
}

/**
 * Show result
 */
function showResult() {
    resultDiv.classList.remove('hidden');
}

/**
 * Hide result
 */
function hideResult() {
    resultDiv.classList.add('hidden');
}

/**
 * Show error message
 */
function showError(message) {
    errorDiv.textContent = message;
    errorDiv.classList.remove('hidden');
}

/**
 * Hide error message
 */
function hideError() {
    errorDiv.classList.add('hidden');
}
