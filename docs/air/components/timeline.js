/**
 * Renders or updates a timeline graph with given emissions data.
 * @param {Array} data - The emissions data to plot, assumed to be an array of objects { country_code, year, emission }.
 */
import * as d3 from 'd3';

async function renderEmissionsTimeline(data) {
    // Format and filter data as needed
    data.forEach(d => {
        d.date = d3.timeParse("%Y")(d.year);
    });

    const margin = { top: 20, right: 20, bottom: 60, left: 60 },
          width = 960 - margin.left - margin.right,
          height = 500 - margin.top - margin.bottom;

    // Set up scales
    const x = d3.scaleTime()
                .domain(d3.extent(data, d => d.date))
                .range([0, width]);

    const y = d3.scaleLinear()
                .domain([0, d3.max(data, d => d.emission)])
                .range([height, 0]);

    // Select the SVG element, if it exists, and bind the data
    let svg = d3.select('#emissions-timeline').selectAll('svg').data([data]);

    // Otherwise, create the skeletal chart
    const svgEnter = svg.enter().append('svg');
    const gEnter = svgEnter.append('g');
    svg = svg.merge(svgEnter);

    svg.attr('width', width + margin.left + margin.right)
       .attr('height', height + margin.top + margin.bottom);

    gEnter.attr('transform', `translate(${margin.left},${margin.top})`);

    // X-axis
    gEnter.append('g')
          .attr('class', 'x-axis')
          .attr('transform', `translate(0,${height})`)
          .call(d3.axisBottom(x))
          .selectAll('text')  
            .style('text-anchor', 'end')
            .attr('dx', '-.8em')
            .attr('dy', '.15em')
            .attr('transform', 'rotate(-65)');

    // Y-axis
    gEnter.append('g')
          .attr('class', 'y-axis')
          .call(d3.axisLeft(y));

    // Plot each data point as a circle
    gEnter.selectAll('.dot')
          .data(data)
          .enter().append('circle')
            .attr('class', 'dot')
            .attr('cx', d => x(d.date))
            .attr('cy', d => y(d.emission))
            .attr('r', 3.5)
            .style('fill', d => "steelblue");

    // If you wish to update the graph dynamically, you'd add logic here to handle updates based on new data or selections
}

export { renderEmissionsTimeline };
