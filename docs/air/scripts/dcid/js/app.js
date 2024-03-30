import { DatabaseClient } from './databaseClient.js';

document.addEventListener('DOMContentLoaded', async () => {
  const dbClient = new DatabaseClient();
  await dbClient.loadDataFromUrl("https://pchj.github.io/data-commons/dist/air/data/EN_ATM_GHGT_AIP_Series.json");

  async function loadData() {
    const data = await dbClient.queryData();
    const countrySelect = document.getElementById("country-select");
    countrySelect.innerHTML = data.map(country =>
      `<option value="${country.country_code}">${country.country_code}</option>`
    ).join('');
  }

  async function updateGraph(selectedCountries, graphType) {
    const data = await dbClient.queryData(); // Adjust this call as necessary
    // Implement the logic for updating the graph based on 'data'
    // This part would involve creating the traces and layout for Plotly as before
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
