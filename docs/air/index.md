
# Data Commons - Air and Climate

## Goal 13: Greenhouse Gas Reduction Climate Action

### Emissions Data Visualizations

```html
<div>
  <select id="country-select" multiple>
    <!-- Options will be dynamically added by JavaScript -->
  </select>
  <select id="graph-type-select">
    <option value="line">Line Graph</option>
    <option value="heatmap">Heatmap</option>
    <option value="area">Stacked Area Plot</option>
    <option value="pie">Pie Chart</option>
  </select>
  <div id="EN_ATM_GHGT_AIP_Data-graph"></div>
</div>
```

```js
import { DatabaseClient } from './components/dbClient.js';
import { fetchJsonData } from './components/dataFetcher.js';

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
      const data = await loadDataFromUrl("./dist/air/data/EN_ATM_GHGT_AIP_Series.json");
      const countrySelect = document.getElementById("country-select");
      countrySelect.innerHTML = data.map(country =>
        `<option value="${country.country_code}">${country.country_code}</option>`
      ).join('');
    }

    async function updateGraph(selectedCountries, graphType) {
      const data = await dbClient.queryData();
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
```

---

# Tutorials:

## Python for Google Data Commons API

[Datacommons.org API used in Python](https://docs.datacommons.org/api/python/)

[Our CoLab for emission timelines](https://colab.research.google.com/drive/1mZC2Pn4oKau9Sz1Q16_qnOK7Tai09uEo#scrollTo=2gMBtmu1MGfq&line=19&uniqifier=1) - Loads from GDC API with Python - Paul

**TO DO:** Invoke our CoLab with REST JSON for Web interactivity.

---

## Building JSON and Fetching with Data Loader

[Observable data loaders](https://observablehq.com/framework/loaders) 

**JavaScript and Python** [Data Loader samples from Observable](https://observablehq.com/framework/getting-started#next-steps).

The JavaScript fetches JSON with this command:

```bash
node docs/air/data/forecast.json.js
```

The Python requires running `python` external to Observable build:

```bash
python docs/air/data/forecast.json.py
```

Python cannot be built from the `yarn build` node.js command, but it can be run directly using the command above, or within GitHub Pages or through a Google CoLab API.

---

## Prerender api.weather.gov with .js

Saves a file when Observable builds using `data/forecast.json.js`. Added `async function fetchData()` since `display(forecast)` returned `Promise{}`.

```js
// Implementation...
```

---

## Embed of GDC Component

Placed in a span or div tag for [built version](../../dist/air/).

```html
<span>
  <script src="https://datacommons.org/datacommons.js"></script>
  <datacommons-line
    header="Population for USA, India, and China"
    places="country/USA country/IND country/CHN"
    variables="Count_Person"
  ></datacommons-line>
</span>
<span style="font-size: 11px;">
  <a href="https://docs.datacommons.org/api/web_components/">Data Commons Web Components</a> - 
  <a href="https://docs.datacommons.org/api/web_components/line">Line Chart Web Component</a>
</span>
```

````
