//require
const express = require('express')
const bodyParser = require('body-parser')
const cors = require('cors');
const app = express()

const PORT = 8080

const server = app.listen(PORT, function(){
 console.log("Listening port "+PORT)
})

app.use(express.static('public'));
app.use(cors());
app.use(bodyParser.json())
app.use(bodyParser.urlencoded())

const router = require('./routes/index.js')(app)
