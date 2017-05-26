// grab the things we need
var mongoose = require('mongoose');
var Schema = mongoose.Schema;

// create a schema
var heroSchema = new Schema({
  hero_id: Number,
  localized_name: String,
  attack_type: String,
  roles:Array,
  primary_attr:String
});

// the schema is useless so far
// we need to create a model using it
var hero = mongoose.model('hero_stats', heroSchema);

module.exports = hero;