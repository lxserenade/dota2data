var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Dota2data' });
});


/* GET home page. */
router.get('/gallery', function(req, res, next) {
  res.render('gallery', { title: 'Dota2data' });
});

module.exports = router;
