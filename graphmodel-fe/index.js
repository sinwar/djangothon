var express = require('express');
var app = express();
var path = require('path');

// viewed at http://localhost:8080
app.get('/schema', function(req, res) {
    res.sendFile('index.html', {root: __dirname })
});

app.listen(3000);