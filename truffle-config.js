require("@babel/register");
require("@babel/polyfill");
require('dotenv').config();
//require('babel-preset-es2015')
//require('babel-preset-env')
//require("@babel/preset-es2015")
require("@babel/preset-env")
module.exports = {
  

  networks: {
    development: {
      host: "127.0.0.1",
      port: 7545,
      network_id: "*" // match any network id
    }
  },
  contracts_directory:'./src/contracts/',
  contracts_build_directory: './src/abis/',

  // Set default mocha options here, use special reporters etc.
  mocha: {
    // timeout: 100000
  },

  // Configure your compilers into ethereum source readable code
  compilers: {
    solc: {
      optimizer: {
        enabled: true,
        runs: 200
      }
     
    }
  }
}
