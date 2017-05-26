// grab the things we need
var mongoose = require('mongoose');
var Schema = mongoose.Schema;

// create a schema
var matchSchema = new Schema({
  match_id: String,
  duration: Number,
  dire_score: Number,
  radiant_score: Number,
  radiant_win:Boolean,
  start_time:Date,
  players:Array,
  first_blood_time:Number
});

// the schema is useless so far
// we need to create a model using it
var match = mongoose.model('matches', matchSchema);

module.exports = match;