[Data Commons](../)

# Air and Climate

Goal 13. Greenhouse Gas Reduction Climate Action

We'll focus on loading from the GDC API with Python here in the "air" folder.

Examples of datacommons.org [API used in Python](https://docs.datacommons.org/api/python/)


[Observable data loaders - for Python?](https://observablehq.com/framework/loaders) - Mentions that Python data loader would be invoked before the md file build, and the md file can access the data generated from the Python data loader. 

Kargil adds: We want to get the input values from the user through our HTML, then pass them to the Python data loader and display that data on our front end.

Loren adds: For interactivity with scalability and speed, javascript interacting with the API is perferable. For pre-loading, we'll use python with a hosted json service. It will be slower, but a Google Colab with JSON REST could probably fetch from GDC API. (Basically one API hitting another API.)

---

### An attempt to async and await

Javascript and python [Data Loader samples from Observable](https://observablehq.com/framework/getting-started#next-steps).

The javascript fetches json with this cmd

	node docs/air/data/forecast.json.js

The python requires running "python"

	python docs/air/data/forecast.json.py

So it seems that python cannot be built from the `yarn build` &nbsp;node.js cmd, but it can be run directly using the command above, or within GitHub Pages or from a Google CoLab API.

What are the steps for saving a file when Observable builds?

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

