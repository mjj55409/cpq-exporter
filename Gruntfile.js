module.exports = function(grunt) {
  grunt.initConfig({
    sass: {                              // Tas
      dist: {
        files: {
          'cpq_exporter/static/css/project.css': 'cpq_exporter/static/sass/project.scss'
        }
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-sass');

  grunt.registerTask('default', ['sass']);

};
