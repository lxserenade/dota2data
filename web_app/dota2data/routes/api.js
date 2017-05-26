var express = require('express');
var router = express.Router();
var match = require('../models/match');
var hero = require('../models/hero_stats');

router.get('/all_matches', function(req, res, next) {
    match.find({}, function(err, docs) {
        if (err) throw err;
        res.json(docs);
    });
});
router.get('/all_heroes', function(req, res, next) {
    hero.find({}, function(err, docs) {
        if (err) throw err;
        res.json(docs);
    });
});
router.get('/matchById/:matchId', function(req, res, next) {
    hero.find({
        match_id: parseInt(req.params.matchId)
    }, function(err, docs) {
        if (err) throw err;
        res.json(docs);
    });
});
router.get('/heroById/:heroId', function(req, res, next) {
    hero.find({
        hero_id: parseInt(req.params.heroId)
    }, function(err, docs) {
        if (err) throw err;
        res.json(docs);
    });
});
router.get('/heroByName/:heroName', function(req, res, next) {
    hero.find({
        localized_name: req.params.heroName
    }, function(err, docs) {
        if (err) throw err;
        res.json(docs);
    });
});
module.exports = router;