import * as duckdb from '@duckdb/duckdb-wasm';

async function initializeDatabase() {
  // Initialize DuckDB-Wasm
  const DuckDB = await duckdb.default();
  const db = new DuckDB();

  // Create a new database in memory (or you can open an existing one)
  const connection = await db.connect();

  // Now, you can run SQL queries using `connection.query`
  // For example, creating a table
  await connection.query(`
    CREATE TABLE test (id INTEGER, name VARCHAR);
    INSERT INTO test VALUES (1, 'Duck'), (2, 'DB');
  `);

  // Querying data
  const result = await connection.query('SELECT * FROM test');
  console.log(result);
  
  // Don't forget to clean up
  connection.close();
  db.dispose();
}

initializeDatabase();

// databaseClient.js
import { fetchJsonData } from './dataFetcher.js';

export class DatabaseClient {
  constructor() {
    this.db = new DuckDB(); // Initialize your DuckDB here
  }

  async loadDataFromUrl(url) {
    const jsonData = await fetchJsonData(url);
    // Assuming a method to load JSON data into DuckDB exists
    // This might involve creating a table and then inserting data
    this.insertData(jsonData);
  }

  async queryData() {
    // Placeholder for querying DuckDB
    // Return the query result directly
    return []; // Return data structure that matches expected format
  }

  insertData(jsonData) {
    // Method to insert jsonData into DuckDB
  }
}

