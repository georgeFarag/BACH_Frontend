const { PythonShell } = require('python-shell');

let options = {
    mode: 'text',
    pythonPath: 'python3',
    pythonOptions: ['-u'], // get print results in real-time
    scriptPath: '',
    args: ['arg1', 'arg2']
};
var path = require('path');

const express = require('express');
const { start } = require('repl');
import { modelStart } from './start';

const app = express()


app.get('', (req, res) => {
   
    res.sendFile(path.join(__dirname, './', 'loadStl.html'));


})
const port = 2000
app.get('/run', (req, res) => {
    start
   
    PythonShell.run('pyniryo_test.py', options, function(err, results) {
        if (err) console.log(err);
        // results is an array consisting of messages collected during execution
        console.log('results: %j', results);
    });


})
app.listen(port, () => console.log(`Example app listening on port 
${port}!`))

