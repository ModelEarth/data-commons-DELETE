import { fetchJsonData } from './dataFetcher.js';
import * as duckdb from '@duckdb/duckdb-wasm';

export class DatabaseClient {
  constructor() {
    this.db = new duckdb.DuckDB(); // Corrected this line
  }

  async loadDataFromUrl(url) {
    const jsonData = await fetchJsonData(url);
    await this.createTable();
    await this.insertData(jsonData);
  }

  async createTable() {
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

  async insertData(jsonData) {
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

  async queryData() {
    const connection = await this.db.connect();
    // Placeholder for querying DuckDB
    // Return the query result directly
    const result = await connection.query('SELECT * FROM emissions');
    connection.close();
    return result;
  }
}
