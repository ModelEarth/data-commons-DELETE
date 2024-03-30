import { DatabaseClient } from './dbClient.js';
import { renderEmissionsTimeline } from './timeline.js'; // Import the visualization function

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
    const data = await loadDataFromUrl('./dist/air/data/EN_ATM_GHGT_AIP_Series.json');
    const countrySelect = document.getElementById("country-select");
    countrySelect.innerHTML = data.map(country =>
      `<option value="${country.country_code}">${country.country_code}</option>`
    ).join('');
  }

  async function updateGraph(selectedCountries, graphType) {
    let data = await dbClient.queryData(); // Fetch all emissions data
    // Filter data based on selected countries (if any are selected)
    if (selectedCountries.length > 0) {
      data = data.filter(record => selectedCountries.includes(record.country_code));
    }
    // For now, we ignore graphType as the timeline visualization doesn't use it
    updateGraphWithData(data);
  }

  async function updateGraphWithData(data) {
    renderEmissionsTimeline(data); // Update the timeline graph with the filtered data
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
