[Data Commons](../)

# API Tests<hr>
Experiments with using Javascript to call Google Data Commons API.
<!--
# Good Paying Jobs
Goal 1. No Poverty - Good Paying Jobs and Assistance
-->

<style>
    body {
      font-family: 'Arial', sans-serif;
      margin: 20px;
      padding: 20px;
    }

    button {
      background-color: #4CAF50;
      color: white;
      padding: 10px 15px;
      margin: 10px 0;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }

    label {
      display: block;
      margin: 10px 0;
    }

    input {
      padding: 8px;
      width: 100%;
      box-sizing: border-box;
      margin-bottom: 10px;
    }

    #resultContainer {
      margin-top: 20px;
      padding: 10px;
      border: 1px solid #ddd;
      border-radius: 4px;
    }

    .suggestion-container {
      margin-top: 5px;
    }

    .suggestion-bubble {
      display: inline-block;
      padding: 5px 10px;
      margin-right: 5px;
      cursor: pointer;
      border-radius: 4px;
      border: 1px solid white; /* Changed border color to white */
    }

    .suggestion-bubble:hover {
      background-color: yellow;
    }
    .bottomInput {
      background-color: #ccc;
      padding: 18px;
      /*
      position: fixed;
      right: 0;
      top: 0;
      */
    }
  </style>

## API Demo

You can find the desired DCID and property from these sources:

- [Data Commons Place Browser](https://datacommons.org/place)
- [Data Commons StatVar Browser](https://datacommons.org/tools/statvar)
- [Data Commons Browser](https://datacommons.org/browser/)

For API examples, you can check:

- [Data Commons REST API Documentation](https://docs.datacommons.org/api/rest/v2)

Enter DCID and Property examples below to view JSON Output

<div class="bottomInput">

<!-- Hid these until javascript modified -->
<!--
<div>
  <label for="dcidInput">Enter DCID:</label>
  <div class="suggestion-container" id="dcidSuggestions">
    <span class="suggestion-bubble">geoId/06</span>
    <span class="suggestion-bubble">Count_Jobs_EconomicDevelopmentAdministration_JobsCreated</span>
    <span class="suggestion-bubble">geoId/13</span>
   
  </div>
  
</div>

<div>
  <label for="propertyInput">Enter Property:</label>
  <div class="suggestion-container" id="propertySuggestions">
    <span class="suggestion-bubble"><-</span>
    <span class="suggestion-bubble">-></span>
    <span class="suggestion-bubble">->*</span>
    <span class="suggestion-bubble">->[nearbyPlaces,landArea]</span>
  </div>
  
</div>
-->

<div style="float:left">
DCID:<br>
<input type="text" id="dcidInput" placeholder="e.g., geoId/06" value="Count_Jobs_EconomicDevelopmentAdministration_JobsCreated">
</div>

<div style="float:left">
Property<br>
<input type="text" id="propertyInput" placeholder="e.g., <-" value="->*">
</div>

<div style="float:left">
&nbsp;
<button id="downloadButton" style="float:right;background-color:#999;">Download</button>
<button id="loadDataButton" style="margin-right:10px">View JSON</button>
</div>

<div style="clear:both"></div>

</div>


<div id="resultContainer">JSON Output from Google Data Commons API</div>
<br>

### API Examples

**To find the properties related to `geoId/06`**  
Display a list of properties using the symbol `->`.

    DCID: geoId/06
    Property: ->


**To display all the properties of JobsCreated**  
Display all values of its properties using `->*` to indicate all records.

    DCID: Count_Jobs_EconomicDevelopmentAdministration_JobsCreated
    Property: ->*


**To display `nearbyPlaces` and `landArea` of Georgia**  
Pass a list in the properties column.

    DCID: geoID/13
    Property: ->[nearbyPlaces, landArea]

<!--
The following is only functional when built into the "dist" repo. [View built version](../../dist/jobs/).
-->

```js
  function addSuggestionToInput(suggestion, inputId) {
    document.getElementById(inputId).value = suggestion;
  }

  // TO DO - Avoid use of event.target.parentNode

  // Event listeners for suggestion bubbles
  document.querySelectorAll('.suggestion-bubble').forEach(item => {
    item.addEventListener('click', event => {
      // Get the suggestion bubble text
      const suggestion = event.target.innerText;
      // Get the corresponding input field id
      const inputId = event.target.parentNode.nextElementSibling.id;
      // Add suggestion to the input field
      addSuggestionToInput(suggestion, inputId);
    });
  });
```

```js
  import {loadDataCommons,displayJsonData} from "../components/data_loader.js";
```

```js
  document.getElementById('loadDataButton').addEventListener('click', () => 
    {
        const apiKey = 'AIzaSyCTI4Xz-UW_G2Q2RfknhcfdAnTHq5X5XuI';
        const dcidInput = document.getElementById('dcidInput').value;
        const propertyInput = document.getElementById('propertyInput').value;

        console.log('DCID:', dcidInput);
        console.log('Property:', propertyInput);

        loadDataCommons(apiKey, dcidInput, propertyInput).then(data => {
            console.log(data);
            displayJsonData(data);
            })
                .catch(error => {
                    console.error('Error loading data:', error);
            });
        
    }
  );
```

```js
  // Download JSON button click event
  document.getElementById("downloadButton").addEventListener("click", function() {
    const resultData = document.getElementById("resultContainer").textContent;
    const data = "data:text/json;charset=utf-8," + encodeURIComponent(resultData);
    const downloadButton = document.createElement("a");
    downloadButton.setAttribute("href", data);
    downloadButton.setAttribute("download", "data.json");
    downloadButton.click();
  });
```
