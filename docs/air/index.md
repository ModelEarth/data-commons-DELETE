[Data Commons](../)

# Air and Climate

Goal 13. Greenhouse Gas Reduction Climate Action

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
