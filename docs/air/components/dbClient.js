import { fetchJsonData } from './dataFetcher.js';
import * as duckdb from '@duckdb/duckdb-wasm';
import { DuckDB, DuckDBBindings } from "@duckdb/duckdb-wasm/dist/duckdb-esm.js";

async function initDuckDB() {
    const duckdb_wasm = await DuckDBBindings();
    const db = new DuckDB(duckdb_wasm);
    return db;
}

// Call initDuckDB inside an async function or use await directly if in an async context
(async () => {
    this.db = await initDuckDB();
})();

async function loadDataFromUrl(url) {
    const jsonData = await fetchJsonData(url);
    await this.createTable();
    await this.insertData(jsonData);
}

async function createTable() {
    const connection = await this.db.connect();
    // Create table if not exists
    await connection.query(`
      CREATE TABLE IF NOT EXISTS emissions (
        country_code VARCHAR,
        year VARCHAR,
        emission FLOAT
      )
    `);
    connection.close();
}

async function insertData(jsonData) {
    const connection = await this.db.connect();
    // Insert data into the table
    for (const countryData of jsonData) {
        const countryCode = countryData.country_code;
        for (const data of countryData.data) {
            const year = data.year;
            const emission = data.emission;
            await connection.query(`
          INSERT INTO emissions (country_code, year, emission)
          VALUES ('${countryCode}', '${year}', ${emission})
        `);
        }
    }
    connection.close();
}

async function queryData() {
    const connection = await this.db.connect();
    // Placeholder for querying DuckDB
    // Return the query result directly
    const result = await connection.query('SELECT * FROM emissions');
    connection.close();
    return result;
}

