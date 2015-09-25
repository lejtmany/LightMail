/// <reference path="typings/gulp/gulp.d.ts" />
//// Include gulp
//var gulp = require('gulp');
//
//// Include Our Plugins
//var jshint = require('gulp-jshint');
//var sass = require('gulp-sass');
//var concat = require('gulp-concat');
//var uglify = require('gulp-uglify');
//var rename = require('gulp-rename');
//
//// Lint Task
//gulp.task('lint', function() {
//    return gulp.src('js/*.js')
//        .pipe(jshint())
//        .pipe(jshint.reporter('default'));
//});
//
//// Compile Our Sass
//gulp.task('sass', function() {
//    return gulp.src('scss/*.scss')
//        .pipe(sass())
//        .pipe(gulp.dest('css'));
//});
//
//// Concatenate & Minify JS
//gulp.task('scripts', function() {
//    return gulp.src('js/*.js')
//        .pipe(concat('all.js'))
//        .pipe(gulp.dest('dist'))
//        .pipe(rename('all.min.js'))
//        .pipe(uglify())
//        .pipe(gulp.dest('dist'));
//});
//
//// Watch Files For Changes
//gulp.task('watch', function() {
//    gulp.watch('js/*.js', ['lint', 'scripts']);
//    gulp.watch('scss/*.scss', ['sass']);
//});
//
//// Default Task
//gulp.task('default', ['lint', 'sass', 'scripts', 'watch']);

var gulp = require('gulp');
var uglify = require('gulp-minify-css');
var rename = require('gulp-rename');
var less = require('gulp-less');
var debug = require('gulp-debug')
var concat = require('gulp-concat')

gulp.task('less', function(){
	return  gulp.src('./Mail/static/bower_components/flat-ui/less/flat-ui.less')
	 .pipe(less())
	 .pipe(rename('my-flat-ui.css'))
	 .pipe(gulp.dest('./Mail/static/bower_components/flat-ui/dist/css'))
	 .pipe(rename('my-flat-ui.min.css'))
	 .pipe(uglify())
	 .pipe(gulp.dest('./Mail/static/Mail/css'));
});

gulp.task('watch', function(){
	gulp.watch('./Mail/static/bower_components/flat-ui/less/variables.less', ['less']);
});

gulp.task('default',['less','watch']);



