const connectToMongo = require('./db')
var cors = require("cors")

const express = require('express')
const app = express()
const port = 5000

app.use(cors())
app.use(express.json())

//Available routes
app.use('/api/auth', require('./routes/auth'))

app.listen(port, () => {
  console.log(`Data analytics backend listening on port ${port}`)
})

connectToMongo()