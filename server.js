const PythonShell = require('python-shell').PythonShell;

PythonShell.run('run.py', null, function (err) {
  if (err) throw err;
  console.log('finished');
});