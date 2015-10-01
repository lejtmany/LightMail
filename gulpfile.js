/// <reference path="typings/gulp/gulp.d.ts" />

var gulp = require('gulp');
var uglify = require('gulp-minify-css');
var rename = require('gulp-rename');
var less = require('gulp-less');
var debug = require('gulp-debug');
var concat = require('gulp-concat');
var connect = require('gulp-connect');
var gutil = require('gulp-util');
var merge = require('merge-stream')

gulp.task('move_vars', function(){
	return gulp.src('./Mail/static/Mail/css/variables.less')
	  .pipe(gulp.dest('./Mail/static/bower_components/flat-ui/less'));

})

gulp.task('less', ['move_vars'],function(){

	  return gulp.src('./Mail/static/bower_components/flat-ui/less/flat-ui.less')
	 .pipe(less())
	 .pipe(rename('my-flat-ui.css'))
	 .pipe(gulp.dest('./Mail/static/bower_components/flat-ui/dist/css'))
	 .pipe(rename('my-flat-ui.min.css'))
	 .pipe(uglify())
	 .pipe(gulp.dest('./Mail/static/bower_components/flat-ui/dist/css'));
});

gulp.task('watch', function(){
	gulp.watch('./Mail/static/Mail/css/variables.less', ['less']);
  	gulp.watch('less/*.less', ['less']);
});

gulp.task('default',['less','watch']);

gulp.task('webserver', function(){
	connect.server(
    {livereload: true}
    );
});

