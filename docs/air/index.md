# Data Commons - Air and Climate

## Goal 13: Greenhouse Gas Reduction Climate Action

### Emissions Data Visualizations

```html
<div>
  <select id="country-select" multiple>
    <option value="USA">USA</option>
    <!-- Add options dynamically using JavaScript -->
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
const db = DuckDBClient.of({ air: FileAttachment("data/EN_ATM_GHGT_AIP_Series.json").json() });


const queryData = async () => {
  const data = await db.air;
  return data;
};

  const loadData = async () => {
    const data = await queryData();
    const countrySelect = document.getElementById("country-select");
    countrySelect.innerHTML = "";
    data.forEach((country) => {
      const option = document.createElement("option");
      option.value = country.country_code;
      option.textContent = country.country_code;
      countrySelect.appendChild(option);
    });
  };

  const updateGraph = async (selectedCountries, graphType) => {
    const data = await queryData();
    const traces = [];
    const layout = {
      title: 'Emissions Data Visualization',
      xaxis: { title: 'Year' },
      yaxis: { title: 'Emissions (Metric Tons)' }
    };

loadData();

  document.getElementById('country-select').addEventListener('change', () => {
    const selectedCountries = Array.from(document.getElementById('country-select').selectedOptions).map((option) => option.value);
    const graphType = document.getElementById('graph-type-select').value;
    updateGraph(selectedCountries, graphType);
  });

  document.getElementById('graph-type-select').addEventListener('change', () => {
    const selectedCountries = Array.from(document.getElementById('country-select').selectedOptions).map((option) => option.value);
    const graphType = document.getElementById('graph-type-select').value;
    updateGraph(selectedCountries, graphType);
  });

```

---

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

