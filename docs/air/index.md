[Data Commons](../)

# Air and Climate

Goal 13. Greenhouse Gas Reduction Climate Action

---
js:
const db = DuckDBClient.of({ air: FileAttachment("data/EN_ATM_GHGT_AIP_Series.json").json() });
---

---
title: Emissions Data Visualizations
layout: |
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
script: |
    
  const db = DuckDBClient.of({ air: FileAttachment("data/dcid/EN_ATM_GHGT_AIP_Series_byCountry.json").json() });

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

    if (graphType === 'heatmap') {
      // Implement heatmap visualization
    } else if (graphType === 'pie') {
      // Implement pie chart visualization
    } else {
      // Default to line or stacked area plot
      const mode = (graphType === 'line') ? 'lines+markers' : 'lines';
      const stackgroup = (graphType === 'area') ? 'one' : null;

      selectedCountries.forEach((country) => {
        const countryData = data.find((item) => item.country_code === country);
        const years = countryData.data.map((data) => data.year);
        const values = countryData.data.map((data) => data.emission);
        traces.push({
          x: years,
          y: values,
          mode: mode,
          stackgroup: stackgroup,
          name: country
        });
      });

      layout.title = 'Emissions Trend';
    }

    const graphDiv = document.getElementById('EN_ATM_GHGT_AIP_Data-graph');
    Plotly.newPlot(graphDiv, traces, layout);
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
  
---










---

## Python for Google Data Commons API

[Datacommons.org API used in Python](https://docs.datacommons.org/api/python/)

[Our CoLab for emission timelines](https://colab.research.google.com/drive/1mZC2Pn4oKau9Sz1Q16_qnOK7Tai09uEo#scrollTo=2gMBtmu1MGfq&line=19&uniqifier=1) - Loads from GDC API with Python - Paul

TO DO: Invoke our CoLab with REST JSON for Web interactivity.

---

## Building json and Fetching with Data Loader

[Observable data loaders](https://observablehq.com/framework/loaders) 

Javascript and python [Data Loader samples from Observable](https://observablehq.com/framework/getting-started#next-steps).

The javascript fetches json with this cmd

	node docs/air/data/forecast.json.js

The python requires running "python" external to Observable build.

	python docs/air/data/forecast.json.py

Python cannot be built from the `yarn build` &nbsp;node.js cmd, but it can be run directly using the command above, or within GitHub Pages or through a Google CoLab API.

---

## Prerender api.weather.gov with .js

Saves a file when Observable builds using data/forecast.json.js.  
Added "async function fetchData()" since "display (forecast)"" returned "Promise{}"

```js
// Important: Remove ".js" from forecast.json.js
// Pre-render json from the .js file into dist _file/air/data
const forecast = FileAttachment("./data/forecast.json").json();

//display (forecast); // BUG: Displays: Promise {}
//display (temperaturePlot(forecast));

async function fetchData() {
    const forecast = await FileAttachment("./data/forecast.json").json()
    .then(response => {
    	console.log("got it")
    	display(temperaturePlot(response));
    })
    .catch(error => {
        console.error('Error fetching forecast data:', error);
        //return null; or handle the error appropriately
    });
    // return forecast;
}
fetchData();

function temperaturePlot(data, {width} = {}) {
  return Plot.plot({
    title: "Hourly temperature forecast",
    width,
    x: {type: "utc", ticks: "day", label: null},
    y: {grid: true, inset: 10, label: "Degrees (F)"},
    marks: [
      Plot.lineY(data.properties.periods, {
        x: "startTime",
        y: "temperature",
        z: null, // varying color, not series
        stroke: "temperature",
        curve: "step-after"
      })
    ]
  });
}


/*
display(
  Plot.plot({
    title: "Hourly temperature forecast",
    x: {type: "utc", ticks: "day", label: null},
    y: {grid: true, inset: 10, label: "Degrees (F)"},
    marks: [
      Plot.lineY(forecast.properties.periods, {
        x: "startTime",
        y: "temperature",
        z: null, // varying color, not series
        stroke: "temperature",
        curve: "step-after"
      })
    ]
  })
);
*/
```
---
<br>

## Embed of GDC Component

Placed in a span or div tag for [built version](../../dist/air/).

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

