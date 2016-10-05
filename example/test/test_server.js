var chai = require('chai');
var chaiHttp = require('chai-http');
var server = require('../server.js');

var should = chai.should();
var app = server.app;
var storage = server.storage;

chai.use(chaiHttp);

describe('Houndify', function() {
  it('should list items on GET', function(done) {
    chai.request(app)
      .get('/items')
      .end(function(err, res) {
        res.should.have.status(200);
        res.should.be.json; // jshint ignore:line
        res.body.should.be.a('array');
        res.body.should.have.length(3);
        res.body[0].should.be.a('object');
        res.body[0].should.have.property('name');
        res.body[0].name.should.be.a('string');
        done();
      });
  });
  
it('should add an item on POST', function(done) {
    chai.request(app)
      .send({'name': 'Weather'})
      .end(function(err, res) {
        should.equal(err, null);
        res.should.have.status(201);
        res.should.be.json; // jshint ignore:line
        res.body.should.be.a('object');
        res.body.should.have.property('name');
        res.body.name.should.be.a('string');
        res.body.name.should.equal('Weather');
        done();
      });
  });  
 

  

