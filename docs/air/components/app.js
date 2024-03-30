import { DatabaseClient } from './dbClient.js';

document.addEventListener('DOMContentLoaded', async () => {
  const dbClient = new DatabaseClient();

  async function loadDataFromUrl(url) {
    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error('Failed to fetch data');
      }
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error fetching data:', error);
      return [];
    }
  }

  async function loadData() {
    // Assuming your server/environment serves files from the root of your project directory
    const data = await loadDataFromUrl('./dist/air/data/EN_ATM_GHGT_AIP_Series.json');
    const countrySelect = document.getElementById("country-select");
    countrySelect.innerHTML = data.map(country =>
      `<option value="${country.country_code}">${country.country_code}</option>`
    ).join('');
  }

  async function updateGraph(selectedCountries, graphType) {
    const data = await dbClient.queryData(); // Assuming dbClient has a method queryData to fetch data
    // Assuming you have a function named "updateGraph" to handle graph updates
    updateGraphWithData(data, selectedCountries, graphType);
  }

  async function updateGraphWithData(data, selectedCountries, graphType) {
    // Implement graph update logic here using the fetched data and selected countries/graph type
    console.log("Updating graph with data:", data);
    console.log("Selected countries:", selectedCountries);
    console.log("Graph type:", graphType);
  }

  loadData();

  document.getElementById('country-select').addEventListener('change', async () => {
    const selectedCountries = Array.from(document.getElementById('country-select').selectedOptions).map(option => option.value);
    const graphType = document.getElementById('graph-type-select').value;
    await updateGraph(selectedCountries, graphType);
  });

  document.getElementById('graph-type-select').addEventListener('change', async () => {
    const selectedCountries = Array.from(document.getElementById('country-select').selectedOptions).map(option => option.value);
    const graphType = document.getElementById('graph-type-select').value;
    await updateGraph(selectedCountries, graphType);
  });
});
