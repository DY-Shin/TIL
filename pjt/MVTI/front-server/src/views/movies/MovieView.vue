<template>
  <div id="movie-list">
    <!-- <h1>Movie Page</h1> -->
    <MovieList/>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'

export default {
  name: 'MovieView',
  components: {
    MovieList,
  },
  computed:{
  },
  created() {
    this.getMovies()
    this.getRecMovies()
  },
  methods: {
    getMovies(){
      this.$store.dispatch('getMovies')
    },
    getRecMovies(){
      this.$store.dispatch('getRecMovies')
    },
  }
}
</script>

<style>

</style>