const express = require('express');
const app = express();
const http = require('http');
var Web3 = require('web3');
const configuration = require('../build/contracts/Sensors.json');
// const web3 = new Web3(new Web3.providers.HttpProvider("http://127.0.0.1:7545"));
const OPTIONS = {
  defaultBlock: "latest",
  transactionBlockTimeout: 150
};
const web3 = new Web3(new Web3.providers.HttpProvider("http://block.amaxilatis.com:8545", null, OPTIONS));
const contract = new web3.eth.Contract(configuration.abi, configuration.networks[5777].address);
const fs = require('fs');
const bodyParser = require('body-parser');
const cors = require('cors');
const { accounts, seeLastValueHum } = require('../server/utils');

app.use(cors());
app.use(express.json());

const myIndex = process.argv[2];
//console.log('MyIndex: ' + myIndex);
let cnt1 = 0;

// new
(async function () {
  let accountsList = await accounts();
  const myAccount = accountsList[myIndex];
 // console.log(myAccount);

  async function seeValueAttack(){
    let theTimeT = await seeLastValueHum(myIndex, myAccount);
    cnt1 += 1;
    if (cnt1 < 100) {
      setTimeout(seeValueAttack, theTimeT)
    }
  }

  seeValueAttack();

})();

