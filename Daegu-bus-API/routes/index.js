const engine = require('../engine/engine.js')
const bodyParser = require('body-parser')
const ejs = require("ejs");



module.exports = (app) => {
  process.env.UV_THREADPOOL_SIZE = 128;
  app.get('/', (req, res) => {
    res.json("hello, world!")
  })

  app.get('/route/search/:text', (req, res) => {

    const text = req.params.text
    
    const callback = (data) => {
      res.send(data);
    }
    engine.route.search(text, callback)
  })

  app.get('/route/:id', (req, res) => {
    const id = req.params.id

    const callback = (data) => {
      res.send(data);
    }

    engine.route.route(id, callback)
  })


  app.get('/station/search/:text', (req, res) => {
    const text = req.params.text

    const callback = (data) => {
      res.send(data);
    }

    engine.station.search(text, callback)
  })

  app.get('/station/:id', (req, res) => {
    const id = req.params.id

    const callback = (data) => {
      res.send(data);
    }
    engine.station.station(id, callback)
  })

  app.get('/stationrow/:id', (req, res) => {
    const id = req.params.id

    const callback = (data) => {
      res.send(data);
    }

    engine.station.stationrow(id, callback)
  })
}

